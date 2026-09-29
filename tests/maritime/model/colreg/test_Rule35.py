#!/usr/bin/python
# Filename: test_Rule35.py
# Description: Test cases for COLREG Rule 35, sound signals in restricted visibility (COS.022)

import unittest

from tests.maritime.model.colreg.colreg_harness import Vessel, Situation, Type, Status, Operation, judge

FOG, CLEAR	= 1.0, 10.0		# Visibility, nautical miles


def vessel(velocity=(5.0, 0.0), signal=False, **kwargs):
	own	= Vessel( 'OS', (0.0, 0.0), velocity, **kwargs )
	own.intent.set( 'Signal.FogHorn' ) if signal else None
	return Situation( own, None )


class Rule35TestCase(unittest.TestCase):
	def test_making_way_in_fog_without_a_signal_violates_a(self):
		self.assertEqual( judge('Rule35', vessel(), FOG), ['COLREG.Rule35.a'] )

	def test_sounding_the_fog_signal_complies(self):
		self.assertEqual( judge('Rule35', vessel(signal=True), FOG), [] )

	def test_good_visibility_needs_no_signal(self):
		self.assertEqual( judge('Rule35', vessel(), CLEAR), [] )

	def test_underway_but_stopped_violates_b(self):
		self.assertEqual( judge('Rule35', vessel(velocity=(0.0, 0.0)), FOG), ['COLREG.Rule35.b'] )

	def test_a_sailing_vessel_is_judged_under_c_not_a(self):
		self.assertEqual( judge('Rule35', vessel(type=Type.SAILING), FOG), ['COLREG.Rule35.c'] )

	def test_a_fishing_power_driven_vessel_is_judged_under_c_not_a(self):
		self.assertEqual( judge('Rule35', vessel(operation=Operation.FISHING), FOG), ['COLREG.Rule35.c'] )

	def test_an_anchored_vessel_is_not_judged_under_a_to_c(self):
		self.assertEqual( judge('Rule35', vessel(velocity=(0.0, 0.0), status=Status.ANCHORED), FOG), [] )


if __name__ == '__main__':
	unittest.main()
