#!/usr/bin/python
# Filename: Runner.py
# Description: The main kernel thread running its internal actions.

from cos.core.simulation.SimulationThread import SimulationThread
from cos.core.simulation.Snapshot import Snapshot
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
		return

	def step(self):
		""" Steps the simulation by one tick
		"""
		self.world.clock.advance()
		return

	def reset(self):
		""" Resets the simulation clock
		"""
		self.world.clock.reset()
		return

	@property
	def timestep(self):
		""" Returns the simulation tick
		"""
		return self.world.clock.tick

	@property
	def tick(self):
		""" Returns the simulated seconds since the epoch
		"""
		return self.world.clock.seconds

class Affinity:
	def __init__(self, text=None):
		""" Constructor
		Arguments
			text -- [ProcessManager] Affinity, e.g. 'Motion:Subsystem,Actors|Rules:Rules,Monitors'.
				The first group owns the clock and runs every faculty no group names
		"""
		self.groups	= []
		for part in (text or '').split('|'):
			if part.strip() == '':
				continue
			name, _, faculties	= part.partition(':')
			self.groups.append( (name.strip(), {f.strip() for f in faculties.split(',') if f.strip()}) )

		if len(self.groups) == 0:
			self.groups.append( ('Motion', set()) )

		self.named	= set().union( *[f for _, f in self.groups] )
		return

	def owns(self, index, faculty):
		""" Checks if a group runs the services of a faculty
		Arguments
			index -- Group index
			faculty -- Faculty the service was loaded from, or None
		"""
		if faculty in self.groups[index][1]:
			return True
		return (index == 0) and (faculty not in self.named)

class RunnerThread(SimulationThread):
	def __init__(self, sim, affinity:Affinity=None, index=0):
		""" Constructor
		Arguments
			sim -- Reference ot the simulation
			affinity -- Faculty groups, one thread each
			index -- Group this thread runs; group 0 owns the clock
		"""
		SimulationThread.__init__(self, sim)
		self.running	= True
		self.ticktime	= 0.030		# Wall-clock pause between ticks
		self.affinity	= affinity or Affinity()
		self.index		= index
		self.group		= self.affinity.groups[index][0]
		self.passes		= 0
		self.lags		= []

		# Duration of the simulation run in steps. -1 for infinite.
		self.duration	= sim.config.get_int('ProcessManager', 'RunCycles')
		return

	@property
	def owner(self):
		""" Checks if this thread owns the clock
		"""
		return self.index == 0

	def run(self):
		""" Runs the simulation
		"""
		# sim.objects.dump()
		time.sleep(self.ticktime)		# Delayed start

		if self.owner:
			self.run_clock()
		else:
			self.run_snapshots()
		return

	def run_clock(self):
		""" Advances the clock and ticks this group's services every tick
		"""
		clock		= SimulationClock(self.sim)
		clock.reset()

		# Set the simulation clock reference
		self.sim.simclock = clock

		while self.running:

			# Step the simulation clock
			clock.step()

			Snapshot.motion_busy( True )
			try:
				self.tick_services()
			finally:
				Snapshot.motion_busy( False )

			if self.duration > 0 and clock.timestep >= self.duration:
				self.stop()
				self.sim.log.info( 'Runner', f'Simulation duration of {self.duration} steps reached. Stopping simulation.' )
				self.runnable	= False
				break

			time.sleep(self.ticktime)
		return

	def run_snapshots(self):
		""" Ticks this group's services on the latest snapshot, skipping the ticks in between
		"""
		clock	= self.sim.clock
		judged	= None

		while self.running:
			snapshot	= Snapshot.latest()
			if (snapshot is None) or (snapshot.tick == judged):
				time.sleep(self.ticktime)
				continue

			clock.pin( snapshot.tick )
			Snapshot.pin( snapshot )
			try:
				self.tick_services()
			finally:
				Snapshot.pin( None )
				clock.unpin()

			judged	= snapshot.tick
			lag		= clock.live - snapshot.tick
			self.passes	+= 1
			self.lags.append( lag )
			self.sim.log.debug( 'Runner', f'{self.group} pass {self.passes} judged tick {snapshot.tick}, {lag} tick(s) behind' )

			time.sleep(self.ticktime)

		self.report()
		return

	def report(self):
		""" Logs how far this group's passes lagged the clock
		"""
		if len(self.lags) == 0:
			return
		mean	= sum(self.lags) / len(self.lags)
		self.sim.log.info( 'Runner', f'{self.group}: {self.passes} pass(es), lag mean {mean:.1f} and max {max(self.lags)} tick(s)' )
		return

	def tick_services(self):
		""" Runs one clock tick on this group's services
		"""
		for type in ['/Services']:
			self.sim.objects.traverse( type,
					self.__tick,
					self,
					8 )
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
	def __tick(thread, simulant:ObjectNode):
		""" Runs a single clock tick of the simulation on a simulant
		Arguments
			thread -- Runner thread ticking its group
			simulant -- The object being simulated
		"""
		if simulant.type != ObjectType.TYPE_SERVICE_OBJECT:
			return ErrorCode.ERROR_CONTINUE

		if simulant.handle == None:
			return ErrorCode.ERROR_CONTINUE

		if thread.affinity.owns( thread.index, simulant.faculty ) == False:
			return ErrorCode.ERROR_CONTINUE

		sim	= thread.sim
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
		self.thread		= None		# The thread that owns the clock
		self.threads	= []
		return

	def run(self, sim):
		""" Starts one simulation thread per faculty group
		Arguments
			sim -- Reference ot the simulation
		"""
		text		= None
		if sim.config.exists_value( 'ProcessManager', 'Affinity' ):
			text	= sim.config.get_value( 'ProcessManager', 'Affinity' )
		affinity	= Affinity( text )

		Snapshot.reset()
		self.threads	= [RunnerThread(sim, affinity, n) for n in range(len(affinity.groups))]
		self.thread		= self.threads[0]

		for n, (name, faculties) in enumerate(affinity.groups):
			owned	= ', '.join(sorted(faculties)) or 'all'
			sim.log.info( 'Runner', f'Thread {name}: {owned}{" (clock)" if n == 0 else ""}' )

		for t in self.threads:
			t.start()
		return

	def stop(self):
		""" Stops the simulation threads
		"""
		for t in self.threads:
			t.stop()
		for t in self.threads:
			t.join()
		return

	def runnable(self):
		""" Checks if the simulation is runnable
		"""
		return self.thread.is_active()

if __name__ == "__main__":
	test = Runner()


