#!/usr/bin/python
# Filename: LaneDisciplineExaminer.py
# Description: Implementation of the LaneDisciplineExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from maritime.model.zone.ZoneAwareness import ZoneAware
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

# REQUIREMENT:
# Lane discipline: overtaking where the zone forbids it.
#
# Two things must both hold. 
# (a) The zone must bar overtaking - 'overtaking: false'
#     in config/examiner/zones.yaml, eg: which the Istanbul Strait reach between
#     Vanikoy and Kanlica does - and the own ship must actually be overtaking.
#
# (b) The second is read from the COLREG resolver's own situation classification
#     rather than re-derived from bearings here, so that this examiner and COLREG
#     rule 13 can never disagree about what counts as overtaking.



class LaneDisciplineExaminer(ZoneAware, NavigationExaminer):
	TOPIC		= '/Faculty/Concern/Lane'
	MESSAGE		= 'vessel.lane'
	EVENT		= 'lane.overtaking_prohibited'

	OVERTAKING	= ('overtaking', 'overtake', 'overtaking_to_port', 'overtaking_to_starboard')

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
		self.init_zones( ctxt, config, requires=['os', 'ts'] )
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

		if self.permitted( rules ):
			return

		if self.overtaking( rule_ctxt ) == False:
			return

		self.score( ctxt, rule_ctxt, vessel, shapes )
		return

	def score(self, ctxt:Context, rule_ctxt, vessel, shapes):
		""" Scores an overtaking manoeuvre in a zone that bars it
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			vessel -- Own ship
			shapes -- Map shapes enclosing the vessel
		"""
		zone	= self.zone_name( shapes )
		penalty	= self.violate( ctxt, vessel, self.EVENT, zone,
								detail='overtaking where the zone bars it' )

		self.announce( ctxt, self.TOPIC, self.MESSAGE, {
			'vessel'	: self.identify( vessel ),
			'target'	: self.identify( rule_ctxt.situation.ts ),
			'time'		: ctxt.sim.now(),
			'zone'		: zone,
			'event'		: self.EVENT,
			'penalty'	: penalty,
		} )

		return penalty

	@staticmethod
	def permitted(rules)->bool:
		""" Whether the zone allows overtaking
		Arguments
			rules -- Merged zone rules
		Note
			Absent means permitted. A zone that says nothing about overtaking
			is not thereby forbidding it.
		"""
		allowed	= rules.get( 'overtaking', True )

		if isinstance( allowed, str ):
			return allowed.strip().lower() not in ('false', 'no', '0', 'prohibited')

		return bool( allowed )

	@classmethod
	def overtaking(cls, rule_ctxt)->bool:
		""" Whether the own ship is overtaking, per the COLREG classification
		Arguments
			rule_ctxt -- Rule context
		Note
			A classmethod rather than a staticmethod so that OVERTAKING is read
			off the class. A jurisdiction that classifies overtaking under a
			different name can then subclass and redeclare the tuple, and
			SpeedExaminer picks up the same reading.
		"""
		situation	= rule_ctxt.resolve( '(OwnShip,TargetShip).COLREG.Situation' )
		if situation is None:
			return False

		return str( situation ).strip().lower() in cls.OVERTAKING


if __name__ == "__main__":
	test = LaneDisciplineExaminer()
