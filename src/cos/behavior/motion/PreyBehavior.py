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
		return

	def update(self, world, t, config, obstacles=None):
		""" Updates the behavior
		Arguments
			world -- World object
			t -- Current time step
			config -- Configuration attributes
			obstacles -- List of obstacles in the world (optional)
		"""

		predators = self.scan(world, t, config, obstacles)

		if predators is None:
			return self.follow_herd(world, t, config, obstacles)
		else:
			return self.escape(predators, world, t, config, obstacles)

		

if __name__ == "__main__":
	test = PreyBehavior()

