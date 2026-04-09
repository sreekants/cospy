#!/usr/bin/python
# Filename: StopOnTrafficBehavior.py
# Description: Implementation of the StopOnTrafficBehavior class

from cos.behavior.control.CollisionAvoidanceBehavior import CollisionAvoidanceBehavior
from cos.core.simulation.Behavior import Behavior, ActorBehavior

class StopOnTrafficBehavior(CollisionAvoidanceBehavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		CollisionAvoidanceBehavior.__init__(self, ctxt, config)
		self.range		= 10
		return

	def update(self, world, t, config):
		""" Updates the world by moving the vehicle
		Arguments
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
			config -- Configuration attributes
		"""

		vehicles = self.get_visible(world, config, self.range)
		if len(vehicles)>0:
			self.stop()
			# print("Stopping on traffic")
		else:
			self.resume()

		return None, None
	
if __name__ == "__main__":
	test = StopOnTrafficBehavior()

