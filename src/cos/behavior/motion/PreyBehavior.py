#!/usr/bin/python
# Filename: PreyBehavior.py
# Description: Implementation of the PreyBehavior class

from cos.behavior.motion.FleetBehavior import FleetBehavior
from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.behavior.swarm.Prey import Prey, Config as PreyConfig
from cos.behavior.swarm.Predator import Predator, Config as PredatorConfig
from cos.behavior.swarm.Swarm import Swarm

from cos.core.kernel.Configuration import Configuration
from cos.math.geometry.Distance import Distance
from io import StringIO
from math import cos,sin,atan2
import numpy as np
import csv

from tests.cos.behavior import swarm

class PreyBehavior(FleetBehavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		FleetBehavior.__init__(self, ctxt, config)

		self.swarm			= Swarm()
		self.preys			= []
		self.predators		= [] 
		return

	def load(self, ctxt, filename):
		""" Loads the behavior
		Arguments
			ctxt -- Simulation context
			filename -- File name
		"""
		FleetBehavior.load(self, ctxt, filename)


		preycfg = PreyConfig()
		predcfg = PredatorConfig()

		ctxt.sim
		preyList = self.swarm.setPreys(preycfg, [Prey.create(preycfg.speed, screen_vec) for _ in range(preycfg.count)])
		predList = self.swarm.setPredators(predcfg, [Predator.create(predcfg.speed, screen_vec) for _ in range(predcfg.count)])

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

		# Update the swarm behavior
		self.swarm.move(world)
		return
		

if __name__ == "__main__":
	test = PreyBehavior()

