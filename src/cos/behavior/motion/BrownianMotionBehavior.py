#!/usr/bin/python
# Filename: BrownianMotionBehavior.py
# Description: Random walk motion behavior

from cos.behavior.motion.LinearMotionBehavior import LinearMotionBehavior
import random


class BrownianMotionBehavior(LinearMotionBehavior):
	# Default class behavior uses the linear vectors defined in the configuration to move the object
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		LinearMotionBehavior.__init__(self, ctxt, config)
		return

	def move(self, world, t, config):
		""" Moves the vehicle
		Arguments
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
			config -- Configuration attributes
		"""
		LinearMotionBehavior.move(self, world, t, config)

		# Introduce more entropy into the direction
		toss	= random.randrange(0,100)
		if self.entropy and toss<self.entropy:
			self.randomize_direction()

		return self.rect, self.dx



if __name__ == "__main__":
	test = BrownianMotionBehavior()


