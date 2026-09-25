#!/usr/bin/python
# Filename: RiskAssessment.py
# Description: Bayesian risk-assessment faculty

from rules.examiner.risk.RiskModel import HAZARDS, CURRENCY, Binding, VoyageTrack, LossMatrix
from rules.examiner.risk.RiskModel import load, hazard_probabilities

from maritime.model.zone.ZoneAwareness import ZoneAware
from maritime.model.zone.ZoneRules import SpatialZones

from cos.model.examiner.ConcernExaminer import ConcernExaminer
from cos.core.kernel.Faculty import Faculty
from cos.core.kernel.Context import Context
from cos.core.time.Ticker import Ticker
from cos.core.utilities.ArgList import ArgList
from cos.model.rule.Context import Context as RuleContext
from cos.model.examiner.Precondition import PreconditionSet

import yaml

# Wraps the ASV risk network of Kristensen et al. (2025), Ocean Engineering 338,
# 121937, Fig. 2, as a COS faculty. It registers under /Faculty/Situation/Processors
# so that COLREG.Evaluator.monitor() drives it with a populated RuleContext; no
# change to the evaluator is required.
#
# The faculty always scores and always records. Publishing is advisory: a vessel
# that subscribed to 'risk.assessment' receives the score, a vessel that did not
# is unaffected, exactly as MaritimeSituation.regulate() treats regulation events.
#
# The risk arithmetic - how hazard probabilities are combined and how cost
# accumulates over a voyage - lives in riskcore.py, which has no COS imports and
# is unit-tested by verify_accumulation.py.

