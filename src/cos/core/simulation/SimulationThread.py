#!/usr/bin/python
# Filename: SimulationThread.py
# Description: Base class for all general threads used in the simulation

from cos.core.kernel.Thread import Thread

class SimulationThread(Thread):
	def __init__(self, sim):
		""" Constructor
		Arguments
			sim -- reference to the simulation kernel
		"""
		Thread.__init__(self, sim)
		return

	@property
	def sim(self):
		""" Returns a reference to the simulation kernel
		"""
		return self.kernel

if __name__ == "__main__":
	test = SimulationThread()


