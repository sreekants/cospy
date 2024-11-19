#!/usr/bin/python
# Filename: RpcBroker_test.py
# Description: Test cases for the RpcBroker class

from cos.core.simulation.Simulation import Simulation
from cos.core.simulation.Context import Context
from cos.core.subsystem.RPCBroker import RPCBroker, RPCPORT
from cos.core.simulation.Service import Service
from cos.core.api.Timer import Timer

from cos.core.network.ORPCService import ORPCService

import unittest, zmq, sys

class TimerService(ORPCService):
	def __init__(self):
		ORPCService.__init__(self,"Timer")
		return
	
	def get_utc(self):
		return 128123


class RpcBrokerTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.broker	= RPCBroker()
		self.sim = Simulation.instance()
		self.ctxt = Context(self.sim, None, None)
		self.timer = TimerService()		
		self.timer.on_init(self.ctxt, None)# Registers automatically
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_start(self):
		self.assertTrue( self.sim.objects.exists("/Services/API/Timer") )
		self.broker.on_start(self.ctxt, None)

		context = zmq.Context()
		socket = context.socket(zmq.REQ)
		socket.connect ("tcp://localhost:%i" % RPCPORT)

		for request in range (1,10):
			try:
				print( f"Sending request {request}..." )
				
				timer = Timer()
				timer.bind()
				message = timer.get_utc()

				#  Get the reply.
				print( f"Received reply {request}: {message}" )
			except Exception as e:
				print( e )
				pass

		self.broker.on_stop(None, None)

if __name__ == '__main__':
    unittest.main()
