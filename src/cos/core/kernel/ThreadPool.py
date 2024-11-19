#!/usr/bin/python
# Filename: ThreadPool.py
# Description: Implementation of a kernel thread pool to run client services.

import cos.core.utilities.ThreadPool

class PoolThread(cos.core.utilities.ThreadPool.PoolThread):
	def __init__(self, kernal, pool):
		""" Constructor.
		Arguments
			self -- reference to this instance
			sim -- reference to the simulation
			pool -- reference to the pool
		"""
		cos.core.utilities.ThreadPool.PoolThread.__init__(self, pool)
		self.kernal	= kernal
		return

class ThreadPool(cos.core.utilities.ThreadPool.ThreadPool):
	def __init__(self, kernel):
		""" Constructor
		Arguments
			self -- reference to this instance
			sim -- reference to the simulation
		"""
		cos.core.utilities.ThreadPool.ThreadPool.__init__(self)
		self.kernel	= kernel
		return


	def create_thread(self):
		""" Overridable to create the pool thread instance
		"""
		thread	= PoolThread(self.kernel, self)
		thread.start()
		return thread



if __name__ == "__main__":
	test = ThreadPool()


