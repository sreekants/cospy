#!/usr/bin/python
# Filename: WebSocketTransport.py
# Description: Implementation of the WebSocketTransport class

from cos.core.network.Transport import Transport
import asyncio
import websockets
import random
import json

RPCPORT			= 8756
MAX_MESSAGES	= 1024




class WebSocketContext:
	def __init__(self):
		""" Constructor
		"""
		self.rpcsocket	= None
		self.ipcsocket	= None
		self.stop		= True
		return

	async def init(self, transport, info):
		self.stop		= False

		# Create the socket ports
		self.rpcsocket = await websockets.serve(self.__create_rpc_handler(transport), "localhost", info['rpc_port'])
		self.ipcsocket = await websockets.serve(self.__create_ipc_handler(transport), "localhost", info['ipc_port'])

		await asyncio.gather(self.rpcsocket.wait_closed(), self.ipcsocket.wait_closed())

	def __create_rpc_handler(self, transport):
		async def echo(websocket):
			print(f"RPC.Client connected")

			try:
				# Keep the connection alive to receive messages from the client
				async for req in websocket:
					resp	= transport.runrpc(req)
					await websocket.send(json.dumps(resp))

			except websockets.exceptions.ConnectionClosed as e:
				print(f"Connection closed: {e}")
			finally:
				print("Client disconnected")
		return echo


	def __create_ipc_handler(self, transport):
		async def push(websocket):
			print(f"Client connected")

			try:
				# Send messages to the client asynchronously
				while not self.stop:
					msg = transport.runipc()
					if msg is not None:
						await websocket.send(json.dumps(msg))

					await asyncio.sleep(2)  # Wait 2 seconds before sending the next message

			except websockets.exceptions.ConnectionClosed as e:
				print(f"Connection closed: {e}")
			finally:
				print("Client disconnected")

		return push

class WebSocketTransport(Transport):
	def __init__(self, sim, broker, args:dict):
		""" Constructor
		Arguments
			sim -- Reference ot the simulation
			broker -- Broker name
			args -- List of arguments
		"""
		Transport.__init__(self, sim, broker, args)

		port 			= self.get_port(args)
		if port < 0:
			port		= RPCPORT

		self.port		= port
		self.context	= None
		return


	def get_port(self, args)->int:
		""" Returns the port address
		Arguments
			args -- List of arguments
		"""
		port	= args["port"]
		if port == None:
			return RPCPORT

		return int(port)

	def create(self):
		""" Creates the transport
		"""
		if self.context is not None:
			return

		self.context = WebSocketContext()

		# Setup the RPC socket
		#self.sim.log.info( 'WebSocket', f'Listening for RPC on [tcp://*:{self.port}]' )
		self.start()
		return

	def close(self):
		""" Closes the transport
		"""
		if self.context == None:
			return

		if self.rpcsocket is not None:
			self.context.rpcsocket.close()

		if self.context is not None:
			self.context = None
		return

	def runrpc(self, msg):
		""" Runs the RPC loop
		"""
		if self.sim is None:
			return { "r": msg }
		
		return msg

	def post( self, sock, objpath, req ):
		""" Posts a message to the socket
		Arguments
			sock -- Reference to the socket
			objpath -- Object path (on the object manager)
			req -- Request object
		"""
		try:
			# Invoke and generate result
			result	= self.broker.invoke_service( objpath, req, self.__to_args(req) )

			msg = { "r": result }

		except Exception as e:
			# Send an exception frame
			err		= {"e":f"ERROR : {str(e)}"}
			return err

		return msg

	def runipc(self):
		""" Runs an IPC loop
		"""
		if self.sim is None:
			return { "m": f"test = {random.randrange(10, 20)}", "d":"" }
		
		queue = self.sim.ipc.ipcq.queue

		# Check if ther are messages in the IPC queue to dispatcy
		if queue.empty():
			return

		# Build a payload of messages to send
		msg = []
		for n in range(0, MAX_MESSAGES):
			if queue.empty():
				break
			evt = queue.get()

			msg.append( {
				"m":evt.msg,
				"d":evt.arg
			} )

		# Send the payload as an event
		return msg

	def __to_args(self, req):
		""" Extracts the results from a request
		Arguments
			req -- Request data
		"""
		return req.d["a"].values()

	def start(self):
		asyncio.run(self.context.init(t,{"rpc_port":self.port, "ipc_port":self.port+1}))		
		

if __name__ == "__main__":
	t		= WebSocketTransport(None, None, {"port":8756})
	t.create()
	t.start()
