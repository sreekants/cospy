#!/usr/bin/python
# Source File: WorldObject.py
# Description: Web service implementation.

from cos.core.network.ORPCService import ORPCService
from cos.core.simulation.Simulation import Simulation

class WorldObject(ORPCService):
	def __init__(self, type):
		""" Constructor
		Arguments
			type -- Type of the object
		"""
		ORPCService.__init__(self)
		self.type	= type
		return

	def describe( self, id ):
		""" #TODO: describe
		Arguments
			id -- Unique identifier
		"""
		object	= Simulation.instance().objects.get( f"/World/{self.type}/{id}" )
		if object == None:
			return {}
		return object




