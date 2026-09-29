#!/usr/bin/python
# Filename: test_Rule15.py
# Description: Test cases for COLREG Rule 15, crossing (COS.022)

import unittest

from tests.maritime.model.colreg.colreg_harness import Vessel, encounter, judge, source_module

Rule15			= source_module( 'rules.colreg.rule15.Rule15' ).Rule15
Rule13			= source_module( 'rules.colreg.rule13.Rule13' ).Rule13
EncounterWatch	= source_module( 'maritime.model.rule.EncounterWatch' ).EncounterWatch


def crossing(speed):
	""" Own ship eastbound; the other vessel on her starboard side (y grows south), northbound at 5 m/s """
	return Vessel( 'OS', (0.0, 0.0), (speed, 0.0) ), Vessel( 'TS', (1000.0, 1000.0), (0.0, -5.0) )


class Rule15TestCase(unittest.TestCase):
	def test_a_give_way_crossing_is_queued_once_past_the_closest_approach(self):
		situation	= encounter( Rule15(), *crossing(3.0) )
		self.assertIsNotNone( situation )
		self.assertIn( 'GiveWay', situation.maneuvers )

	def test_passing_astern_complies(self):
		self.assertEqual( judge('Rule15', encounter(Rule15(), *crossing(3.0))), [] )

	def test_crossing_ahead_violates(self):
		self.assertEqual( judge('Rule15', encounter(Rule15(), *crossing(7.0))), ['COLREG.Rule15/CrossAstern'] )

	def test_passing_too_close_violates(self):
		self.assertIn( 'COLREG.Rule15/KeepClear', judge('Rule15', encounter(Rule15(), *crossing(5.2))) )

	def test_the_stand_on_vessel_is_not_judged(self):
		own, target	= crossing( 3.0 )
		self.assertIsNone( encounter(Rule15(), target, own) )

	def test_an_encounter_keeps_the_role_it_began_with(self):
		own, target	= crossing( 3.0 )
		key			= ( own.id, target.id )
		self.addCleanup( EncounterWatch.roles.pop, key, None )
		EncounterWatch.roles[key]	= 'Overtaking'
		self.assertFalse( Rule15().watch.begins(own, target) )
		EncounterWatch.roles[key]	= 'GiveWay'
		self.assertTrue( Rule15().watch.begins(own, target) )


if __name__ == '__main__':
	unittest.main()
