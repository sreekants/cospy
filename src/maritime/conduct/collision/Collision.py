#!/usr/bin/python
# Filename: Collision.py
# Description: Implementation of the Collision class

from maritime.core.situation.MaritimeConductSituation import MaritimeConductSituation
from cos.core.kernel.Context import Context
from cos.model.rule.Situation import Situation as RuleSituation
from cos.model.rule.Context import Context as RuleContext
from maritime.core.situation.Types import Encounter as EncounterType

class Collision(MaritimeConductSituation):
	def __init__(self):
		""" Constructor
		Arguments
			"""
		MaritimeConductSituation.__init__( self )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.setup(ctxt, config)

		self.lpa		= {}		# Map of last-known point of approach
		return

	def evaluate(self, ctxt:Context, rule_ctxt:RuleContext):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		self.for_each_in_range( ctxt, rule_ctxt,
				self.range_of_interest,
				rule_ctxt.vessels,
				rule_ctxt.vessels,
				self.on_collide_vessel )

		self.for_each_in_range( ctxt, rule_ctxt,
				self.collision_range,
				rule_ctxt.vessels,
				rule_ctxt.bodies,
				self.on_collide_obstacle )

		return

	def setup(self, ctxt:Context, config):
		""" Sets up the parameters of the situations
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Overridable implementation
		self.range_of_interest	= 10		# Range of interest
		self.tracking_range		= 5			# Range at approach (must be greater than collision range)
		self.collision_range	= 1			# Range at collision
		return

	def on_collide_vessel(self, ctxt:Context, rule_ctxt:RuleContext, info, arg ):
		""" Event handler to evaluate vessel collision
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			info -- String of name-value pair attributes
			arg -- Opaque argument passed to the callback
		"""
		lhs			= info[0]
		rhs			= info[1]
		distance	= info[2]



		if distance < self.collision_range:
			return

		# If the vessel is outside the tracking range, we are no longer tracking it
		if distance > self.tracking_range:
			self.set_lpa(lhs, rhs, None)
			return

		lpa			= self.get_lpa(lhs, rhs)
		if (lpa is None) or (distance < lpa):
			self.set_lpa(lhs, rhs, distance)
		elif distance > lpa:
			# Last point of approach was the closest point of approach (CPA) in the simulation
			print( f'CPA {lhs.config["name"]} and {rhs.config["name"]} at distance {lpa}')
			self.regulate( ctxt, lhs, "vessel.approach", (EncounterType.CPA, lhs, rhs, lpa) )
			self.set_lpa(lhs, rhs, distance)


		if distance > self.collision_range:
			return

		# print( f'COLLISION! {lhs.config["name"]} and {rhs.config["name"]} at distance {info[2]:0.2}')
		return

	def on_collide_obstacle(self, ctxt:Context, rule_ctxt:RuleContext, info, arg ):
		""" Event handler to evaluate obstacle collision
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
			info -- String of name-value pair attributes
			arg -- Opaque argument passed to the callback
		"""
		lhs		= info[0]
		rhs		= info[1]

		# print( f'COLLISION! {lhs.config["name"]} and {rhs.config["name"]} at distance {info[2]:0.2}')
		return

	def get_lpa(self, lhs, rhs):
		""" TODO: get_lpa
		Arguments
			lhs -- TODO
			rhs -- TODO
		""" 
		return self.lpa.get( (lhs.vid, rhs.vid), None )

	def set_lpa(self, lhs, rhs, distance):
		""" TODO: set_lpa
		Arguments
			lhs -- TODO
			rhs -- TODO
			distance -- TODO
		""" 
		self.lpa[(lhs.vid, rhs.vid)]	= distance
		return

if __name__ == "__main__":
	test = Collision("XXX")


