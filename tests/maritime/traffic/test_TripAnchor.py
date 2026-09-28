#!/usr/bin/python
# Filename: test_TripAnchor.py
# Description: Test cases for the anchor(<s>) trip action (COS.014)

from unittest import mock
import unittest

import numpy as np

from cos.behavior.motion.PathFollowingMotionBehavior import PathFollowingMotionBehavior
from maritime.behavior.vessels.PlannedVesselBehavior import PlannedVesselBehavior
from maritime.behavior.vessels.FishingVessel import FishingVessel
from maritime.behavior.vessels.Ferry import Ferry
from maritime.model.vessel.Vessel import Status


class Log:
	def __init__(self):
		self.warnings	= []

	def warning(self, module, text):
		self.warnings.append( text )


class Context:
	def __init__(self, clock):
		self.log	= Log()
		self.sim	= mock.Mock()
		self.sim.config	= None
		self.sim.clock	= clock
		self.sim.objects.get.return_value	= None


class Vehicle:
	def __init__(self):
		self.name	= 'Test Ferry'
		self.status	= Status.UNDERWAY

	def anchored(self):
		self.status	= Status.ANCHORED

	def under_way(self):
		self.status	= Status.UNDERWAY


class Clock:
	def __init__(self):
		self.seconds	= 1000.0		# Simulated seconds


class TripAnchorTestCase(unittest.TestCase):
	def setUp(self):
		self.clock	= Clock()
		self.ctxt	= Context( self.clock )

	def behavior(self, cls=PlannedVesselBehavior):
		b			= cls( self.ctxt, {} )
		b.vehicle	= Vehicle()
		b.rect		= None
		b.dx		= np.zeros(3)
		return b

	def waypoint(self, action):
		return PathFollowingMotionBehavior.waypoint( [], 0, 10.0, 0.0, 0.0, 1.5, 0.0, action )[0]

	def test_anchor_calls_anchor_with_its_duration(self):
		for action, duration in (('anchor(1.5)', 1.5), ('anchor(2)', 2.0), (' anchor( 2 )', 2.0)):
			b	= self.behavior()
			with mock.patch.object( b, 'anchor' ) as anchor:
				b.on_at_waypoint( None, None, 1, self.waypoint(action) )
			anchor.assert_called_once_with( duration )

	def test_anchor_stops_the_vessel_until_the_watch_expires(self):
		b	= self.behavior()
		b.on_at_waypoint( None, None, 1, self.waypoint('anchor(2)') )

		self.assertEqual( b.vehicle.status, Status.ANCHORED )
		self.assertFalse( b.movable )

		self.clock.seconds	+= 1.5
		b.update( None, None, {} )
		self.assertEqual( b.vehicle.status, Status.ANCHORED )

		self.clock.seconds	+= 0.5
		b.update( None, None, {} )
		self.assertEqual( b.vehicle.status, Status.UNDERWAY )
		self.assertTrue( b.movable )
		self.assertIsNone( b.watchdogs['anchor'] )

	def test_reaching_an_anchor_waypoint_on_the_path_anchors(self):
		b			= self.behavior( Ferry )
		b.path		= PathFollowingMotionBehavior.waypoint( [], 0, 0.0, 0.0, 0.0, 1.5, 0.0, '' ) + [ self.waypoint('anchor(2)') ]
		t			= mock.Mock( timestep=1.0 )

		b.move_next( None, t )
		b.x			= np.array( (9.5, 0.0, 0.0) )
		b.move_next( None, t )

		self.assertEqual( b.vehicle.status, Status.ANCHORED )

	def test_each_waypoint_fires_once_per_lap(self):
		b			= self.behavior( Ferry )
		path		= []
		for n, x in enumerate( (0.0, 10.0, 20.0) ):
			PathFollowingMotionBehavior.waypoint( path, n, x, 0.0, 0.0, 1.5, 0.0, f'wp{n}' )
		b.path, b.looprun, b.reverse	= path, True, True
		t			= mock.Mock( timestep=1.0 )

		seen		= []
		b.on_at_waypoint	= lambda world, t, n, pt: seen.append( pt[3] )

		b.move_next( None, t )
		for _ in range(4):
			b.x		= b.next[1].copy()
			b.move_next( None, t )

		self.assertEqual( seen, ['wp0', 'wp1', 'wp2', 'wp1', 'wp0'] )

	def test_subclasses_fall_back_to_anchor(self):
		b	= self.behavior( FishingVessel )
		b.on_at_waypoint( None, None, 1, self.waypoint('anchor(1.5)') )
		self.assertEqual( b.vehicle.status, Status.ANCHORED )

	def test_unknown_action_is_logged_once(self):
		b	= self.behavior()
		for _ in range(3):
			b.on_at_waypoint( None, None, 1, self.waypoint('ancor(2)') )
		b.on_at_waypoint( None, None, 1, self.waypoint('anchor(two)') )

		self.assertEqual( b.vehicle.status, Status.UNDERWAY )
		self.assertEqual( len(self.ctxt.log.warnings), 2 )
		self.assertIn( "'ancor(2)'", self.ctxt.log.warnings[0] )

	def test_no_action_does_nothing(self):
		b	= self.behavior()
		b.on_at_waypoint( None, None, 1, self.waypoint('') )
		self.assertEqual( b.vehicle.status, Status.UNDERWAY )
		self.assertEqual( self.ctxt.log.warnings, [] )


if __name__ == '__main__':
	unittest.main()
