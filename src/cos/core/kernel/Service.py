#!/usr/bin/python
# Filename: Service.py
# Description: Base class for all COS services

from cos.core.kernel.Object import Object
from cos.core.kernel.Context import Context

class Service(Object):
	def __init__(self, type, name):
		""" Constructor
		Arguments
			type -- Type of the object
			name -- Name of the object
		"""
		category	= 'Services'

		if name == None:
			name	= self.__class__.__name__

		scope	= f'{category}/{type}'
		Object.__init__( self, scope, name )

		self.ipc_nodes	= []
		return

	def on_start(self, ctxt:Context, unused):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		namespace = self.type.replace('.', '/')
		self.listen( f'/{namespace}/{self.id}' )
		return

	def on_timer(self, ctxt:Context, unused):
		""" Callback handling timer events
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		# Pump events on IPC nodes
		for node in self.ipc_nodes:
			ctxt.ipc.pump_node( node )

		return

	def poll_ipc(self, ctxt, pathlist):
		""" Registers a list of paths for polling on the IPC queue
		Arguments
			ctxt -- Simulation context
			pathlist -- List of IPC queue paths
		"""
		for path in pathlist:
			node = ctxt.ipc.get_node( path )
			if node is None:
				ctxt.log.error( self.type, f'Failed to resolve IPC queues[{path}]' )
				continue

			self.ipc_nodes.append( node )

		return


if __name__ == "__main__":
	test = Service()


