#!/usr/bin/python
# Filename: ORPCProxy.py
# Description: Base class for all RPC proxy classes 

from cos.core.network.ZMQTransport import ZMQTransport

class ORPCProxy:
	def __init__(self, objectName):
		""" Constructor
		Arguments
			objectName -- Object name
		"""
		self.url = ""
		self.socket = None
		self.objectName = objectName
		self.flag = 0x40000000
		self.ttl = 2
		self.seq = 1

		if self.objectName == None:
			self.objectName = (f"/Services/API/{self.__class__.__name__}")

		self.objectName = self.objectName.replace("//","/")
		self.transport = ZMQTransport(self.objectName)
		return

	def bind(self, args=None):
		""" Bind the transport to an address
		Arguments
			args -- List of arguments
		"""
		return self.transport.bind(args)

	def invoke(self, method, args):
		""" Invokes a method
		Arguments
			method -- Method name
			args -- List of arguments
		"""
		self.transport.flag = self.flag
		self.transport.ttl = self.ttl
		self.transport.seq = self.seq
		return self.transport.invoke(method, args)


if __name__ == "__main__":
	test = ORPCProxy()

