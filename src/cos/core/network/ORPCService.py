#!/usr/bin/python
# Filename: ORPCService.py
# Description: The base class for all API services

from cos.core.simulation.SimulationThread import SimulationThread
from cos.core.kernel.Service import Service
from cos.core.kernel.Context import Context

class ORPCService(Service):
	def __init__(self, name=None):
		""" Constructor
		Arguments
			name -- Name of the object
		"""
		if name == None:
			name	= self.__class__.__name__

		Service.__init__(self, "API", name)
		return


if __name__ == "__main__":
	test = ORPCService()

