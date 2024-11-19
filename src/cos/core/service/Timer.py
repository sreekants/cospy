#!/usr/bin/python
# Source File: Timer.py
# Description: Web service implementation.

from cos.core.network.ORPCService import ORPCService
from cos.core.simulation.Simulation import Simulation
from cos.core.time.Clock import Clock

class Timer(ORPCService):
	def __init__(self):
		""" Constructor
		"""
		ORPCService.__init__(self)
		self.clock:Clock	= Simulation.instance().clock
		return

	def get_utc( self,):
		""" #TODO: get_utc
		Arguments
			 -- #TODO
		"""
		return self.clock.utc

	def get_tickcount( self,):
		""" #TODO: get_tickcount
		Arguments
			 -- #TODO
		"""
		return self.clock.tickcount




