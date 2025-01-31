#!/usr/bin/python
# Filename: RPCAgent.py
# Description: Agent servicing RPC requests

from cos.core.kernel.IPCMessage import IPCMessage, IPCFlags
from cos.core.network.ZMQFrame import ZMQFrame
import sys, time, zmq, random, msgpack, struct, datetime, socket

RPCAGENT_PORT		= 5557

class RPCAgent:
	def __init__(self):
		""" Constructor
		"""
		return

	def connect(self, host="localhost", port=RPCAGENT_PORT, ):
		""" Cpmmects to the server
		"""

		# Socket to talk to server
		self.context = zmq.Context()
		self.socket = self.context.socket(zmq.SUB)

		print( f"Collecting updates from world server on tcp://localhost:{port}..." )
		self.socket.connect ( f"tcp://{host}:{port}")

		self.topicfilter = ""
		self.socket.setsockopt(zmq.SUBSCRIBE, b'')
		self.poller		= zmq.Poller()
		self.poller.register(self.socket, zmq.POLLIN)
		return

	def pump(self, dispatcher, maxmsg=100):
		""" Pumps messages to from the event queue
		Arguments
			dispatcher -- Reference to the dispatcher
		"""

		if self.socket is None:
			return

		for n in range (maxmsg):
			socks = dict(self.poller.poll(10))
			if self.socket in socks and socks[self.socket] == zmq.POLLIN:

				# Receive the frame and unpack it
				req 	= self.socket.recv_multipart()

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

				dispatcher.notify( msg )
				continue

			break


		return



if __name__ == "__main__":
	test = RPCAgent()


