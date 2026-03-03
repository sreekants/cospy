#!/usr/bin/python
# Filename: PreyBehavior.py
# Description: Implementation of the PreyBehavior class

from cos.behavior.motion.FleetBehavior import FleetBehavior
from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.core.kernel.Configuration import Configuration
from cos.math.geometry.Distance import Distance
from io import StringIO
from math import cos,sin,atan2
import numpy as np
import csv

class PreyBehavior(FleetBehavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		FleetBehavior.__init__(self, ctxt, config)
		self.predators = None	# List of predator objects in the world
		return


	def intialize(self, ctxt, actor, vehicle, config:dict):
		""" Initialize the behavior for the actor
		Arguments
			actor -- Actor to initialize the behavior for
		"""
		FleetBehavior.intialize(self, ctxt, actor, vehicle, config)

		# TODO: Resolve all predators in the world and store them for later use
		return

	def update(self, world, t, config, obstacles=None):
		""" Updates the behavior
		Arguments
			world -- World object
			t -- Current time step
			config -- Configuration attributes
			obstacles -- List of obstacles in the world (optional)
		"""

		if self.predators is None:
			return self.follow_herd(world, t, config, obstacles)
		else:
			return self.escape(self.predators, world, t, config, obstacles)

	def follow_herd(self, world, t, config, obstacles=None):
		""" Follows the herd behavior
		Arguments
			world -- World object
			t -- Current time step
			config -- Configuration attributes
			obstacles -- List of obstacles in the world (optional)
		"""
		return	
	
	def escape(self, predators, world, t, config, obstacles=None):
		""" Escapes from predators
		Arguments
			predators -- List of predator objects in the world
			world -- World object
			t -- Current time step
			config -- Configuration attributes
			obstacles -- List of obstacles in the world (optional)
		"""
		return
		

if __name__ == "__main__":
	test = PreyBehavior()

