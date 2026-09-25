#!/usr/bin/python
# Filename: ZoneAwareness.py
# Description: Shared machinery for examiners that judge a vessel against its zone

# A mixin rather than a base class: CargoExaminer descends from the
# environmental family and the rest from the navigation family, but all of them
# need the same four things - the zone rules, the map shapes under the vessel,
# the seabed beneath it, and one way to record a violation.
#
# Nothing here decides anything. Each examiner supplies the judgement; this
# supplies the footing so that the judgements stay comparable and every
# violation lands in the same fact table with the same shape.

from maritime.model.zone.ZoneRules import ZoneRules
from maritime.model.zone.Ledger import Ledger, FindingGuard, SOURCE_EXAMINER, seconds
from cos.model.examiner.Precondition import PreconditionSet
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList
from cos.model.rule.Situation import Situation

import queue

# Situation attributes an examiner may declare a dependency on.
SITUATION_ATTRIBUTES = ('os', 'ts', 'fleet', 'zone', 'eez', 'harbour',
						'lane', 'mez', 'tss')

# Encounter messages the conduct and situation faculties post (COS.023 L4)
ENCOUNTER_MESSAGES	= ('vessel.approach', 'vessel.overtaking', 'vessel.crossing')

# Where an examiner's situations come from (COS.023 L5)
ENCOUNTERS	= 'encounters'		# subscribed encounter messages
SUBJECTS	= 'subjects'		# each vessel under test, alone


