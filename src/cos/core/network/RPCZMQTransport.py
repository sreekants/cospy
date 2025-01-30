#!/usr/bin/python
# Filename: RPCZMQTransport.py
# Description: Implementation of the RPC Transport for ZMQ

from cos.core.network.Transport import Transport
from cos.core.kernel.Context import Context
from cos.core.kernel.IPCMessage import IPCMessage, IPCFlags
from cos.core.network.ZMQFrame import ZMQFrame

import time, zmq, random, msgpack, struct, datetime, socket

RPCPORT			= 5556
MAX_MESSAGES	= 1024

class RPCZMQTransport(Transport):
	def __init__(self, sim, broker, args:dict):
		""" Constructor
		Arguments
			sim -- Reference ot the simulation
			broker -- Broker name
			args -- List of arguments
		"""
		Transport.__init__(self, sim, broker, args)

		self.poller		= zmq.Poller()

		self.context	= None
		self.rpcsocket	= None
		self.ipcsock	= None

		port 			= self.get_port(args)
		if port < 0:
			port		= RPCPORT

		self.port		= port
		return

	def __enter__(self):
		""" Called when locked
		"""
		self.create()
		return self

	def __exit__(self, exception_type, exception_value, exception_traceback):
		""" Called when exception occurs
		Arguments
			exception_type -- Type of exception
			exception_value -- Valie of the exception
			exception_traceback -- Exception stack
		"""
		self.close()
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

		self.context = zmq.Context()

		# Setup the RPC socket
		address			= f"tcp://*:{self.port}"
		self.rpcsocket	= self.context.socket(zmq.REP)
		self.rpcsocket.bind( address )
		self.poller.register(self.rpcsocket, zmq.POLLIN)
		self.sim.log.info( 'RPC', f'Listening for RPC on [{address}]' )

		# Setup the IPC socket
		ipcaddr		 = f"tcp://*:{self.port+1}"
		self.ipcsock = self.context.socket(zmq.PUB)
		self.ipcsock.bind( ipcaddr )
		self.sim.log.info( 'IPC', f'Posting IPC events on [{ipcaddr}]' )
		return

	def close(self):
		""" Closes the transport
		"""
		if self.context == None:
			return

		if self.rpcsocket is not None:
			self.rpcsocket.close()

		if self.ipcsock is not None:
			self.ipcsock.close()

		if self.context is not None:
			self.context.destroy()
			self.context = None
		return

	def is_pending(self):
		""" Checks if a request is queued
		"""
		socks = dict(self.poller.poll(800))
		if self.rpcsocket in socks and socks[self.rpcsocket] == zmq.POLLIN:
			return True

		return False

	def runrpc(self):
		""" Runs the RPC loop
		"""
		socks = dict(self.poller.poll(800))
		if self.rpcsocket in socks and socks[self.rpcsocket] == zmq.POLLIN:
			# Receive the frame and unpack it
			req 	= self.rpcsocket.recv_multipart()

			objpath	= req[1].decode("utf-8")
			props	= struct.unpack( 'iii', req[2] )
			data	= msgpack.unpackb( req[3] )

			# Encode the received packet to a message
			msg			= IPCMessage(objpath, "")
			now			= int(datetime.datetime.now(datetime.timezone.utc).timestamp())
			msg.id		= socket.ntohl(props[0])	# ID of the message
			msg.flag	= socket.ntohl(props[1])	# Message flags
			msg.ttl		= socket.ntohl(props[2])	# Time to live for the message

			msg.d		= data		# Payload of the message
			msg.p		= ""		# Properties of the payload
			msg.tc		= now		# Time the message was created
			msg.ts		= now		# Time the message was sent (UTC)
			msg.ta		= None		# Time the message arrived at the destination (UTC)

			self.__post( self.rpcsocket, objpath, msg )

	def __post( self, sock, objpath, req ):
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

			if req.ttl>1:
				ttl	= req.ttl-1
			else:
				ttl	= 1

			resp = ZMQFrame.encode(
					objpath,
					req.id,
					req.flag,
					ttl,
					msg
				)

			sock.send_multipart(resp)
			return
		except Exception as e:
			# Send an exception frame
			err		= {"e":f"ERROR : {str(e)}"}
			resp = ZMQFrame.encode(
					objpath,
					req.id,
					IPCFlags.IPC_MESSAGE_EXCEPTION,
					1,
					err
				)

			sock.send_multipart( resp )

		return

	def runipc(self):
		""" Runs an IPC loop
		"""
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
		self.notify( msg )
		return

	def notify(self, events):
		""" Notifies events remotely
		Arguments
			events -- Events to dispatch
		"""
		try:
			# Invoke a remote asynchronous IPC call
			req = ZMQFrame.encode(
					'/IPC',
					socket.ntohl(0xFFFF),
					0,
					0,
					events
				)

			self.ipcsock.send_multipart( req )
		except Exception as e:
			pass

		return

	def __to_args(self, req):
		""" Extracts the results from a request
		Arguments
			req -- Request data
		"""
		return req.d["a"].values()


if __name__ == "__main__":
	test = RPCZMQTransport()


