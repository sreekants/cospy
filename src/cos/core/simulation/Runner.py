#!/usr/bin/python
# Filename: Runner.py
# Description: The main kernel thread running its internal actions.

from cos.core.simulation.SimulationThread import SimulationThread
from cos.core.kernel.Context import Context
from cos.core.kernel.ObjectManager import ObjectNode, ObjectType
from cos.core.utilities.Tree	import ErrorCode
from threading import Thread
import time

class RunnerThread(SimulationThread):
	def __init__(self, sim):
		""" Constructor
		Arguments
			sim -- Reference ot the simulation
		"""
		SimulationThread.__init__(self, sim)
		self.running	= True
		self.ticktime	= 0.030		# Ticks every .3 seconds
		return

	def run(self):
		""" Runs the simulation
		"""
		# sim.objects.dump()
		time.sleep(self.ticktime)		# Delayed start

		while self.running:

			for type in ['/Services']:
				self.sim.objects.traverse( type,
						self.__tick,
						self.sim,
						8 )

			time.sleep(self.ticktime)
		return


	def stop(self):
		""" Stops the simulation
		"""
		self.running	= False
		return

	@staticmethod
	def __tick(sim, simulant:ObjectNode):
		""" Runs a single clock tick of the simulation on a simulant
		Arguments
			sim -- Reference ot the simulation
			simulant -- The object being simulated
		"""
		if simulant.type != ObjectType.TYPE_SERVICE_OBJECT:
			return ErrorCode.ERROR_CONTINUE

		if simulant.handle == None:
			return ErrorCode.ERROR_CONTINUE

		# Trigger the timer on the service
		simulant.handle.on_timer( Context(sim, sim, sim.ipc), None )
		return ErrorCode.ERROR_CONTINUE

class Runner:
	def __init__(self):
		""" Constructor
		"""
		self.thread	= None
		return

	def run(self, sim):
		""" Starts the simulation thread
		Arguments
			sim -- Reference ot the simulation
		"""
		self.thread		= RunnerThread(sim)
		self.thread.start()
		return

	def stop(self):
		""" Stops the simulation thread
		"""
		self.thread.stop()
		self.thread.join()
		return

if __name__ == "__main__":
	test = Runner()