class RiskExaminer(ZoneAware, ConcernExaminer):
	TOPIC		= '/Faculty/Risk/Assessment'
	MESSAGE		= 'risk.assessment'

	def __init__(self):
		""" Constructor
		"""
		ConcernExaminer.__init__( self, 'Risk' )

		self.bn			= None
		self.engine		= None
		self.matrix		= LossMatrix()	# Rl, from the territory's risk file
		self.spatial	= SpatialZones()	# Sea.Type -> spatial zone, per territory
		self.tracks		= {}		# Vessel IMO -> VoyageTrack
		self.timer		= None
		self.trace		= False

		# Evidence bindings, simulation term -> BN node
		self.bindings	={
				'collision':[],
				'target':[],
				'environment':[],
				'at_sea':[],
				'auv_operation':[]
			}

		self.gate = PreconditionSet( {
				'collision': ['os','ts'],
				'target': ['os','ts'],
				'at_sea': ['os'],
				'environment': ['os'],
				'auv_operation': ['os','ts.fleet']
				})

		return

	def resolvable(self, binding, rule_ctxt:RuleContext):
		return self.gate.holds( binding, rule_ctxt.situation )

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		ConcernExaminer.on_init(self, ctxt, module)

		config		= ArgList( module.get("config", "") )
		self.trace	= config.IsTrue('trace')

		self.setup( ctxt, config )
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the faculty, loading the network and its bindings
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		poll_at		= config["sample.frequency"]
		self.timer	= Ticker( int(poll_at) ) if poll_at is not None else Ticker( 1 )

		# Zone awareness supplies the map shapes under a vessel, which the
		# spatial classification of Rl needs.
		self.init_zones( ctxt, config, requires=['os'] )

		self.__load_network( ctxt, config["network"] )
		self.__load_bindings( ctxt, config["bindings"] )
		self.__load_matrix( ctxt, config["territory"] )

		gap	= self.gate.undeclared( self.bindings.keys() )
		if gap:
			raise ValueError( f'RiskExaminer: no precondition declared for binding group(s) {gap}' )

		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.cache_shapes( ctxt )
		return

	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates risk for every vessel under assessment.
		Invoked by COLREG.Evaluator.monitor() once the situation faculties have run.
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if (self.engine is None) or (self.timer.signaled() == False):
			return

		try:
			for vessel in rule_ctxt.subjects:
				self.assess( ctxt, rule_ctxt, vessel )
		except Exception as e:
			ctxt.log.error( self.id, f'Runtime error: {str(e)}' )

		return

	def assess(self, ctxt:Context, rule_ctxt:RuleContext, vessel):
		""" Runs one inference pass and scores the vessel
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			vessel -- Vessel under assessment
		"""
		evidence	= self.observe( ctxt, rule_ctxt, vessel )
		if evidence is None:
			return

		self.engine.setEvidence( evidence )
		self.engine.makeInference()

		hazards		= hazard_probabilities( self.engine )

		# Rl is indexed by where the vessel is as well as by what may happen to
		# it, so the spatial zone is resolved before the loss row is taken.
		shapes		= self.survey( vessel )[0]
		zone		= self.spatial.classify( shapes )
		concerns	= self.matrix.row( self.engine, zone )
		serialized	= self.matrix.matlab( self.engine, self.spatial.order )
		cost		= sum( concerns.values() )

		imo			= vessel.config["identifier"]["imo"]
		track		= self.track( imo )
		increment	= track.charge( cost, hazards['any'], evidence )

		report		= {
			'vessel'		: imo,
			'time'			: ctxt.sim.now(),
			'zone'			: zone,			# spatial zone, the i index of Rl
			'matrix'		: serialized,	# the whole of Rl, MATLAB literal, USD
			'hazards'		: hazards,		# marginals, plus 'any' (exact) and 'sum' (eq. 14)
			'exposure'		: concerns,		# Rl row: concern -> expected economic loss
			'cost'			: cost,			# instantaneous expected loss
			'increment'		: increment,	# what was actually added to the voyage total
			'survival'		: track.survival,
			'cumulative'	: track.cost,
			'evidence'		: evidence,
		}

		self.publish( ctxt, vessel, report )
		self.record( ctxt, report )
		return

	def observe(self, ctxt:Context, rule_ctxt:RuleContext, vessel):
		""" Resolves each bound simulation term into a BN evidence state
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			vessel -- Vessel under assessment
		Returns
			A dictionary of BN node name -> state label
		"""
		evidence	= None

		# NOTE: RuleContext.resolve() resolves against rule_ctxt.situation, which the
		# conduct faculties populate per encounter. Terms naming TargetShip therefore
		# only resolve while an encounter is in scope; see the note in the manifest.
		for k,v in self.bindings.items():
			if self.resolvable(k, rule_ctxt) == False:
				continue

			for binding in v:
				value	= rule_ctxt.resolve( binding['term'] )
				if value is None:
					continue			# Unobserved: the node keeps its prior

				state	= binding.discretize( value )
				if state is not None:
					if evidence is None:
						evidence	= {}
						
					evidence[ binding['node'] ]	= state

		return evidence


	def track(self, imo):
		""" Returns the voyage track for a vessel, creating it if needed
		Arguments
			imo -- Vessel IMO
		"""
		if imo not in self.tracks:
			self.tracks[imo]	= VoyageTrack()

		return self.tracks[imo]

	def publish(self, ctxt:Context, vessel, report):
		""" Publishes the assessment. Advisory only - a vessel that did not
		subscribe to the message is unaffected by it.
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel under assessment
			report -- Assessment payload
		"""
		ctxt.ipc.push( self.TOPIC, self.MESSAGE, ctxt, report, 8 )

		if vessel is not None:
			vessel.notify( ctxt, self.MESSAGE, report )

		return

	def record(self, ctxt:Context, report):
		""" Records the assessment. Unconditional - the score is persisted whether
		or not any vessel acted on it.
		Arguments
			ctxt -- Simulation context
			report -- Assessment payload
		"""
		hazards		= report['hazards']

		# The assessment rollup: one row per vessel per sample. CaseId is
		# injected by the partition, so it is not passed here.
		self.data( ctxt, 'risk_assessment', (
			report['time'],
			report['vessel'],
			report['zone'],
			hazards['collision'],
			hazards['grounding'],
			hazards['loss_of_comms'],
			hazards['any'],
			hazards['sum'],
			report['cost'],
			report['increment'],
			report['survival'],
			report['cumulative'],
		) )

		# Rl itself, serialized whole as a MATLAB literal in one column. The
		# fact schema is then fixed: a territory that adds a concern or a zone
		# changes the shape of the literal and nothing else, with no column to
		# add and no warehouse schema to regenerate.
		#
		# The axes are not in the row. Anything decoding these strings needs
		# the order logged at startup - see __load_matrix - and that order must
		# not be edited part way through a sweep.
		self.data( ctxt, 'rl', (
			report['time'],
			report['vessel'],
			report['matrix'],
		) )

		return

	def __load_network(self, ctxt:Context, file):
		""" Loads the Bayesian network
		Arguments
			ctxt -- Simulation context
			file -- File path
		"""
		if file is None:
			ctxt.log.error( self.id, 'No network specified' )
			return

		path		= ctxt.sim.config.resolve( file )
		ctxt.log.info( self.id, f'Loading Bayesian network : {file}' )

		self.bn, self.engine	= load( path, HAZARDS )
		return

	def __load_bindings(self, ctxt:Context, file):
		""" Loads the evidence bindings, the loss values and the concern mapping
		Arguments
			ctxt -- Simulation context
			file -- File path
		"""
		if file is None:
			return

		path		= ctxt.sim.config.resolve( file )
		config		= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes(path) )
		risk		= config['risk']

		for k in self.bindings.keys():
			self.bindings[k]	= [ Binding(b) for b in risk.get(k, []) ]

		# Valuation is NOT read here. What a consequence is worth is a national
		# convention in a national currency, so it belongs to the territory and
		# is loaded by __load_matrix from $(SIMULATION)/risk.yaml. This file
		# binds the network to the simulation and nothing more.
		return

	def __load_matrix(self, ctxt:Context, file):
		""" Loads Rl, the territory's zone-specific loss matrix
		Arguments
			ctxt -- Simulation context
			file -- File path
		"""
		if file is None:
			ctxt.log.error( self.id, 'No territory risk file specified; Rl is undefined' )
			return

		path		= ctxt.sim.config.resolve( file )
		ctxt.log.info( self.id, f'Loading loss matrix Rl : {file}' )

		config		= yaml.safe_load( ctxt.sim.fs.read_file_as_bytes(path) )
		risk		= (config or {}).get( 'risk', {} ) or {}

		self.matrix		= LossMatrix( risk )
		self.spatial	= SpatialZones( risk.get('spatial_zones', {}) )

		for problem in self.spatial.errors() + self.matrix.errors( self.bn ):
			ctxt.log.error( self.id, f'Rl: {problem}' )

		# Rl is stored as a bare matrix literal with no axis labels in the row,
		# so the order that produced it is recorded here. Without this line a
		# stored matrix cannot be decoded after the fact.
		ctxt.log.info( self.id,
					   f'Rl axes [{CURRENCY}]: {self.matrix.axis_labels(self.spatial.order)}' )

		return
