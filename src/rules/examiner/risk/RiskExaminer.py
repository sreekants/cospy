#!/usr/bin/python
# Filename: RiskAssessment.py
# Description: Bayesian risk-assessment faculty

from rules.examiner.risk.RiskModel import HAZARDS, CURRENCY, Binding, VoyageTrack, LossMatrix, ConcernWeights
from rules.examiner.risk.RiskModel import load, hazard_probabilities, individual_risk

from maritime.model.zone.ZoneAwareness import ZoneAware
from maritime.model.zone.ZoneRules import SpatialZones
from maritime.model.zone.Ledger import Ledger

from cos.model.examiner.ConcernExaminer import ConcernExaminer
from cos.core.kernel.Faculty import Faculty
from cos.core.kernel.Context import Context
from cos.core.time.Ticker import Ticker
from cos.core.utilities.ArgList import ArgList
from cos.model.rule.Context import Context as RuleContext
from cos.model.examiner.Precondition import PreconditionSet
from cos.model.rule.Situation import Situation
from cos.math.geometry.Distance import Distance

# maritime.model.vessel.Builder's FLEET prototype. A controller is a flocking
# driver, not a ship, and carries a FLEET-<hash8(guid)> tag rather than an IMO.
FLEET_CONTROLLER	= 800000

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
		self.weights	= ConcernWeights()	# Rw, from the same file
		self.spatial	= SpatialZones()	# Sea.Type -> spatial zone, per territory
		self.tracks		= {}		# Vessel guid -> VoyageTrack (COS-029-02)
		self.timer		= None
		self.trace		= False
		self.range		= 4000.0	# Encounter range for pair evidence [m], COLREG stage 2
		self.states		= {}		# Node -> state labels
		self.rejected	= set()		# (node, state) pairs already logged

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
		ConcernExaminer.on_init(self, ctxt, module)		# runs setup(); calling it again loads everything twice
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the faculty, loading the network and its bindings
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.trace	= config.IsTrue('trace')
		poll_at		= config["sample.frequency"]
		self.timer	= Ticker( int(poll_at) ) if poll_at is not None else Ticker( 1 )
		self.range	= config.ToFloat( 'range', self.range )

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
		self.record_weights( ctxt )
		return

	def record_weights(self, ctxt:Context):
		""" Records Rw once per run, unapplied to Rl (REQ-004-08)
		Arguments
			ctxt -- Simulation context
		"""
		if self.weights.errors():
			return

		now		= ctxt.sim.now()
		for concern, weight in self.weights.normalised().items():
			self.data( ctxt, 'rw', (now, concern, weight, float(self.weights.declared[concern])) )
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

		saved	= rule_ctxt.situation
		try:
			for vessel in rule_ctxt.subjects:
				if self.tracked( vessel ) == False:
					continue
				try:
					self.assess( ctxt, rule_ctxt, vessel )
				except Exception as e:
					ctxt.log.error( self.id, f'{getattr(vessel, "name", vessel)}: {e}' )
		finally:
			rule_ctxt.situation	= saved
			self.reset_resolver( ctxt, rule_ctxt )

		return

	@staticmethod
	def tracked(vessel)->bool:
		""" Whether a vessel carries a voyage of its own (COS-029-04)
		Arguments
			vessel -- Candidate vessel
		Returns
			False for a fleet controller, True otherwise

		A fleet controller is not a vessel. It never moves, its box stays at
		(0,0), and it exists only to fly its members. Assessing it would put a
		voyage track and a run of fact rows against something that is not at
		sea. It is excluded here, explicitly, rather than by its identity
		happening not to collide with a real one.

		The record type is the test, not the class: Fleet passes Type.SEAPLANE
		to its base constructor, so the runtime type of a controller is not
		distinctive. The class name is checked as well, so a Fleet built from
		JSON with no type still resolves.
		"""
		try:
			if int( vessel.config["type"] ) == FLEET_CONTROLLER:
				return False
		except (KeyError, TypeError, ValueError, AttributeError):
			pass

		return vessel.__class__.__name__ != 'Fleet'

	def encounters(self, rule_ctxt:RuleContext, vessel):
		""" The situations a vessel is assessed in (COS.008)
		Arguments
			rule_ctxt -- Rule context
			vessel -- Vessel under assessment
		Returns
			One situation per other vessel within range, or the vessel alone when none is
		"""
		targets	= [ v for v in (rule_ctxt.vessels or []) if (v is not vessel)
					and Distance.euclidean(vessel.location, v.location) <= self.range ]

		if not targets:
			return [ Situation(vessel, None) ]

		return [ Situation(vessel, target) for target in targets ]

	def infer(self, ctxt:Context, rule_ctxt:RuleContext, situation):
		""" Runs one inference pass for one situation
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			situation -- Own ship, and target if any
		Returns
			(evidence, hazards), or None when nothing resolves
		"""
		evidence	= self.observe( ctxt, rule_ctxt, situation )
		if evidence is None:
			return None

		self.engine.setEvidence( evidence )
		self.engine.makeInference()

		return evidence, hazard_probabilities( self.engine )

	def assess(self, ctxt:Context, rule_ctxt:RuleContext, vessel):
		""" Scores the vessel once, in its worst encounter
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			vessel -- Vessel under assessment
		"""
		worst	= None
		for situation in self.encounters( rule_ctxt, vessel ):
			result	= self.infer( ctxt, rule_ctxt, situation )
			if (result is not None) and ((worst is None) or (result[1]['any'] > worst[1]['any'])):
				worst	= result + ( situation.ts, )

		if worst is None:
			return

		evidence, hazards, target	= worst

		# Rl is read from the engine, so restore the worst encounter's posterior
		self.engine.setEvidence( evidence )
		self.engine.makeInference()

		# Rl is indexed by where the vessel is as well as by what may happen to
		# it, so the spatial zone is resolved before the loss row is taken.
		shapes		= self.survey( vessel )[0]
		zone		= self.spatial.classify( shapes )
		concerns	= self.matrix.row( self.engine, zone )
		serialized	= self.matrix.matlab( self.engine, self.spatial.order )
		cost		= sum( concerns.values() )
		ir			= individual_risk( self.engine )		# same inference pass as cost (REQ-020-02)

		# Keyed on the guid, which is unique by construction; the IMO is
		# recorded beside it rather than keyed on (COS-029-02).
		key			= Ledger.identify( vessel )
		imo			= Ledger.imo( vessel )
		track		= self.track( key )
		increment	= track.charge( cost, hazards['any'], evidence )

		report		= {
			'vessel'		: key,
			'recid'			: Ledger.recid( vessel ),	# database id written to every fact row
			'imo'			: imo,
			'time'			: ctxt.sim.now(),
			'zone'			: zone,			# spatial zone, the i index of Rl
			'matrix'		: serialized,	# the whole of Rl, MATLAB literal, USD
			'hazards'		: hazards,		# marginals, plus 'any' (exact) and 'sum' (eq. 14)
			'individual_risk'	: ir,		# P(harm_to_humans = fatality), IR [K, eq. (4)]
			'exposure'		: concerns,		# Rl row: concern -> expected economic loss
			'cost'			: cost,			# instantaneous expected loss
			'increment'		: increment,	# what was actually added to the voyage total
			'survival'		: track.survival,
			'cumulative'	: track.cost,
			'evidence'		: evidence,
			'target'		: Ledger.identify( target ) if target is not None else None,
		}

		self.publish( ctxt, vessel, report )
		self.record( ctxt, report )
		return

	def observe(self, ctxt:Context, rule_ctxt:RuleContext, situation):
		""" Resolves each bound simulation term into a BN evidence state
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			situation -- Own ship, and target if any; terms resolve against it alone
		Returns
			A dictionary of BN node name -> state label
		"""
		evidence	= None

		rule_ctxt.situation	= situation
		self.reset_resolver( ctxt, rule_ctxt )

		for k,v in self.bindings.items():
			if self.resolvable(k, rule_ctxt) == False:
				continue

			for binding in v:
				value	= rule_ctxt.resolve( binding['term'] )
				if value is None:
					continue			# Unobserved: the node keeps its prior

				state	= binding.discretize( value )
				if (state is not None) and (state not in self.labels( binding['node'] )):
					self.reject( ctxt, binding, state )
					continue

				if state is not None:
					if evidence is None:
						evidence	= {}
						
					evidence[ binding['node'] ]	= state

		return evidence


	def labels(self, node):
		""" The states of a network node, cached
		Arguments
			node -- Node name
		"""
		if node not in self.states:
			self.states[node]	= set( self.bn.variable(node).labels() )

		return self.states[node]

	def reject(self, ctxt:Context, binding, state):
		""" Logs, once per node and state, an observation the node has no state for
		Arguments
			ctxt -- Simulation context
			binding -- Binding that produced it
			state -- Offending state label
		"""
		key	= ( binding['node'], state )
		if key not in self.rejected:
			self.rejected.add( key )
			ctxt.log.error( self.id, f'{binding["term"]} gave state {state!r}, which node '
									 f'{binding["node"]} does not have; left unobserved' )
		return

	def track(self, key):
		""" Returns the voyage track for a vessel, creating it if needed
		Arguments
			key -- Vessel guid (COS-029-02)
		"""
		if key not in self.tracks:
			self.tracks[key]	= VoyageTrack()

		return self.tracks[key]

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
			report['recid'],
			report['zone'],
			hazards['collision'],
			hazards['grounding'],
			hazards['loss_of_comms'],
			hazards['any'],
			hazards['sum'],
			report['individual_risk'],
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
			report['recid'],
			report['matrix'],
		) )

		# Rb long form: one row per concern, zeros included (REQ.018)
		for concern, exposure in report['exposure'].items():
			self.data( ctxt, 'rb', (
				report['time'],
				report['recid'],
				report['zone'],
				concern,
				exposure,
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

		names	= set( self.bn.names() ) if self.bn is not None else None
		for k in self.bindings.keys():
			bindings	= [ Binding(b) for b in risk.get(k, []) ]
			if names is not None:
				for b in bindings:
					if b.get('node') not in names:
						ctxt.log.error( self.id, f'Binding {k}: node {b.get("node")!r} is not in the network; dropped (COS.006)' )
				bindings	= [ b for b in bindings if b.get('node') in names ]
			self.bindings[k]	= bindings

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
		self.weights	= ConcernWeights( risk )

		for problem in self.spatial.errors() + self.matrix.errors( self.bn ):
			ctxt.log.error( self.id, f'Rl: {problem}' )

		problems	= self.weights.errors()
		for problem in problems:
			ctxt.log.error( self.id, f'Rw: {problem} in {file}' )

		vocabulary	= set( getattr(getattr(self, 'rules', None), 'vocabulary', []) or [] )
		if vocabulary and (set(self.matrix.concerns) != vocabulary):
			problem	= f'concerns {sorted(self.matrix.concerns)} differ from the Ro vocabulary {sorted(vocabulary)} (REQ-018-04)'
			ctxt.log.error( self.id, f'Rb: {problem} in {file}' )
			problems.append( problem )

		if problems:
			raise ValueError( f'{self.id}: {file}: {"; ".join(problems)}' )

		ctxt.log.info( self.id, f'Rw: {self.weights.normalised()}' )

		# Rl is stored as a bare matrix literal with no axis labels in the row,
		# so the order that produced it is recorded here. Without this line a
		# stored matrix cannot be decoded after the fact.
		ctxt.log.info( self.id,
					   f'Rl axes [{CURRENCY}]: {self.matrix.axis_labels(self.spatial.order)}' )

		return
