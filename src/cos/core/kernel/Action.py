#!/usr/bin/python
# Filename: Action.py
# Description: Base class for COS actions

from cos.core.kernel.Object import Object
from cos.core.kernel.Context import Context

class Action(Object):
	def __init__(self, type, name):
		""" Constructor
		Arguments
			type -- Type of the object
			name -- Name of the object
		"""
		category	= 'Actions'

		if name is None:
			name	= self.__class__.__name__

		scope	= f'{category}/{type}'
		Object.__init__( self, scope, name )
		return

	def on_start(self, ctxt:Context, unused):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		self.listen( f'{self.type}/{self.id}' )
		return

	def on_timer(self, ctxt:Context, unused):
		""" Callback handling timer events
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		return



if __name__ == "__main__":
	test = Action()


