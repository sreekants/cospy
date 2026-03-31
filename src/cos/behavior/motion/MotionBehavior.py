#!/usr/bin/python
# Filename: MotionBehavior.py
# Description: Base class for all motion behavior

from cos.model.environment.Types import DynamicForce
from cos.core.simulation.Behavior import Behavior, ActorBehavior
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

import numpy as np


class MotionBehavior(Behavior):
	def __init__(self):
		""" Constructor
		"""
		Behavior.__init__(self, ActorBehavior.MOTION)
		
		null_vector		= np.zeros(3)
		self.x			= null_vector
		self.dx			= null_vector
		self.d2x		= null_vector
		
		self.movable	= True

		self.forces	= {
			DynamicForce.WIND_CURRENT : null_vector,
			DynamicForce.SEA_CURRENT : null_vector,
			DynamicForce.SEA_WAVE : null_vector
		}
		return

	def init(self, currpos):
		""" Initializes the behavior
		Arguments
			currpos -- Start position of the vehicle
		"""
		self.rect	= currpos
		self.last	= currpos
		return

	def get_settings(self, config):
		""" Extracts a setting from the configuration
		Arguments
			config -- Configuration attributes
		"""
		return ArgList( config.get("settings", None) )

	@property
	def force(self):
		""" Returns the forces acting on the vehicle
		"""
		return self.forces

	def update(self, world, t, config):
		""" Updates the world by moving the vehicle
		Arguments
			world -- Reference ot the simulation world
			t -- Time on the simulation clock
			config -- Configuration attributes
		"""
		if self.movable == False:
			distance = np.linalg.norm(self.dx)*1000.0
			orientation = self.dx / distance if distance > 0 else np.zeros(3)
			return self.rect, orientation
		
		return self.move(world, t, config)

	def ioctl(self, op, arg):
		""" Handles operation signals
		Arguments
			op -- Operation code
			arg -- arguments for the operation
		"""
		return False

	def runnable(self, ctxt:Context, config):
		""" Checks if the object is runnable
		Arguments
			ctxt -- Simulation context
			config -- Config information
		"""		
		return True



if __name__ == "__main__":
	test = MotionBehavior()


