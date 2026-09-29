#!/usr/bin/python
# Filename: test_SpawnCheck.py
# Description: Test cases for the warning on a vessel that spawns in collision (COS-012 item 4)

from cos.model.environment.Actors import Actors

import unittest
from types import SimpleNamespace
from unittest import mock


class BrownianMotionBehavior:
	pass

class NavalFleet:
	pass


def vessel(motion, name='X100'):
	rect	= SimpleNamespace( left=510, top=210 )
	return SimpleNamespace( boundary=rect, motion=motion, config={'name': name}, id='guid' )


class SpawnCheckTestCase(unittest.TestCase):
	def check(self, v, blocked):
		actors			= Actors.__new__( Actors )
		actors.world	= SimpleNamespace( has_collision=lambda rect: blocked )
		ctxt			= mock.Mock()
		actors.check_spawn( ctxt, v )
		return ctxt.log.warning

	def test_vessel_on_land_is_warned(self):
		warning	= self.check( vessel(BrownianMotionBehavior()), True )
		warning.assert_called_once()
		self.assertIn( 'X100 starts in collision at (510, 210)', warning.call_args[0][1] )

	def test_vessel_on_water_is_silent(self):
		self.check( vessel(BrownianMotionBehavior()), False ).assert_not_called()

	def test_fleet_controller_is_skipped(self):
		self.check( vessel(NavalFleet()), True ).assert_not_called()

	def test_vessel_without_motion_is_skipped(self):
		self.check( vessel(None), True ).assert_not_called()


if __name__ == '__main__':
	unittest.main()
