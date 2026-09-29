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
		""" Returns the simulated time as UTC epoch seconds
		"""
		return int( self.clock.utc.timestamp() )

	def get_tickcount( self,):
		""" Returns the simulation tick
		"""
		return self.clock.tickcount




