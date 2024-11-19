#!/usr/bin/python
# Filename: Object.py
# Description: Base class for all the objects in the simulation

from cos.core.kernel.Context import Context
from typing import Any
import uuid

class Object:
	def __init__(self, type:str, id:str=None, guid:str=None ):
		""" Constructor
		Arguments
			type -- Type of the object
			id -- Unique identifier (usually within a class)
			guid -- Globally unique identifier of the object
		"""
		if guid == None:
			self.guid	= str(uuid.uuid1()).lower()
		else:
			self.guid	= guid

		if id == None:
			self.id	= self.guid
		else:
			self.id	= id

		self.type		= type.replace('/','.')
		self.ipc_topic	= None
		self.callbacks	= {}
		return

	def listen(self, topic:str):
		""" Sets the object to listen to an IPC topic
		Arguments
			topic -- Path of the IPC topic
		"""
		if topic.startswith('/') == False:
			raise Exception( f'Invalid topic name [{path}]' )

		self.ipc_topic	= topic
		return

	@property
	def topic(self):
		""" Returns the IPC topic the object listens to
		"""
		return self.ipc_topic

	def push_msg(self, ctxt:Context, msg:str, arg=None):
		""" Pushes a message to the IPC queue
		Arguments
			ctxt -- Simulation context
			msg -- Message string
			arg -- Message properties (name-value pairs)
		"""
		ctxt.ipc.push( self.ipc_topic, msg, ctxt, arg )
		return

	def pop_msg(self, ctxt:Context, arg=None):
		""" Pops a message from the IPC queue
		Arguments
			ctxt -- Simulation context
			arg -- Message properties (name-value pairs)
		"""
		return ctxt.ipc.pop( self.ipc_topic )

	def notify(self, ctxt:Context, method:str, arg:Any):
		""" Triggers a method
		Arguments
			ctxt -- Simulation context
			method -- Method name
			arg -- Message argumnt
		"""
		if method in self.callbacks:
			self.callbacks[method](ctxt, arg)
		return

	def subscribe(self, method:str, handler):
		""" Assign a handler to a notification method
		Arguments
			method -- Method name
			handler -- Handler for the method
		"""
		self.callbacks[method]	= handler
		return

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		self.initalize( ctxt, module)
		return

	def initalize(self, ctxt:Context, module):
		""" Initializes the object
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		if self.ipc_topic is not None:
			ctxt.sim.ipc.subscribe(self.ipc_topic, self)

		namespace = self.type.replace('.', '/')
		ctxt.sim.objects.register( f'/{namespace}', self.id, self )
		return

	def on_start(self, ctxt:Context, unused):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		return

	def on_run(self, ctxt:Context, runlevel:int):
		""" Event handler for run
		Arguments
			ctxt -- Simulation context
			runlevel -- Run level
		"""
		return

	def on_suspend(self, ctxt:Context, unused):
		""" Callback for simulation suspension
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		return

	def on_stop(self, ctxt:Context, unused):
		""" Callback for simulation shutdown
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		return

	def on_term(self, ctxt:Context, unused):
		""" Callback for simulation termination
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		return

if __name__ == "__main__":
	test = Object()


