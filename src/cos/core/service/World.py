#!/usr/bin/python
# Source File: World.py
# Description: Web service implementation.

from cos.core.network.ORPCService import ORPCService
from cos.core.simulation.Simulation import Simulation

class World(ORPCService):
	def __init__(self):
		""" Constructor
		"""
		ORPCService.__init__(self)
		self.world	= Simulation.instance().objects.get('/Services/Kernel/World')
		return

	def init( self, bodies ):
		""" #TODO: init
		Arguments
			bodies -- #TODO
		"""
		self.world.init(bodies)
		return

	def has_collision( self, shape ):
		""" #TODO: has_collision
		Arguments
			shape -- #TODO
		"""
		return self.world.has_collision(shape)

	def add( self, type, obj ):
		""" #TODO: add
		Arguments
			type -- Type of the object
			obj -- #TODO
		"""
		self.world.add(type, obj)
		return

	def play(self):
		""" #TODO: play
		"""
		return self.world.play()

	def describe( self, type ):
		""" #TODO: describe
		Arguments
			type -- Type of the object
		"""
		return self.world.describe( type )

