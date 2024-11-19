#!/usr/bin/python
# Filename: MotionBehavior.py
# Description: Base class for all motion behavior

from cos.core.utilities.ArgList import ArgList
from cos.model.environment.Types import DynamicForce

import numpy as np


class MotionBehavior:
	def __init__(self):
		""" Constructor
		"""
		null_vector		= np.zeros(3)
		self.x			= null_vector
		self.dx			= null_vector
		self.d2x		= null_vector

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
		return self.move(world, t, config)

	def ioctl(self, op, arg):
		""" Handles operation signals
		Arguments
			op -- Operation code
			arg -- arguments for the operation
		"""
		return

if __name__ == "__main__":
	test = MotionBehavior()


