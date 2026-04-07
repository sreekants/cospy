#!/usr/bin/python
# Filename: Runner.py
# Description: The main kernel thread running its internal actions.

from cos.core.simulation.SimulationThread import SimulationThread
from cos.core.kernel.Context import Context
from cos.core.kernel.ObjectManager import ObjectNode, ObjectType
from cos.core.utilities.Tree	import ErrorCode
from threading import Thread
import time

class SimulationClock:
	def __init__(self, world):
		""" Constructor
		Arguments
			world -- Reference ot the simulation world
		"""
		self.world		= world
		self.timestep	= -1 	# timestep count
		self.tick		= self.world.clock.tickcount
		return
	
	def step(self):
		""" Steps the simulation by one tick
		Arguments
			world -- Reference ot the simulation world
		"""
		self.timestep	= self.timestep+1
		self.tick		= self.world.clock.tickcount
		return

	def reset(self):		
		""" Resets the simulation clock
		"""
		self.timestep	= 0
		self.tick		= 0
		return

class RunnerThread(SimulationThread):
	def __init__(self, sim):
		""" Constructor
		Arguments
			sim -- Reference ot the simulation
		"""
		SimulationThread.__init__(self, sim)
		self.running	= True
		self.ticktime	= 0.030		# Ticks every .3 seconds
		
		# Duration of the simulation run in steps. -1 for infinite.
		self.duration	= sim.config.get_int('ProcessManager', 'RunCycles')
		return

	def run(self):
		""" Runs the simulation
		"""
		# sim.objects.dump()
		time.sleep(self.ticktime)		# Delayed start
		clock		= SimulationClock(self.sim)
		clock.reset()

		# Set the simulation clock reference
		self.sim.simclock = clock

		while self.running:
						
			# Step the simulation clock
			clock.step()
			
			for type in ['/Services']:
				self.sim.objects.traverse( type,
						self.__tick,
						self.sim,
						8 )

			if self.duration > 0 and clock.timestep >= self.duration:
				self.stop()
				self.sim.log.info( 'Runner', f'Simulation duration of {self.duration} steps reached. Stopping simulation.' )
				self.runnable	= False
				break

			time.sleep(self.ticktime)
		return


	def is_active(self):		
		""" Checks if the simulation is runnable
		"""
		return self.running

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

		try:
			# Trigger the timer on the service
			simulant.handle.on_timer( Context(sim, sim, sim.ipc), None )
		except Exception as e:
			sim.log.error( 'Runner', f'Service [{simulant.name}] timer error: {e}' )
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

	def runnable(self):
		""" Checks if the simulation is runnable
		"""
		return self.thread.is_active()

if __name__ == "__main__":
	test = Runner()


