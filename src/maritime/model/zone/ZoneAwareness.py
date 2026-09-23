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
from cos.model.examiner.Precondition import PreconditionSet
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

# Situation attributes an examiner may declare a dependency on.
SITUATION_ATTRIBUTES = ('os', 'ts', 'fleet', 'zone', 'eez', 'harbour',
						'lane', 'mez', 'tss')

FACT = 'Concern'


class ZoneAware:
	""" Zone rules, map lookup and violation recording for a concern examiner.
	"""

	def init_zones(self, ctxt:Context, config:ArgList, requires=None):
		""" Loads the zone rules and declares the examiner's preconditions
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
			requires -- Situation attributes this examiner needs
		"""
		self.rules		= ZoneRules()
		self.rules.load( ctxt, config["zones"] or '$(CONFIG)/examiner/zones.yaml' )

		self.sea		= []
		self.land		= []
		self.gate		= PreconditionSet( {'vessel': list(requires or ['os'])} )
		return

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
		return self.gate.holds( 'vessel', rule_ctxt.situation )

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
		for shape in reversed( shapes ):
			name	= getattr( shape, 'name', None )
			if name:
				return name

		return 'open water'

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
			return None

		allowance	= getattr( vessel, 'underkeel_clearance', 0.0 ) or 0.0
		return float(depth) - float(draught) - float(allowance)

	def violate(self, ctxt:Context, vessel, event:str, zone:str, value=0.0, detail=None):
		""" Records a violation and returns the penalty scored
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel in violation
			event -- Violation identifier, keyed into the penalties scorecard
			zone -- Name of the zone the violation happened in
			value -- Quantity behind the violation, e.g. metres over or USD
			detail -- Optional free text for the log
		"""
		penalty		= self.rules.penalty( event )

		ctxt.sim.data.push( f'fact_{FACT}', (
			ctxt.sim.case_id,
			ctxt.sim.now(),
			self.identify( vessel ),
			self.__class__.__name__,
			event,
			zone,
			penalty,
			float( value ),
		) )

		if detail is not None:
			ctxt.log.info( self.id, f'{event} [{zone}] {detail}' )

		return penalty

	def announce(self, ctxt:Context, topic:str, message:str, payload):
		""" Posts a message to an IPC topic
		Arguments
			ctxt -- Simulation context
			topic -- IPC topic
			message -- Message name
			payload -- Message body
		"""
		if topic is None:
			return

		ctxt.ipc.push( topic, message, ctxt, payload, 8 )
		return

	@staticmethod
	def identify(vessel):
		""" IMO of a vessel, or 0 when it declares none
		Arguments
			vessel -- Vessel
		"""
		try:
			return vessel.config["identifier"]["imo"]
		except (KeyError, TypeError):
			return 0


if __name__ == "__main__":
	test = ZoneAware()
