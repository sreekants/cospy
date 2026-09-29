#!/usr/bin/python
# Filename: test_BrownianMotion.py
# Description: Test cases for the Brownian rollback pair and vector aliasing (COS.012)

import unittest

import numpy as np

from cos.behavior.motion.BrownianMotionBehavior import BrownianMotionBehavior
from cos.behavior.motion.LinearMotionBehavior import LinearMotionBehavior
from cos.math.geometry.Rectangle import Rectangle


class World:
	def __init__(self, land):
		self.land	= land
	def has_collision(self, rect):
		return self.land


class Tick:
	timestep	= 1


def brownian(x, y, X=None, zone='100,300,900,400'):
	config	= { 'settings': f'zone={zone}',
				'pose': { 'position': (x, y, 0.0), 'X': X, 'R': None } }
	b		= BrownianMotionBehavior( None, config )
	b.init( Rectangle(x-10, y-5, 20, 10) )
	b.entropy	= 0
	return b


class BrownianMotionTestCase(unittest.TestCase):
	def test_blocked_first_move_outside_zone_does_not_raise(self):
		b	= brownian( 510, 210, X=(1.0, 1.0, 0.0, 0.0, 0.0, 0.0) )		# on land, outside the zone
		b.move( World(land=True), Tick(), None )
		self.assertEqual( b.rect, b.last )

	def test_first_move_on_water_outside_zone(self):
		b	= brownian( 510, 210, X=(1.0, 1.0, 0.0, 0.0, 0.0, 0.0) )
		b.move( World(land=False), Tick(), None )
		self.assertEqual( b.dx[1], 1.0 )			# turned back towards the zone below

	def test_first_move_on_land_inside_zone(self):
		b	= brownian( 510, 400, X=(1.0, 1.0, 0.0, 0.0, 0.0, 0.0) )
		b.move( World(land=True), Tick(), None )

	def test_lastdx_is_a_copy(self):
		b	= brownian( 510, 400, X=(1.0, 1.0, 0.0, 0.0, 0.0, 0.0) )
		b.move( World(land=False), Tick(), None )
		self.assertIsNot( b.lastdx, b.dx )
		b.limit_to( Rectangle(0, 0, 10, 10), b.x )
		self.assertIsNot( b.lastdx, b.dx )

	def test_default_vectors_are_not_shared(self):
		config	= { 'pose': { 'position': (0.0, 0.0, 0.0), 'X': None, 'R': None } }
		b		= LinearMotionBehavior( None, config )
		b.randomize_direction()
		self.assertTrue( np.any(b.dx) )
		for name in ('d2x', 'θ', 'dθ', 'lastdx'):
			self.assertFalse( np.any(getattr(b, name)), name )


if __name__ == '__main__':
	unittest.main()