class ZoneAware:
	""" Zone rules, map lookup and violation recording for a concern examiner.
	"""

	# Finding scope; overridable per class under 'findings' in zones.yaml
	FINDING		= {'scope': 'change'}
	SITUATIONS	= SUBJECTS

	def init_zones(self, ctxt:Context, config:ArgList, requires=None):
		""" Loads the zone rules and declares the examiner's preconditions
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
			requires -- Situation attributes this examiner needs
		"""
		self.ledger		= Ledger()
		self.ledger.load( ctxt, self.id, config["zones"], config["territory"] )
		self.rules		= self.ledger.rules
		self.guard		= self.finding_guard( self.rules )

		self.sea		= []
		self.land		= []
		# Named zone_gate, not gate: a mixin must not overwrite the gate of the
		# examiner it is mixed into (RiskExaminer declares its own per group).
		self.zone_gate	= PreconditionSet( {'vessel': list(requires or ['os'])} )

		self.situations	= queue.Queue()
		for message in ENCOUNTER_MESSAGES:
			self.subscribe( message, self.on_encounter )
		return

	def on_encounter(self, ctxt:Context, evt):
		""" Queues an encounter; ignored by examiners that iterate subjects
		Arguments
			ctxt -- Simulation context
			evt -- (kind, own ship, target or EncounterEvent, ...)
		"""
		if self.SITUATIONS != ENCOUNTERS:
			return

		own		= evt[1]
		target	= getattr( evt[2], 'TS', evt[2] )
		self.situations.put( Situation(own, target) )
		return

	def evaluate(self, ctxt:Context, rule_ctxt):
		""" Judges each situation in turn, restoring the shared one afterwards (COS.007)
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		saved	= rule_ctxt.situation
		try:
			for situation in self.pending( rule_ctxt ):
				rule_ctxt.situation	= situation
				self.reset_resolver( ctxt, rule_ctxt )
				self.judge( ctxt, rule_ctxt )
		finally:
			rule_ctxt.situation	= saved
			self.reset_resolver( ctxt, rule_ctxt )
		return

	def pending(self, rule_ctxt):
		""" This pass's situations: queued encounters, or each subject alone
		Arguments
			rule_ctxt -- Rule context
		"""
		queued	= []
		while not self.situations.empty():
			queued.append( self.situations.get() )

		if self.SITUATIONS == SUBJECTS:
			subjects	= getattr( rule_ctxt, 'subjects', None ) or rule_ctxt.vessels or []
			return [ Situation(vessel, None) for vessel in subjects ]

		unique	= {}
		for situation in queued:
			unique.setdefault( (situation.os.id, situation.ts.id), situation )
		return list( unique.values() )

	@staticmethod
	def reset_resolver(ctxt:Context, rule_ctxt):
		""" Points the resolver at the current situation
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		resolver	= getattr( rule_ctxt, 'resolver', None )
		if resolver is not None:
			resolver.reset( ctxt, rule_ctxt )
		return

	def judge(self, ctxt:Context, rule_ctxt):
		""" Judges rule_ctxt.situation; each examiner supplies this
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		return

	def finding_guard(self, rules:ZoneRules)->FindingGuard:
		""" The guard counting this examiner's findings
		Arguments
			rules -- Loaded zone rules
		"""
		findings	= rules.section( 'findings' )
		settings	= dict( findings.get('default', {}) or {} )
		settings.update( self.FINDING )
		settings.update( findings.get(self.__class__.__name__, {}) or {} )

		return FindingGuard( scope=settings.get('scope', 'change'),
							 release=settings.get('release', 10.0),
							 interval=settings.get('interval'),
							 dwell=settings.get('dwell', 0.0) )

	def cache_shapes(self, ctxt:Context):
		""" Caches the map shapes once the world has been built.

		Deliberately not named on_start: Examiner already defines that, and a
		mixin silently winning or losing an MRO race is the kind of bug that
		only shows up as an examiner that never fires. Each examiner calls this
		from its own on_start.
		Arguments
			ctxt -- Simulation context
		"""
		objmgr		= ctxt.sim.objects
		self.sea	= objmgr.get_all( "/World/Sea" )
		self.land	= objmgr.get_all( "/World/Land" )
		return

	def applicable(self, rule_ctxt)->bool:
		""" Checks this examiner's precondition against the current situation
		Arguments
			rule_ctxt -- Rule context
		"""
		return self.zone_gate.holds( 'vessel', rule_ctxt.situation )

	def survey(self, vessel):
		""" Everything the examiners need to know about where a vessel is
		Arguments
			vessel -- Vessel under examination
		Returns
			(shapes, rules, depth) - the map shapes enclosing the vessel, the
			merged zone rules, and the shallowest seabed beneath it
		"""
		position	= getattr( vessel, 'location', None )
		shapes		= ZoneRules.enclosing( self.sea, position )
		rules		= self.rules.rules_at( shapes )
		depth		= self.rules.seabed_depth( shapes )

		return shapes, rules, depth

	def zone_name(self, shapes)->str:
		""" A readable name for the innermost zone, for reporting
		Arguments
			shapes -- Map shapes enclosing the vessel
		"""
		return Ledger.area( shapes )

	def clearance(self, vessel, depth):
		""" Water left beneath the keel
		Arguments
			vessel -- Vessel under examination
			depth -- Seabed depth, or None when the map does not report one
		Returns
			Metres of clearance, or None when it cannot be computed
		"""
		if depth is None:
			return None

		draught		= getattr( vessel, 'draft', None )
		if draught is None:
			draught	= getattr( vessel, 'draught', None )
		if draught is None:
			draught	= getattr( getattr(vessel, 'model', None), 'draft', None )	# where OS.Draft reads it
		if draught is None:
			return None

		allowance	= getattr( vessel, 'underkeel_clearance', 0.0 ) or 0.0
		return float(depth) - float(draught) - float(allowance)

	def violate(self, ctxt:Context, vessel, event:str, shapes, value=0.0, detail=None, subject=None):
		""" Records a violation, once per occurrence, and returns the penalty scored
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel in violation
			event -- Violation identifier, keyed into the penalties scorecard
			shapes -- Map shapes enclosing the vessel
			value -- Quantity behind the violation, e.g. metres over or USD
			detail -- Optional free text for the log
			subject -- What the finding is about beyond vessel and event, e.g.
					   the target ship; defaults to the innermost area
		Returns
			The penalty, or 0.0 when the finding is already recorded
		"""
		key			= self.finding_key( vessel, event, shapes, subject )
		if self.guard.admit( key, seconds(ctxt.sim.now()) ) == False:
			return 0.0

		penalty		= self.rules.penalty( event )
		recorded	= self.ledger.record( ctxt, SOURCE_EXAMINER, self.__class__.__name__,
										  vessel, event, shapes, penalty, value )
		if recorded == False:
			return 0.0

		if detail is not None:
			ctxt.log.info( self.id, f'{event} [{self.zone_name(shapes)}] {detail}' )

		return penalty

	def settle(self, vessel, event:str, shapes, subject=None):
		""" Ends a finding the examiner has seen end
		Arguments
			vessel -- Vessel
			event -- Violation identifier
			shapes -- Map shapes enclosing the vessel
			subject -- As passed to violate()
		"""
		self.guard.clear( self.finding_key(vessel, event, shapes, subject) )
		return

	def finding_key(self, vessel, event:str, shapes, subject=None):
		""" What a finding is about, for the guard
		Arguments
			vessel -- Vessel
			event -- Violation identifier
			shapes -- Map shapes enclosing the vessel
			subject -- Explicit subject, else the innermost area
		"""
		if subject is None:
			subject	= self.zone_name( shapes )

		return ( self.identify(vessel), event, subject )

	def announce(self, ctxt:Context, topic:str, message:str, payload):
		""" Posts a message to one IPC topic or several
		Arguments
			ctxt -- Simulation context
			topic -- IPC topic, or a list of them
			message -- Message name
			payload -- Message body
		"""
		if topic is None:
			return

		for t in ([topic] if isinstance(topic, str) else topic):
			ctxt.ipc.push( t, message, ctxt, payload, 8 )
		return

	@staticmethod
	def identify(vessel):
		""" IMO of a vessel, or 0 when it declares none
		Arguments
			vessel -- Vessel
		"""
		return Ledger.identify( vessel )


if __name__ == "__main__":
	test = ZoneAware()
