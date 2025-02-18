#!/usr/bin/python
# Source File: Service.py
# Description: Web service implementation.

from cos.core.network.ORPCService import ORPCService
from cos.core.simulation.Simulation import Simulation
from cos.core.kernel.Object import Object

import inspect

class Service(ORPCService):
	def __init__(self):
		""" Constructor
		"""
		ORPCService.__init__(self)
		self.debug	= True
		return

	def stop( self, args ):
		""" #TODO: stop
		Arguments
			args -- List of arguments
		"""
		# TODO: Implement your method here.
		return 123456

	def start( self, args ):
		""" #TODO: start
		Arguments
			args -- List of arguments
		"""
		# TODO: Implement your method here.
		return 123456

	def suspend( self, args ):
		""" #TODO: suspend
		Arguments
			args -- List of arguments
		"""
		# TODO: Implement your method here.
		return 123456

	def resume( self, args ):
		""" #TODO: resume
		Arguments
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

	def call( self, arg ):
		""" #TODO: call
		Arguments
			arg -- #TODO
		"""
		# TODO: Implement your method here.
		return 123456

	def find( self, arg ):
		""" #TODO: find
		Arguments
			arg -- #TODO
		"""
		# TODO: Implement your method here.
		return 123456

	def info( self, path ):
		""" #TODO: info
		Arguments
			path -- #TODO
		"""
		obj:Object	= Simulation.instance().objects.get(path)
		if obj is None:
			raise Exception( f'Not object resolved for path [{path}].' )

		result	= []

		klass = obj.__class__
		result.append( f' Class:\t\t{obj.__class__.__name__}')
		result.append( f' Module:\t{obj.__class__.__module__}')
		result.append( f' ID:\t\t{obj.id}')
		result.append( f' Type:\t\t{obj.type}')
		result.append( f' Path:\t\t{path}')

		if obj.ipc_topic is not None:
			result.append( f' IPC:\t\t{obj.ipc_topic}')
		if self.debug:
			result.append( f' Source:\t{inspect.getsourcefile(obj.__class__)}')
		return '\r\n'.join(result)

	def list( self, arg ):
		""" #TODO: list
		Arguments
			arg -- #TODO
		"""
		return Simulation.instance().objects.dump()

	def pub( self, arg ):
		""" #TODO: pub
		Arguments
			arg -- #TODO
		"""
		# TODO: Implement your method here.
		return 123456

	def type( self, arg ):
		""" #TODO: type
		Arguments
			arg -- #TODO
		"""
		# TODO: Implement your method here.
		return 123456




