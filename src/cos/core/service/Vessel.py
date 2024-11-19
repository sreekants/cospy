#!/usr/bin/python
# Source File: Vessel.py
# Description: Web service implementation.

from cos.core.network.ORPCService import ORPCService
from cos.core.simulation.Simulation import Simulation
from cos.core.kernel.ObjectManager import ObjectNode, ObjectType
from cos.core.utilities.Errors import ErrorCode

class ObjectQuery:
	def __init__(self, text):
		""" Constructor
		Arguments
			text -- #TODO
		"""
		self.text	= text
		self.match	= None
		return

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

	def __get_vessel(self, id):
		""" Finds a vessel with an ID
		Arguments
			id -- Unique identifier
		"""
		query = ObjectQuery(id)

		Simulation.instance().objects.traverse("/World/Vehicle/Vessel", self.__match_node_by_name, query, 0xFFFF )
		return query.match

	@staticmethod
	def __match_node_by_name(result:ObjectQuery, node:ObjectNode):
		""" Finds a matching vessel with a name
		Arguments
			result -- #TODO
			node -- #TODO
		"""
		if node.type != ObjectType.TYPE_SERVICE_OBJECT:
			return ErrorCode.ERROR_CONTINUE

		if node.name != result.text:
			return ErrorCode.ERROR_CONTINUE

		# Return the match immediately
		result.match	= node.handle
		return ErrorCode.S_OK


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
