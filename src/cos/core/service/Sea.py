#!/usr/bin/python
# Source File: Sea.py
# Description: Web service implementation.

from cos.core.service.WorldObject import WorldObject
from cos.core.simulation.Simulation import Simulation

class Sea(WorldObject):
	def __init__(self):
		""" Constructor
		"""
		WorldObject.__init__(self, 'Sea')
		self.world	= Simulation.instance().objects.get('/Services/Kernel/World')
		return

	def describe( self, type ):
		""" Describes the regions of the sea
		Arguments
			type -- Type of the object
		"""
		return self.world.describe( type )



