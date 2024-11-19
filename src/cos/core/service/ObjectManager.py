#!/usr/bin/python
# Source File: ObjectManager.py
# Description: Web service implementation.

from cos.core.simulation.Simulation import Simulation
from cos.core.network.ORPCService import ORPCService

class ObjectManager(ORPCService):
	def __init__(self):
		""" Constructor
		"""
		ORPCService.__init__(self)
		self.om		= Simulation.instance().objects
		return

	def create( self, path, name, type, config ):
		""" Creates an object
		Arguments
			path -- Path of the object
			name -- Name of the object
			type -- Type of the object
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return

	def register( self, path, name, type, objref, config ):
		""" Registers an object
		Arguments
			path -- Path of the object
			name -- Name of the object
			type -- Type of the object
			objref -- Reference to an object
			config -- Configuration attributes
		"""
		inst = objref
		return self.om.register(path, name, object)

	def link( self, path, name, target, config ):
		""" Creates a symbolic link to an object
		Arguments
			path -- Path of the object
			name -- Name of the object
			target -- Target object path
			config -- Configuration attributes
		"""
		return self.om.link(path, name, target)

	def unregister( self, path, config ):
		""" Unregisters an object or link
		Arguments
			path -- Path of the object
			config -- Configuration attributes
		"""
		return self.om.unregister(path)

	def get( self, path, depth, config ):
		""" Returns a reference to the object
		Arguments
			path -- Path of the object
			depth -- Recursive depth to search for (for symbolic links)
			config -- Configuration attributes
		"""
		# TODO: Implement your method here.
		return None

	def find( self, path, depth, config ):
		""" Finds an object
		Arguments
			path -- Path of the object
			depth -- Recursive depth to search for (for symbolic links)
			config -- Configuration attributes
		"""
		return self.om.get_all(path)

	def exists( self, path, config ):
		""" Unregisters an object or link
		Arguments
			path -- Path of the object
			config -- Configuration attributes
		"""
		return self.om.exists(path)




