#!/usr/bin/python
# Source File: Service.py
# Description: Web service implementation.

from cos.core.network.ORPCService import ORPCService
from cos.core.simulation.Simulation import Simulation

class Service(ORPCService):
	def __init__(self):
		""" Constructor
		"""
		ORPCService.__init__(self)
		return

	def stop( self, name, args ):
		""" #TODO: stop
		Arguments
			name -- Name of the object
			args -- List of arguments
		"""
		# TODO: Implement your method here.
		return 123456

	def start( self, name, args ):
		""" #TODO: start
		Arguments
			name -- Name of the object
			args -- List of arguments
		"""
		# TODO: Implement your method here.
		return 123456

	def suspend( self, name, args ):
		""" #TODO: suspend
		Arguments
			name -- Name of the object
			args -- List of arguments
		"""
		# TODO: Implement your method here.
		return 123456

	def resume( self, name, args ):
		""" #TODO: resume
		Arguments
			name -- Name of the object
			args -- List of arguments
		"""
		# TODO: Implement your method here.
		return 123456

	def command( self, name, args ):
		""" #TODO: command
		Arguments
			name -- Name of the object
			args -- List of arguments
		"""
		# TODO: Implement your method here.
		return 123456

	def signal( self, event, args ):
		""" #TODO: signal
		Arguments
			event -- #TODO
			args -- List of arguments
		"""
		# TODO: Implement your method here.
		return 123456

	def describe( self, scope, args ):
		""" #TODO: describe
		Arguments
			scope -- Scope namespace
			args -- List of arguments
		"""
		# TODO: Implement your method here.
		return 123456




