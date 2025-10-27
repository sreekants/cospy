#!/usr/bin/python
# Filename: ZMQTransport.py
# Description: Transport layer class for ZMQ support.

from cos.core.kernel.IPCMessage import IPCMessage, IPCFlags
from cos.core.network.RPCZMQTransport import RPCPORT
from cos.core.network.ZMQFrame import ZMQFrame

import zmq, msgpack

DEFAULT_HOST = f"tcp://localhost:{RPCPORT}"

class ZMQTransport:
	def __init__(self, objname):
		""" Constructor
		Arguments
			objname -- Object name
		"""
		self.socket		= None
		self.objname	= objname
		self.seq		= 0
		self.ttl		= 2
		self.flag		= 0
		self.timeout	= 5000
		return

	@staticmethod
	def set_host(host):
		""" Sets the host of the transport
		Arguments
			host -- Host name
		"""
		global DEFAULT_HOST
		DEFAULT_HOST = f'tcp://{host}'
		return

	def is_open(self):
		""" Checks if the transport is open
		"""
		return (self.socket is not None)

	def set_timeout(self, timeout):
		""" Sets the timeout for the transport
		Arguments
			timeout -- Timeout value
		"""
		self.timeout	= timeout
		return

	def bind(self, host=None):
		""" Binds the
		Arguments
			host -- Host address
		"""
		if self.socket is not None:
			self.close()

		if host is None:
			host	= DEFAULT_HOST

		print( "Connecting to {}".format(host) )
		context = zmq.Context()
		self.socket = context.socket(zmq.REQ)
		self.socket.connect (host)
		return self.socket

	def close(self):
		""" Closes the transport
		"""
		if self.socket is None:
			return False

		self.socket.close()
		self.socket=None
		return True

	def invoke(self, method, args, flag=0x40000000, ttl=2):
		""" Invokes a method on the transport
		Arguments
			method -- Method name
			args -- List of arguments
			flag -- Binary 32-bit flag
			ttl -- Time to live for the request
		"""
		if self.socket is None:
			self.bind()

		msg = self.invoke_raw( method, args, flag, ttl )
		if msg.failed():
			raise Exception( msg.d["e"] )

		return msg.d["r"]


	def invoke_raw(self, method, args, flag=0x40000000, ttl=2):
		""" Low level method to invoke a method
		Arguments
			method -- Method name
			args -- List of arguments
			flag -- Binary 32-bit flag
			ttl -- Time to live for the request
		"""
		if args is None:
			args	= {}

		msg = {'m': method,
			'a': args
			}

		req = ZMQFrame.encode(
				self.objname,
				self.seq,
				flag,
				ttl,
				msg
			)

		self.socket.send_multipart( req )
		if self.socket.poll(self.timeout) == 0:
			raise Exception( "Connection timed out." )

		return ZMQFrame.decode( self.socket.recv_multipart() )


if __name__ == "__main__":
	test = ZMQTransport()

