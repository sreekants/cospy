#!/usr/bin/python
# Filename: test_Vehicle.py
# Description: Test cases for the scenario time a vessel.move event carries

import types, unittest
import pygame

from cos.model.vehicle.Vehicle import Vehicle
from cos.core.time.Clock import Clock


class Queue:
	bridge	= '/Bridge'
	def __init__(self):
		self.published	= []
	def publish(self, msg, key, arg):
		self.published.append( (msg, key, arg) )
	def has_children(self, path):
		return False		# No bridge display subscribed, so no vessel.state


class VesselMoveTestCase(unittest.TestCase):
	def test_vessel_move_carries_the_local_time(self):
		clock	= Clock( 60.0, '2026-06-21T21:00:00+03:00' )
		for _ in range(3):
			clock.advance()

		ipc		= Queue()
		world	= types.SimpleNamespace( sim=types.SimpleNamespace(clock=clock, ipc=ipc) )
		actor	= types.SimpleNamespace( update=lambda world, config: (pygame.Rect(10, 20, 4, 2), (1.0, 0.0, 0.0), None) )
		vehicle	= types.SimpleNamespace( actor=actor, config=None, guid='v1', intent=[], signal=[] )
		Vehicle.sim_update( vehicle, world )

		msg, key, arg	= ipc.published[0]
		self.assertEqual( (msg, key), ('vessel.move', 'v1') )
		self.assertEqual( arg["time"], '2026-06-21T21:03:00+03:00' )
		self.assertEqual( arg["rect"], [10, 20, 4, 2] )


if __name__ == '__main__':
	unittest.main()
