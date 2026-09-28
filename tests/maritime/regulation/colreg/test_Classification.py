#!/usr/bin/python
# Filename: test_Classification.py
# Description: Test cases for encounter classification (COS.025)

import math, os, unittest

from maritime.core.situation.Types import Encounter as Type
from maritime.regulation.colreg.Classification import Thresholds, THRESHOLDS, classify
from maritime.regulation.colreg.Encounter import Encounter
from maritime.model.resolver.ColregResolver import ColregResolver
from maritime.model.resolver.TargetResolver import TargetResolver
from cos.model.rule.Situation import Situation

ROOT	= os.path.abspath( os.path.join(os.path.dirname(__file__), '..', '..', '..', '..') )


class Vessel:
	def __init__(self, x, y, vx, vy):
		self.location	= (float(x), float(y), 0.0)
		self.velocity	= (float(vx), float(vy), 0.0)


def polar(bearing, distance):
	""" A map offset at a bearing measured clockwise from east; map y grows south """
	return distance*math.cos(math.radians(bearing)), distance*math.sin(math.radians(bearing))


class ClassificationTestCase(unittest.TestCase):
	def kind(self, own, target):
		return classify( own, target )[2]

	def test_reciprocal_courses_target_ahead_is_head_on(self):
		self.assertEqual( self.kind(Vessel(0, 0, 1, 0), Vessel(1000, 5, -1, 0)), Type.HO )

	def test_same_course_and_speed_is_not_head_on(self):
		self.assertEqual( self.kind(Vessel(0, 0, 1, 0), Vessel(100, 0, 1, 0)), Type.NAR )
		self.assertEqual( self.kind(Vessel(0, 0, 1, 0), Vessel(0, 50, 1, 0)), Type.NAR )
		self.assertEqual( Encounter.maneuver(Vessel(0, 0, 1, 0), Vessel(100, 0, 1, 0))[2], Type.NAR )

	def test_coming_up_from_abaft_the_beam_is_overtaking(self):
		x, y	= polar( 120.0, 200.0 )			# 30° abaft the target's starboard beam
		own		= Vessel( x, y, 3*math.cos(math.radians(-50)), 3*math.sin(math.radians(-50)) )
		target	= Vessel( 0, 0, 1, 0 )
		self.assertEqual( self.kind(own, target), Type.OTGW )
		self.assertEqual( self.kind(target, own), Type.OTSO )

	def test_forward_of_the_overtaking_sector_is_not_overtaking(self):
		x, y	= polar( 100.0, 200.0 )			# only 10° abaft the beam
		own		= Vessel( x, y, 3*math.cos(math.radians(-50)), 3*math.sin(math.radians(-50)) )
		self.assertNotEqual( self.kind(own, Vessel(0, 0, 1, 0)), Type.OTGW )

	def test_overtaking_needs_the_faster_vessel(self):
		self.assertEqual( self.kind(Vessel(0, 0, 2, 0), Vessel(500, 0, 1, 0)), Type.OTGW )
		self.assertEqual( self.kind(Vessel(500, 0, 1, 0), Vessel(0, 0, 2, 0)), Type.OTSO )

	def test_crossing_target_on_starboard_gives_way(self):
		own		= Vessel( 0, 0, 0, -1 )			# northbound
		target	= Vessel( 500, -500, -1, 0 )	# on the starboard bow, westbound
		α, β, kind	= classify( own, target )
		self.assertAlmostEqual( α, 45.0 )
		self.assertAlmostEqual( β, -45.0 )
		self.assertEqual( kind, Type.CRGW )
		self.assertEqual( self.kind(target, own), Type.CRSO )

	def test_opening_or_stationary_is_not_an_encounter(self):
		self.assertEqual( self.kind(Vessel(0, 0, -1, 0), Vessel(1000, 0, 1, 0)), Type.NAR )
		self.assertEqual( self.kind(Vessel(0, 0, 1, 0), Vessel(1000, 0, 0, 0)), Type.NAR )

	def test_defaults_match_evaluator_yaml(self):
		loaded	= Thresholds.load( os.path.join(ROOT, 'config', 'evaluator.yaml') )
		self.assertEqual( vars(loaded), vars(Thresholds()) )


class Parent:
	def __init__(self):
		self.target	= TargetResolver()
	def get(self, scope):
		return self.target if scope == 'target' else None


class RuleContext:
	def __init__(self, situation):
		self.situation	= situation


class EncounterSituationTestCase(unittest.TestCase):
	def resolve(self, own, target):
		resolver	= ColregResolver( Parent() )
		resolver.reset( None, RuleContext(Situation(own, target)) )
		return resolver.EncounterSituation()

	def test_resolves_without_raising(self):
		self.assertEqual( self.resolve(Vessel(0, 0, 1, 0), Vessel(1000, 5, -1, 0)), 'HeadOn' )
		self.assertEqual( self.resolve(Vessel(0, 0, 0, -1), Vessel(500, -500, -1, 0)), 'GiveWay' )
		self.assertEqual( self.resolve(Vessel(0, 0, 1, 0), Vessel(100, 0, 1, 0)), '' )

	def test_no_target_is_none(self):
		self.assertIsNone( self.resolve(Vessel(0, 0, 1, 0), None) )


if __name__ == '__main__':
	unittest.main()
