#!/usr/bin/python
# Filename: NightTimeExaminer.py
# Description: Implementation of the NightTimeExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from maritime.model.zone.ZoneAwareness import ZoneAware
from cos.model.examiner.Examination import ExaminationType
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList
from cos.model.vehicle.Signal import Signal
from maritime.model.vessel.Vessel import Vessel

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
#   A required light is a name or wildcard pattern from the signal vocabulary
#   (REQ.036), e.g. 'Light.Masthead.*'. It counts as shown when the vessel's
#   signal set matches it (Vehicle.is_signaled). A vessel with no signal set is
#   reported as unlit.



class NightTimeExaminer(ZoneAware, NavigationExaminer):
	EXAMINES	= ExaminationType.NIGHT_TIME
	TOPIC		= '/Faculty/Concern/NightTime'
	MESSAGE		= 'vessel.lights'
	EVENT		= 'night.lights_missing'

	# Once per vessel per night: the night is the finding's subject
	FINDING		= {'scope': 'episode'}

	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the examiner
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.init_zones( ctxt, config, requires=['os'] )
		Vessel.load_signals( ctxt )
		self.check_lights()
		return

	def check_lights(self):
		""" Checks every required light in the zone rules against the signal vocabulary
		Raises
			ValueError naming the zones file and the entry when a light is not in the vocabulary
		"""
		vocabulary	= Signal.vocabulary
		if vocabulary is None:
			return

		layers	= [ ('default', self.rules.defaults) ]
		layers	+= [ (f'types.{name}', rules or {}) for name, rules in self.rules.types.items() ]
		layers	+= [ (f'named.{name}', rules or {}) for name, rules in self.rules.zones.items() ]

		for where, rules in layers:
			for light in NightTimeExaminer.lights( rules.get('required_lights') ):
				vocabulary.check( light, f'{self.rules.source}: zones.{where}.required_lights' )
		return

	@staticmethod
	def lights(required):
		""" The required lights as a list
		Arguments
			required -- A list, or a comma-separated string as a shape's settings give it
		"""
		if isinstance( required, str ):
			return [ l.strip() for l in required.split(',') if l.strip() ]
		return list( required or [] )

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.cache_shapes( ctxt )
		return

	def judge(self, ctxt:Context, rule_ctxt):
		""" Judges rule_ctxt.situation
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		if self.applicable( rule_ctxt ) == False:
			return

		vessel		= rule_ctxt.situation.os
		shapes, rules, _depth	= self.survey( vessel )

		if self.is_night( ctxt, rules ) == False:
			return

		required	= NightTimeExaminer.lights( rules.get('required_lights') )

		if len( required ) == 0:
			return

		missing		= self.missing( vessel, required )
		if len( missing ) == 0:
			return

		self.score( ctxt, vessel, shapes, rules, required, missing )
		return

	def score(self, ctxt:Context, vessel, shapes, rules, required, missing):
		""" Scores a vessel showing fewer lights than the zone requires
		Arguments
			ctxt -- Simulation context
			vessel -- Own ship
			shapes -- Map shapes enclosing the vessel
			rules -- Merged zone rules
			required -- Lights the zone requires
			missing -- Lights not being shown
		"""
		imo		= self.identify( vessel )

		zone	= self.zone_name( shapes )
		penalty	= self.violate( ctxt, vessel, self.EVENT, shapes, value=len(missing),
								detail=f'not showing {", ".join(missing)}',
								subject=self.night( ctxt, rules ) )
		if not penalty:
			return 0.0

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

	def night(self, ctxt:Context, rules):
		""" Which night it is: the date the current night began
		Arguments
			ctxt -- Simulation context
			rules -- Merged zone rules
		"""
		now		= ctxt.sim.localtime()
		end		= int( rules.get('night_to', 6) )
		hour	= self.hour( ctxt )

		if isinstance( now, datetime.datetime ):
			day	= now.date()
			if (hour is not None) and (hour < end):
				day	= day - datetime.timedelta( days=1 )
			return day.isoformat()

		try:
			day	= int( float(now) // 86400 )
		except (TypeError, ValueError):
			return None

		if (hour is not None) and (hour < end):
			day	-= 1
		return day

	@staticmethod
	def hour(ctxt:Context):
		""" Local hour of the simulation clock
		Arguments
			ctxt -- Simulation context
		"""
		now	= ctxt.sim.localtime()
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
		signaled	= getattr( vessel, 'is_signaled', None )
		if signaled is None:
			return list( required )

		return [ light for light in required if signaled(light) == False ]


if __name__ == "__main__":
	test = NightTimeExaminer()
