#!/usr/bin/python
# Filename: WebSocketBroker.py
# Description: RPC broker thread and supporting classes

from cos.core.simulation.SimulationThread import SimulationThread
from cos.core.kernel.Subsystem import Subsystem
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

import time, asyncio, websockets, json, functools

async def notify(websocket, sim):
	print("Client connected")
	target = websocket.request.path
	try:
		obj		= sim.objects.get(target)
		if obj is None:
			return
		
		resp    = { "r": obj.data() }
		message = json.dumps(resp)
		await websocket.send(message)
		await asyncio.sleep(1)  # Wait few seconds before sending the next message
	
		async for message in websocket:
			print(f"Received from client{message}")

	except websockets.exceptions.ConnectionClosed as e:
		print(f"Connection closed: {e}")
	finally:
		print("Client disconnected")


async def api(websocket, sim):
	print("RPC:Client connected")
	try:
		global start_at
		async for message in websocket:
			req = json.loads(message)
			start_at = req['r']['start']
			print(f"Received from client: {start_at}")

	except websockets.exceptions.ConnectionClosed as e:
		print(f"Connection closed: {e}")
	finally:
		print("Client disconnected")


# Server loops to service clients
async def ipc(sim, stop_event):
	async with websockets.serve(functools.partial(notify, sim=sim), "localhost", 8756):
		await stop_event.wait()

async def rpc(sim, stop_event):
	async with websockets.serve(functools.partial(api, sim=sim), "localhost", 8757):
		await stop_event.wait()

class BrokerThread(SimulationThread):
	def __init__(self, sim, broker, args:ArgList):
		""" Constructor
		Arguments
			sim -- Reference ot the simulation
			broker -- Reference to the broker
			args -- Arguments to create the transport
		"""
		SimulationThread.__init__(self, sim)
		self.running	= True
		self.broker		= broker
		return

class WebSocketBrokerThread(BrokerThread):
	def __init__(self, sim, broker, args:ArgList, package:str):
		""" Constructor
		Arguments
			sim -- Reference ot the simulation
			broker -- Reference to the broker
			args -- Arguments to create the transport
			package -- Transport software module implementing the stack
		"""
		BrokerThread.__init__(self, sim, broker, args)
		self.loop		= None
		self.stop_event	= None
		self.tasks		= []
		return

	async def _shutdown_async(self):
		"""Cancels the server tasks while the event loop is still running."""
		if self.stop_event is not None and self.stop_event.is_set() == False:
			self.stop_event.set()

		tasks = [task for task in self.tasks if task is not None and task.done() == False]
		for task in tasks:
			task.cancel()

		if len(tasks) > 0:
			await asyncio.gather(*tasks, return_exceptions=True)
		return

	def run(self):
		""" Runs the transport
		"""
		self.loop = asyncio.new_event_loop()
		asyncio.set_event_loop(self.loop)
		self.stop_event = asyncio.Event()
		self.tasks = [
			self.loop.create_task(ipc(self.sim, self.stop_event), name='websocket-ipc'),
			self.loop.create_task(rpc(self.sim, self.stop_event), name='websocket-rpc')
		]

		# Sleep a bit to allow the server to start before the simulation starts sending messages
		time.sleep(1)

		try:
			self.loop.run_forever()
		except KeyboardInterrupt:
			print("Shutting down")
		finally:
			pending = [task for task in asyncio.all_tasks(self.loop) if task.done() == False]
			for task in pending:
				task.cancel()
			if len(pending) > 0:
				self.loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
			self.loop.run_until_complete(self.loop.shutdown_asyncgens())
			self.loop.close()
			asyncio.set_event_loop(None)
		return



	def stop(self):
		""" Signals the broker thread to terminate
		"""
		if self.loop is None or self.loop.is_closed():
			self.running	= False
			return

		try:
			future = asyncio.run_coroutine_threadsafe(self._shutdown_async(), self.loop)
			future.result(timeout=2)
		finally:
			self.loop.call_soon_threadsafe(self.loop.stop)

		self.running	= False
		return

class WebSocketBroker(Subsystem):
	def __init__(self):
		""" Constructor
		"""
		Subsystem.__init__(self, "WebSocket", "Broker")
		self.threads	= []
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		self.sim	= ctxt.sim
		args		= ArgList(config["config"])
		transports	= args['transport']
		if transports == None:
			return

		transports	= transports.split(',')
		
		# Start the RPC thread for each protocol
		for proto in transports:
			thread	= WebSocketBrokerThread(ctxt.sim, self, args, proto)
			thread.start()

			self.threads.append( thread )

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
		for thread in self.threads:
			thread.stop()
			thread.join()

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

		raise Exception( f'Failed to call method[{method}] on [{objpath}]' )


if __name__ == "__main__":
	test = WebSocketBroker()


