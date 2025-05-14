#!/usr/bin/python
# Source File: Vessel.py
# Description: Web service implementation.

from cos.core.network.ORPCService import ORPCService
from cos.core.simulation.Simulation import Simulation


class Vessel(ORPCService):
	def __init__(self):
		""" Constructor
		"""
		ORPCService.__init__(self)
		return

	def describe( self, id ):
		""" Describes a vessel and its configurations
		Arguments
			id -- Unique identifier
		"""
		inst = self.__get_vessel(id)
		if inst == None:
			return {}

		return inst.describe()


	def init( self, id, config ):
		""" Initializes a vessel
		Arguments
			id -- Unique identifier
			config -- Configuration attributes
		"""
		inst = self.__get_vessel(id)
		if inst == None:
			return
		inst.initialize( config )
		return

	def ioctl( self, id, op, arg ):
		inst = self.__get_vessel(id)
		if inst == None:
			raise Exception( f"Unknown vessel {id}." )
		
		inst.ioctl( op, arg )
		return

	def update( self, id, state ):
		inst = self.__get_vessel(id)
		if inst == None:
			raise Exception( f"Unknown vessel {id}." )
		
		self.__update_pose(inst, state)
		return

	def __update_pose(self, inst, state):
		pose	= state.get("pose", None)
		if pose is None:
			return
		position	= pose.get("position", None)
		X			= pose.get("X", None)
		R			= pose.get("R", None)

		if position is not None:
			inst.ioctl( "position", position )

		if X is not None:
			inst.ioctl( "velocity", X )

		if R is not None:
			inst.ioctl( "heading", X )
		return

	def __get_vessel(self, id):
		""" Finds a vessel with an ID
		Arguments
			id -- Unique identifier
		"""
		return Simulation.instance().objects.find("/World/Vehicle/Vessel", id )

