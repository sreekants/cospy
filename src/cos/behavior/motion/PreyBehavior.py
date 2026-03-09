#!/usr/bin/python
# Filename: PreyBehavior.py
# Description: Implementation of the PreyBehavior class

from cos.behavior.motion.FleetBehavior import FleetBehavior
from cos.behavior.motion.MotionBehavior import MotionBehavior
from cos.behavior.swarm.Prey import Prey, Config as PreyConfig
from cos.behavior.swarm.Predator import Predator, Config as PredatorConfig
from cos.behavior.swarm.Swarm import Swarm
from cos.math.geometry.Rectangle import Rectangle
from cos.math.geometry.Point import Point
from cos.math.geometry.Vector import Vector

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

	def intialize(self, ctxt, actor, vehicle, config:dict):
		""" Initialize the behavior for the actor
		Arguments
			actor -- Actor to initialize the behavior for
		"""
		FleetBehavior.intialize(self, ctxt, actor, vehicle, config)

		preycfg = PreyConfig()
		predcfg = PredatorConfig()

		preys = []
		predators = []

		for v in self.vessels:
			vessel	= v[0]
			type 	= v[1]

			pose		= vessel.config['pose']	
			position	= pose['position']
			X			= pose['X']
			pos		= Point(position[0], position[1])
			vel		= Vector(X[0], X[1])

			if type == 100000:
				preys.append(Prey(pos, vel))
			elif type == 200000:
				predators.append(Predator(pos, vel))	

		# Resolve the members to the swarm behavior
		self.swarm.setPreys(preycfg, preys )
		self.swarm.setPredators(predcfg, predators )
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
		#self.swarm.move(world)
		return None, None
		

if __name__ == "__main__":
	test = PreyBehavior()

