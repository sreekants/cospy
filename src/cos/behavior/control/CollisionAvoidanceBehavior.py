#!/usr/bin/python
# Filename: CollisionAvoidanceBehavior.py
# Description: Implementation of the CollisionAvoidanceBehavior class

from cos.core.simulation.Behavior import Behavior, ActorBehavior
from cos.core.kernel.Configuration import Configuration
from cos.math.geometry.Distance import Distance
from io import StringIO
from math import cos,sin,atan2
import numpy as np
import csv

class CollisionAvoidanceBehavior(Behavior):
	def __init__(self, ctxt, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Behavior.__init__(self, ActorBehavior.CONTROL_COLAV)
		self.motion		= None
		return

	def intialize(self, ctxt, actor, vehicle, config:dict):
		""" Initialize the behavior for the actor
		Arguments
			ctxt -- Simulation context
			actor -- Actor to initialize the behavior for
			vehicle -- Vehicle object to create the actor for
			config -- Configuration attributes
		"""
		Behavior.intialize(self, ctxt, actor, vehicle, config)
		
		self.motion		= actor.behaviors.get(ActorBehavior.MOTION, None)
		self.vehicle	= vehicle
		return

	def stop(self):
		""" Stops the behavior
		"""
		self.motion.movable	= False
		return

	def resume(self):
		""" Resumes the behavior
		"""
		self.motion.movable	= True
		return

	
	def get_visible_in_range(self, world, config, range):
		""" Gets the list of visible vehicles
		Arguments
			world -- Reference ot the simulation world
			config -- Configuration attributes
		"""
		# Get a list of all the vehicles in the world within range
		vehicles	= []
		
		for v in world.sim.objects.get_all('/World/Vehicle/Vessel'):
			if v is self.vehicle:
				continue

			if Distance.euclidean_squared(v.location, self.vehicle.location) > range:
				continue

			vehicles.append( v )
		
		return vehicles

		

if __name__ == "__main__":
	test = CollisionAvoidanceBehavior()

