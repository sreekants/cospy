#!/usr/bin/python
# Filename: SimulationThreadPool.py
# Description: Implementation of the thread pool used in simulation

from cos.core.kernel.ThreadPool import ThreadPool, PoolThread

class SimulationPoolThread(PoolThread):
	def __init__(self, sim, pool):
		""" Constructor.
		Arguments
			sim -- reference to the simulation
			pool -- reference to the pool
		"""
		PoolThread.__init__(self, sim, pool)
		return

	@property
	def sim(self):
		""" Returns a reference to the simulation kernel
		"""
		return self.kernel

class SimulationThreadPool(ThreadPool):
	def __init__(self, sim):
		""" Constructor
		Arguments
				sim -- reference to the simulation
		"""
		ThreadPool.__init__(self, sim)
		return

	@property
	def sim(self):
		""" Returns a reference to the simulation kernel
		"""
		return self.kernel

	def create_thread(self):
		""" Overridable to create the pool thread instance
		"""
		thread	= SimulationPoolThread(self.kernel, self)
		thread.start()
		return thread



if __name__ == "__main__":
	test = SimulationThreadPool( None )


