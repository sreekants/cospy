#!/usr/bin/python
# Filename: PreyBehavior.py
# Description: Implementation of the PreyBehavior class

from cos.behavior.motion.FleetBehavior import FleetBehavior
from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.behavior.swarm.Prey import Prey
from cos.behavior.swarm.Predator import Predator
from cos.behavior.swarm.Swarm import Swarm

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

		self.swarm	= Swarm()
		return


	def append_member(self, ctxt, vessel, type):
		""" Appends a member to the fleet
		Arguments
			ctxt -- Simulation context
			vessel -- Vessel object to append
			type -- Type of the vessel (e.g., "leader", "follower")
		"""

		FleetBehavior.append_member(self, ctxt, vessel, type)

		if type == 100000:	
			self.preys.append(vessel)
		elif type == 200000:	
			self.predators.append(vessel)
		return


	def update(self, world, t, config, obstacles=None):
		""" Updates the behavior
		Arguments
			world -- World object
			t -- Current time step
			config -- Configuration attributes
			obstacles -- List of obstacles in the world (optional)
		"""

		if not self.predators:
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

