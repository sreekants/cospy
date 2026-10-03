#!/usr/bin/python
# Filename: test_VirtualWorld.py
# Description: Test cases for the CViz clock

import datetime, unittest

from cos.tools.cviz.VirtualWorld import VirtualWorld

OSLO	= datetime.timezone( datetime.timedelta(hours=2) )


class ClockTestCase(unittest.TestCase):
	def test_no_time_yet_shows_dashes(self):
		self.assertEqual( VirtualWorld.format_clock(None), '--:--:--' )

	def test_formats_day_of_month_hour_and_minute(self):
		t	= datetime.datetime( 2026, 6, 21, 21, 5, 59, tzinfo=OSLO )
		self.assertEqual( VirtualWorld.format_clock(t), '21:21:05' )

	def test_vessel_move_time_keeps_the_scenario_timezone(self):
		world	= VirtualWorld.__new__( VirtualWorld )
		world.groups	= {"vessel": []}
		world.sim_time	= None
		world.on_vessel_move( {"guid": "v1", "time": '2026-06-01T00:00:30+02:00'} )
		self.assertEqual( VirtualWorld.format_clock(world.sim_time), '01:00:00' )

	def test_vessel_move_without_time_keeps_the_clock(self):
		world	= VirtualWorld.__new__( VirtualWorld )
		world.groups	= {"vessel": []}
		world.sim_time	= None
		world.on_vessel_move( {"guid": "v1"} )
		self.assertIsNone( world.sim_time )


if __name__ == '__main__':
	unittest.main()
