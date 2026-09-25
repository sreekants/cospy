#!/usr/bin/python
# Filename: SpeedExaminer.py
# Description: Implementation of the SpeedExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from maritime.model.zone.ZoneAwareness import ZoneAware
from rules.examiner.navigation.LaneDisciplineExaminer import LaneDisciplineExaminer
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

# REQUIREMENT:
# Speed: exceeding a zone's limit, with a heavier penalty while overtaking.
#
# NOTE:
#   Overtaking is the aggravating circumstance the brief asks for: a vessel that
#   breaks the limit in order to get past another is scored under a separate
#   event, 'speed.limit_exceeded_overtaking', so the scorecard can price the two
#   differently without this examiner deciding by how much.
#
#   The overtaking test is delegated to LaneDisciplineExaminer so that both
#   examiners read the same COLREG classification. Note the asymmetry with lane
#   discipline: overtaking need not be prohibited here for the aggravation to
#   apply - speeding to overtake is worse even where overtaking is allowed.



class SpeedExaminer(ZoneAware, NavigationExaminer):
	TOPIC			= '/Faculty/Concern/Speed'
	MESSAGE			= 'vessel.speed'

	EXCEEDED		= 'speed.limit_exceeded'
	WHILE_OVERTAKING	= 'speed.limit_exceeded_overtaking'

	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)

		self.tolerance	= 0.0		# Knots of slack before a limit is 'exceeded'
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the examiner
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Only the own ship is required: a speed limit applies whether or not
		# another vessel is in scope. The overtaking aggravation needs a target
		# and is tested separately.
		self.init_zones( ctxt, config, requires=['os'] )

		tolerance		= config["tolerance"]
		self.tolerance	= float( tolerance ) if tolerance is not None else 0.0
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

		limit		= rules.get( 'speed_limit' )
		if limit is None:
			return			# The zone is unrestricted

		speed		= rule_ctxt.resolve( 'OwnShip.Velocity' )
		if speed is None:
			return

		limit		= float( limit )
		if float( speed ) <= (limit + self.tolerance):
			return

		self.score( ctxt, rule_ctxt, vessel, shapes, float(speed), limit )
		return

	def score(self, ctxt:Context, rule_ctxt, vessel, shapes, speed, limit):
		""" Scores a speed limit violation
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			vessel -- Own ship
			shapes -- Map shapes enclosing the vessel
			speed -- Observed speed
			limit -- Zone speed limit
		"""
		overtaking	= (rule_ctxt.situation.ts is not None) and \
					  LaneDisciplineExaminer.overtaking( rule_ctxt )

		event	= self.WHILE_OVERTAKING if overtaking else self.EXCEEDED
		zone	= self.zone_name( shapes )
		over	= speed - limit

		penalty	= self.violate( ctxt, vessel, event, shapes, value=over,
								detail=f'{speed:.1f} kn in a {limit:.1f} kn zone'
									   f'{" while overtaking" if overtaking else ""}' )

		self.announce( ctxt, self.TOPIC, self.MESSAGE, {
			'vessel'	: self.identify( vessel ),
			'time'		: ctxt.sim.now(),
			'zone'		: zone,
			'event'		: event,
			'speed'		: speed,
			'limit'		: limit,
			'over'		: over,
			'overtaking': overtaking,
			'penalty'	: penalty,
		} )

		return penalty


if __name__ == "__main__":
	test = SpeedExaminer()
