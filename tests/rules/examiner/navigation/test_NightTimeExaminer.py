#!/usr/bin/python
# Filename: test_NightTimeExaminer.py
# Description: Test cases for the NightTimeExaminer class: night follows the scenario clock (COS.024)

import types, unittest

from cos.core.time.Clock import Clock
from rules.examiner.navigation.NightTimeExaminer import NightTimeExaminer
from maritime.model.vessel.Vessel import Vessel


def context(epoch):
	clock	= Clock( 60.0, epoch )
	sim		= types.SimpleNamespace( clock=clock, localtime=lambda: clock.local, now=lambda: clock.utc )
	return types.SimpleNamespace( sim=sim ), clock


def vessel():
	config	= { 'name': 'A', 'identifier': {'imo': '1', 'mmsi': '2'}, 'weight': 1.0, 'length': [10, 5, -1],
				'pose': {'position': [0, 0, 0], 'X': [0]*12, 'R': [0]*12} }
	return Vessel( types.SimpleNamespace(log=None, sim=None), 'Vessel', 'A', config )


LIGHTS	= ['masthead', 'sidelights', 'sternlight']


def examiner():
	return NightTimeExaminer.__new__( NightTimeExaminer )		# The night test needs no configuration


class NightTimeExaminerTestCase(unittest.TestCase):
	def test_a_scenario_starting_at_21_needs_lights(self):
		ctxt, clock	= context( '2026-06-01T21:00:00+03:00' )
		self.assertEqual( NightTimeExaminer.hour(ctxt), 21 )
		self.assertTrue( examiner().is_night(ctxt, {}) )

	def test_night_ends_on_the_scenario_clock(self):
		ctxt, clock	= context( '2026-06-01T05:00:00+03:00' )
		self.assertTrue( examiner().is_night(ctxt, {}) )
		for _ in range(60):		# One simulated hour at 60 s per tick
			clock.advance()
		self.assertFalse( examiner().is_night(ctxt, {}) )

	def test_the_night_is_dated_by_the_evening_it_began(self):
		ctxt, clock	= context( '2026-06-02T02:00:00+03:00' )
		self.assertEqual( examiner().night(ctxt, {}), '2026-06-01' )

	def test_a_vessel_declaring_no_light_intent_shows_none(self):
		self.assertEqual( NightTimeExaminer.missing(vessel(), LIGHTS), LIGHTS )

	def test_a_light_counts_once_its_intent_is_set(self):
		v	= vessel()
		v.signal( 'Light', 'masthead', True )
		v.signal( 'Light', 'sidelights', True )
		self.assertEqual( NightTimeExaminer.missing(v, LIGHTS), ['sternlight'] )

		v.signal( 'Light', 'sidelights', False )
		self.assertEqual( NightTimeExaminer.missing(v, LIGHTS), ['sidelights', 'sternlight'] )

if __name__ == '__main__':
    unittest.main()
