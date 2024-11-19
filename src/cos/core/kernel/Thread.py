#!/usr/bin/python
# Filename: Thread.py
# Description: Base class for all kernel threads

from cos.core.kernel.Kernel import Kernel
import threading

class Thread(threading.Thread):
	def __init__(self, kernel:Kernel):
		""" Constructor
		Arguments
			self -- reference to this instance
			sim -- reference to the simulation
		"""
		threading.Thread.__init__(self)
		self.kernel	= kernel
		return



if __name__ == "__main__":
	test = Thread()


