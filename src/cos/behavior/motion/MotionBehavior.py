#!/usr/bin/python
# Filename: MotionBehavior.py
# Description: Base class for all motion behavior

from cos.model.environment.Types import DynamicForce
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

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
		return False

	def runnable(self, ctxt:Context, config):
		""" Checks if the object is runnable
		Arguments
			ctxt -- Simulation context
			config -- Config information
		"""
		syscfg	= config[0]
		instcfg	= ArgList(config[1]['settings'])

		if self.__match_scanario(instcfg, syscfg) == False:
			return False
		
		return True


	def __match_scanario(self, instcfg, syscfg):
		scenarios	= instcfg['scenario']

		# If a scenario is not specified, default to activate 
		# the instance
		if scenarios is None:
			return True
		
		# If scenarios are specified, then explicitly match
		# scenarios
		scenarios	= scenarios.split(',')
		match		= syscfg['scenario']
		for s in scenarios:
			if match.find(s) != -1:
				return True
			
		return False

if __name__ == "__main__":
	test = MotionBehavior()


