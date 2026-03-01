#!/usr/bin/python
# Filename: PredatorBehavior.py
# Description: Implementation of the PredatorBehavior class

from cos.behavior.motion.FleetBehavior import FleetBehavior
from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.core.kernel.Configuration import Configuration
from cos.math.geometry.Distance import Distance
from io import StringIO
from math import cos,sin,atan2
import numpy as np
import csv

class PredatorBehavior(FleetBehavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		FleetBehavior.__init__(self, ctxt, config)
		return

	def update(self, world, t, config, obstacles=None):
		""" Updates the behavior
		Arguments
			world -- World object
			t -- Current time step
			config -- Configuration attributes
			obstacles -- List of obstacles in the world (optional)
		"""
		prey = self.pick(world, t, config, obstacles)

		if prey is None:
			return self.random_walk(world, t, config, obstacles)
		else:
			return self.chase_prey(prey, world, t, config, obstacles)
	
	def pick(self, vessel, location, velocity, positions, world, t):
		""" Picks a prey for the predator
		Arguments
			vessel -- The predator vessel
			location -- Current location of the predator
			velocity -- Current velocity of the predator
			positions -- List of positions of all vessels in the fleet
			world -- World object
			t -- Current time step
		"""
		prey = None
		min_distance = float('inf')

		# Find the closest vessel to the predator
		for other_vessel, other_location, other_velocity in positions:
			if other_vessel == vessel:
				continue

			distance = Distance.euclidean(location, other_location)
			if distance < min_distance:
				min_distance = distance
				prey = (other_vessel, other_location, other_velocity)

		return prey
		

if __name__ == "__main__":
	test = PredatorBehavior()

