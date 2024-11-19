#!/usr/bin/python
# Source File: Topic.py
# Description: Web service implementation.

from cos.core.network.ORPCService import ORPCService
from cos.core.simulation.Simulation import Simulation

class Topic(ORPCService):
	def __init__(self):
		""" Constructor
		"""
		ORPCService.__init__(self)
		self.ipc	= Simulation.instance().ipc
		return

	def assert_path(self, path):
		""" #TODO: assert_path
		Arguments
			path -- #TODO
		"""
		if self.ipc.exists(path) == False:
			raise RuntimeError( f'Topic {path} does not exist.' )
		return path

	def pop( self, path ):
		""" #TODO: pop
		Arguments
			path -- #TODO
		"""
		self.assert_path( path )
		evt	= self.ipc.pop(path)
		if evt == None:
			return None

		return evt.msg

	def push( self, path, msg ):
		""" #TODO: push
		Arguments
			path -- #TODO
			msg -- #TODO
		"""
		self.assert_path( path )
		self.ipc.push(path, msg)
		return

	def find( self, path ):
		""" #TODO: find
		Arguments
			path -- #TODO
		"""
		return self.ipc.find(path)

	def info( self, path ):
		""" #TODO: info
		Arguments
			path -- #TODO
		"""
		return self.ipc.info(path)

	def list( self, path ):
		""" #TODO: list
		Arguments
			path -- #TODO
		"""
		return self.ipc.dump(path)

	def type( self, path ):
		""" #TODO: type
		Arguments
			path -- #TODO
		"""
		self.assert_path( path )
		return f'{path}:INFO'

	def route( self, src, dest ):
		""" #TODO: route
		Arguments
			src -- #TODO
			dest -- #TODO
		"""
		return self.ipc.route( src, dest )

	def unroute( self, path ):
		""" #TODO: unroute
		Arguments
			path -- #TODO
		"""
		return self.ipc.unroute( path )




