#!/usr/bin/python
# Filename: Simulation.py
# Description: Global singleton object that implements the simulation

from cos.core.simulation.SimulationThreadPool import SimulationThreadPool
from cos.core.simulation.Runner import Runner
from cos.core.kernel.Kernel import Kernel


class Simulation:
	__instance = None

	class __SimulationSingletonInstance(Kernel):
		def __init__(self):
			""" Constructor
			"""
			Kernel.__init__(self)
			return

		def start(self, settings):
			""" Starts the simulation kernel
			"""
			# Start the kernel
			Kernel.start(self, 'cos.ini', 'COS_CONFIG', settings)

			# Run the simulation
			self.runner	= Runner()
			self.runner.run(self)
			return

		def stop(self):
			""" Stops the simulation kernel
			"""
			# Shutdown the runner
			self.runner.stop()

			# Stop the kernel
			Kernel.stop(self)
			return

		def create_thread_pool(self):
			""" Creates the simulation thread pool
			"""
			return SimulationThreadPool(self)

	def __str__(self):
		""" Describes the kernel
		"""
		return self

	@staticmethod
	def instance():
		""" Returns the singleton instance of the kernel
		"""
		return Simulation()



	def __new__(cls): # __new__ always a classmethod
		""" Creates an instance of the singleton
		Arguments
			cls -- Class definition
		"""
		if not Simulation.__instance:
			Simulation.__instance = Simulation.__SimulationSingletonInstance()
		return Simulation.__instance

	def __getattr__(self, name):
		""" Returns an attribute of the kernel
		Arguments
			name -- Name of the attribute
		"""
		return getattr(self.__instance, name)

	def __setattr__(self, name, value):
		""" Sets an attribute on the kernel
		Arguments
			name -- Name of the attribute
			value -- Value of the attribute
		"""
		return setattr(self.__instance, name, value)


if __name__ == "__main__":
	test = Simulation.instance()


