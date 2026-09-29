#!/usr/bin/python
# Filename: test_Rule13.py
# Description: Test cases for COLREG Rule 13, overtaking (COS.022)

import unittest

from tests.maritime.model.colreg.colreg_harness import Vessel, encounter, judge, source_module

Rule13		= source_module( 'rules.colreg.rule13.Rule13' ).Rule13


def overtake(offset):
	""" Own ship coming up from astern at 10 m/s on a ship making 5 m/s, offset abeam by some metres """
	return Vessel( 'OS', (0.0, 0.0), (10.0, 0.0) ), Vessel( 'TS', (1000.0, offset), (5.0, 0.0) )


class Rule13TestCase(unittest.TestCase):
	def test_an_overtaking_encounter_is_queued_once_past_the_closest_approach(self):
		situation	= encounter( Rule13(), *overtake(50.0) )
		self.assertIsNotNone( situation )
		self.assertIn( 'Overtaking', situation.maneuvers )

	def test_passing_too_close_violates(self):
		self.assertEqual( judge('Rule13', encounter(Rule13(), *overtake(50.0))), ['COLREG.Rule13.a'] )

	def test_passing_well_clear_complies(self):
		self.assertEqual( judge('Rule13', encounter(Rule13(), *overtake(300.0))), [] )

	def test_no_risk_of_collision_is_not_an_encounter(self):
		self.assertIsNone( encounter(Rule13(), *overtake(800.0)) )

	def test_being_overtaken_is_not_judged(self):
		own, target	= overtake( 50.0 )
		self.assertIsNone( encounter(Rule13(), target, own) )


if __name__ == '__main__':
	unittest.main()
