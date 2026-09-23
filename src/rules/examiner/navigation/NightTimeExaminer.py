#!/usr/bin/python
# Filename: NightTimeExaminer.py
# Description: Implementation of the NightTimeExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from maritime.model.zone.ZoneAwareness import ZoneAware
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

import datetime

# REQUIREMENT:
# Night time: between sunset and sunrise a vessel must show the lights her type
# and state require. This examiner checks that the required lights are posted,
# and scores the ones that are missing.
#
# NOTE:
#   Which lights are required is configuration, not code - 'required_lights' per
#   zone in config/examiner/zones.yaml - because the set differs by vessel type
#   and by jurisdiction, and because COLREG part C is exactly the sort of list a
#   scenario designer needs to vary.
#
#   The lights a vessel is actually showing are read from its operation ValueSet,
#   the same property set the bridge model raises signals into. A vessel with no
#   operation set at all is reported once as unlit rather than passed, since an
#   absent set and a dark ship are indistinguishable here.



class NightTimeExaminer(ZoneAware, NavigationExaminer):
	TOPIC		= '/Faculty/Concern/NightTime'
	MESSAGE		= 'vessel.lights'
	EVENT		= 'night.lights_missing'

	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)

		self.reported	= set()		# Vessel IMOs already reported this night
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the examiner
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.init_zones( ctxt, config, requires=['os'] )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.cache_shapes( ctxt )
		return

	def evaluate(self, ctxt:Context, rule_ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if self.applicable( rule_ctxt ) == False:
			return

		vessel		= rule_ctxt.situation.os
		shapes, rules, _depth	= self.survey( vessel )

		if self.is_night( ctxt, rules ) == False:
			self.reported.clear()		# A new day; report each vessel afresh
			return

		required	= rules.get( 'required_lights' ) or []
		if isinstance( required, str ):
			required	= [ l.strip() for l in required.split(',') if l.strip() ]

		if len( required ) == 0:
			return

		missing		= self.missing( vessel, required )
		if len( missing ) == 0:
			return

		self.score( ctxt, vessel, shapes, required, missing )
		return

	def score(self, ctxt:Context, vessel, shapes, required, missing):
		""" Scores a vessel showing fewer lights than the zone requires
		Arguments
			ctxt -- Simulation context
			vessel -- Own ship
			shapes -- Map shapes enclosing the vessel
			required -- Lights the zone requires
			missing -- Lights not being shown
		"""
		imo		= self.identify( vessel )

		# Once per vessel per night: an unlit ship is one finding, not one
		# finding per tick for as long as it stays dark.
		if imo in self.reported:
			return 0.0

		self.reported.add( imo )

		zone	= self.zone_name( shapes )
		penalty	= self.violate( ctxt, vessel, self.EVENT, zone, value=len(missing),
								detail=f'not showing {", ".join(missing)}' )

		self.announce( ctxt, self.TOPIC, self.MESSAGE, {
			'vessel'	: imo,
			'time'		: ctxt.sim.now(),
			'zone'		: zone,
			'event'		: self.EVENT,
			'required'	: list( required ),
			'missing'	: missing,
			'penalty'	: penalty,
		} )

		return penalty

	def is_night(self, ctxt:Context, rules)->bool:
		""" Whether the simulation clock reads night
		Arguments
			ctxt -- Simulation context
			rules -- Merged zone rules
		Note
			night_from > night_to, so the window wraps midnight and the test is
			a disjunction rather than a range.
		"""
		hour	= self.hour( ctxt )
		if hour is None:
			return False

		start	= int( rules.get('night_from', 20) )
		end		= int( rules.get('night_to', 6) )

		if start == end:
			return False

		if start > end:
			return (hour >= start) or (hour < end)

		return start <= hour < end

	@staticmethod
	def hour(ctxt:Context):
		""" Local hour of the simulation clock
		Arguments
			ctxt -- Simulation context
		"""
		now	= ctxt.sim.now()
		if now is None:
			return None

		if isinstance( now, datetime.datetime ):
			return now.hour

		try:
			return int( (float(now) // 3600) % 24 )
		except (TypeError, ValueError):
			return None

	@staticmethod
	def missing(vessel, required):
		""" Required lights a vessel is not showing
		Arguments
			vessel -- Vessel
			required -- Lights the zone requires
		"""
		showing	= getattr( vessel, 'operation', None )
		if showing is None:
			return list( required )

		return [ light for light in required if showing.has(light) == False ]


if __name__ == "__main__":
	test = NightTimeExaminer()
