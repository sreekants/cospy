#!/usr/bin/python
# Filename: ParameterManager.py
# Description: A parameter subsystem is a shared, dictionary that is accessible via APIs.
#              Processes use this server to store and retrieve parameters at runtime.

from cos.core.kernel.ObjectManager import ObjectManager, ObjectType, ObjectNode
from cos.core.kernel.Context import Context

class ParameterManager(ObjectManager):
	def __init__(self):
		""" Constructor
		"""
		ObjectManager.__init__(self)
		return

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		return

	def on_start(self, ctxt:Context, module):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		return

	def on_run(self, ctxt:Context, module):
		""" Event handler for run
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		return

	def on_term(self, ctxt:Context, module):
		""" Callback for simulation termination
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		return

	def on_stop(self, ctxt:Context, module):
		""" Callback for simulation shutdown
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		return


	def register( self, path:str, name:str, obj:any, type:ObjectType=ObjectType.TYPE_OPAQUE_OBJECT ):
		""" Registers a marameter
		Arguments
			path -- Path identifier of the parameter
			name -- Name of the object
			obj -- Reference to the object
			type -- Type of the object
		"""
		node	= self.ot.find( path )
		if node is None:
			param	= []
			node	= ObjectManager.register(self, path, str, param, type)
		else:
			param	= node.handle

		param.append(obj)
		return node

	def clear( self, path:str ):
		""" Clears a parameter
		Arguments
			path -- Path identifier of the parameter
		"""
		node	= self.ot.find( path )
		if node is None:
			return False

		param	= node.handle
		param.clear()
		return True

if __name__ == "__main__":
	test = ParameterManager()


