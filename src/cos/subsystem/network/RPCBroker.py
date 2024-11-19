#!/usr/bin/python
# Filename: RPCBroker.py
# Description: RPC broker thread and supporting classes

from cos.core.simulation.SimulationThread import SimulationThread
from cos.core.kernel.Subsystem import Subsystem
from cos.core.kernel.Context import Context
from cos.core.kernel.BootLoader import BootLoader
from cos.core.utilities.ArgList import ArgList

import time


class RPCBrokerThread(SimulationThread):
	def __init__(self, sim, broker, arg):
		""" Constructor
		Arguments
			sim -- Reference ot the simulation
			broker -- Reference to the broker
			arg -- Arguments to create the transport
		"""
		SimulationThread.__init__(self, sim)
		self.running	= True
		self.broker		= broker

		self.__create_transport(sim, broker, arg)

		return

	def __create_transport(self, sim, broker, arg):
		""" Creates a transport
		Arguments
			sim -- Reference ot the simulation
			broker -- Reference to the broker
			arg -- Arguments to create the transport
		"""
		self.transport	= None
		if arg == None:
			return

		args				= ArgList(arg)
		package				= args["transport"]

		if package==None or len(package) == 0:
			return

		klassname, klass	= BootLoader.load_class(package)

		self.transport		= klass(sim, broker, args)
		return

	def run(self):
		""" Runs the transport
		"""
		if self.transport == None:
			return

		with self.transport as layer3:
			while self.running:
				layer3.runrpc()
				layer3.runipc()

		return



	def stop(self):
		""" Signals the broker thread to terminate
		"""
		self.running	= False
		return

class RPCBroker(Subsystem):
	def __init__(self):
		""" Constructor
		"""
		Subsystem.__init__(self, "RPC", "Broker")
		self.thread		= None
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.sim	 = ctxt.sim

		config		= self.get_config(config)

		# Start the RPC thread
		self.thread	= RPCBrokerThread(ctxt.sim, self, config["config"])
		self.thread.start()

		# Reguster this broker as the master broker
		self.sim.ipc.broker	= self
		return

	def on_stop(self, ctxt:Context, config):
		""" Callback for simulation shutdown
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		# Stop the RPC thread
		self.thread.stop()
		self.thread.join()

		# Wait for sockets to close
		time.sleep(.5)
		return

	def invoke_service(self, objpath, req, args ):
		""" Invokes an RPC method on the service
		Arguments
			objpath -- Object path
			req -- Request to invoke on the object
			args -- List of arguments
		"""
		inst	= self.sim.objects.get( objpath )
		if inst == None:
			raise Exception( f'Object not found: {objpath}' )

		method = req.d["m"]
		if hasattr(inst, method) and callable(func:=getattr(inst, method)):
			return func( *args )

		raise Exception( f'Failed to call method{method} on {objpath}' )


if __name__ == "__main__":
	test = RPCBroker()


