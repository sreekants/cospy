#!/usr/bin/python
# Filename: CompositeService.py
# Description: Base class for all COS composite services

from cos.core.kernel.Service import Service
from cos.core.kernel.Object import Object
from cos.core.kernel.Context import Context

class CompositeService(Service):
	def __init__(self, type, name):
		""" Constructor
		Arguments
			type -- Type of the object
			name -- Name of the object
		"""
		Service.__init__(self, type, name)
		self.components	= []
		return

	def add_component(self, inst):
		""" Adds a component to the service collection
		Arguments
			inst -- Service to add to collection
		"""
		self.components.append(inst)
		return inst

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		Service.on_start(self, ctxt, config)
		for c in self.components:
			c.on_start(ctxt, config)
		return

	def on_timer(self, ctxt:Context, unused):
		""" Callback handling timer events
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		Service.on_timer(self, ctxt, unused)
		for c in self.components:
			c.on_timer(ctxt, unused)
		return

if __name__ == "__main__":
	test = CompositeService()


