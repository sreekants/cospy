#!/usr/bin/python
# Filename: Snapshot.py
# Description: Per-tick state of the simulants, published by the motion thread and read by other threads

import copy, threading

class State:
	def __init__(self, x, dx, d2x, rect):
		""" Constructor
		Arguments
			x -- Position
			dx -- Velocity
			d2x -- Acceleration
			rect -- Bounding rectangle
		"""
		self.x		= x
		self.dx		= dx
		self.d2x	= d2x
		self.rect	= rect
		return

class Snapshot:
	__latest	= None
	__lock		= threading.Lock()
	__view		= threading.local()
	__idle		= threading.Event()		# Clear while the motion thread computes a tick
	__idle.set()

	def __init__(self, tick, states):
		""" Constructor
		Arguments
			tick -- Tick the states were taken at
			states -- Mapping of guid -> State
		"""
		self.tick	= tick
		self.states	= states
		return

	@staticmethod
	def capture(tick, vehicles):
		""" Copies the motion state of vehicles
		Arguments
			tick -- Current tick
			vehicles -- Vehicles to copy
		"""
		states	= {}
		for v in vehicles:
			actor	= getattr( v, 'actor', None )
			if actor is None:
				continue
			states[v.guid]	= State( copy.copy(actor.x), copy.copy(actor.dx),
									 copy.copy(actor.d2x), copy.copy(actor.rect) )
		return Snapshot( tick, states )

	@staticmethod
	def publish(snapshot):
		""" Makes a snapshot the latest one
		Arguments
			snapshot -- Snapshot to publish
		"""
		with Snapshot.__lock:
			Snapshot.__latest	= snapshot
		return

	@staticmethod
	def latest():
		""" Returns the latest published snapshot, or None
		"""
		with Snapshot.__lock:
			return Snapshot.__latest

	@staticmethod
	def reset():
		""" Forgets the published snapshot
		"""
		Snapshot.publish( None )
		Snapshot.motion_busy( False )
		return

	@staticmethod
	def motion_busy(busy):
		""" Marks the motion thread busy, so readers of a pinned snapshot wait for its tick to end
		Arguments
			busy -- True while the motion thread computes a tick
		"""
		if busy:
			Snapshot.__idle.clear()
		else:
			Snapshot.__idle.set()
		return

	@staticmethod
	def pin(snapshot):
		""" Makes the calling thread read simulants from a snapshot
		Arguments
			snapshot -- Snapshot to read, None to read live state
		"""
		Snapshot.__view.snapshot	= snapshot
		return

	@staticmethod
	def pinned():
		""" Returns the snapshot the calling thread reads, or None
		"""
		return getattr( Snapshot.__view, 'snapshot', None )

	@staticmethod
	def state(guid):
		""" Returns a simulant's state in the calling thread's snapshot, or None to read it live
		Arguments
			guid -- Simulant guid
		"""
		snapshot	= Snapshot.pinned()
		if snapshot is None:
			return None

		# Give way to the motion thread: it runs its tick without sharing the GIL
		if Snapshot.__idle.is_set() == False:
			Snapshot.__idle.wait( 1.0 )
		return snapshot.states.get( guid )


if __name__ == "__main__":
	test = Snapshot( 0, {} )
