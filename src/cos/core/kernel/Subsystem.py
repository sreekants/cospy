#!/usr/bin/python
# Filename: Service.py
# Description: Base class for all COS subsystems

from cos.core.kernel.Service import Service
from cos.core.kernel.Context import Context

class Subsystem(Service):
	def __init__(self, type, name):
		""" Constructor
		Arguments
			type -- Type of the object
			name -- Name of the object
		"""
		Service.__init__(self, type, name)
		return

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		Service.on_init(self, ctxt, module)
		return

	def on_start(self, ctxt:Context, unused):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		Service.on_start( self, ctxt, unused )
		self.sim	= ctxt.sim
		return

if __name__ == "__main__":
	test = Service()


