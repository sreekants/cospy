#!/usr/bin/python
# Filename: test_SwarmConfig.py
# Description: Test cases for loading swarm settings from swarm.yaml

import math, os, unittest
from unittest import mock

from cos.behavior.swarm.Prey import Config as PreyConfig
from cos.behavior.swarm.Predator import Config as PredatorConfig
from cos.behavior.motion.FleetBehavior import FleetBehavior
from cos.behavior.motion.PreyBehavior import PreyBehavior

SWARM	= b'''
prey:
  speed: 12.0
  maxTurnAngle: 3.0
  minSeparation: 60.0
predator:
  speed: 14.0
  killDist: 25.0
'''
SHIPPED	= '/home/ssreedharan/projects/cos-data/config/vehicle/fleet/swarm.yaml'


def context(data=SWARM):
	ctxt	= mock.Mock()
	ctxt.sim.config.resolve.side_effect	= lambda p: p
	ctxt.sim.fs.read_file_as_bytes.return_value	= data
	return ctxt


def configs(behavior):
	return { kind: cfg for kind, cfg, _, _ in behavior.swarm.groups }


class SwarmConfigTestCase(unittest.TestCase):
	def test_load_overrides_named_values_and_converts_degrees(self):
		cfg	= PreyConfig().load( {'speed': 12, 'maxTurnAngle': 3.0} )
		self.assertEqual( cfg.speed, 12.0 )
		self.assertAlmostEqual( cfg.maxTurnAngle, math.radians(3.0) )
		self.assertEqual( cfg.minSeparation, 18.0 )				# untouched default

	def test_unknown_setting_is_refused(self):
		with self.assertRaises( ValueError ):
			PreyConfig().load( {'sped': 12} )
		with self.assertRaises( ValueError ):
			PredatorConfig().load( {'cohesion': 1.0} )			# a prey-only setting

	def test_empty_section_keeps_defaults(self):
		self.assertEqual( PredatorConfig().load(None).killDist, 10.0 )


class PreyBehaviorSwarmTestCase(unittest.TestCase):
	def initialize(self, settings, data=SWARM):
		b	= PreyBehavior( None, {} )
		with mock.patch.object( FleetBehavior, 'intialize' ):
			b.intialize( context(data), None, None, {'settings': settings} )
		return b

	def test_without_swarm_setting_speeds_stay_at_half_a_metre(self):
		c	= configs( self.initialize('membership=fleet1.csv') )
		self.assertEqual( c['prey'].speed, 0.5 )
		self.assertEqual( c['predator'].speed, 0.5 )

	def test_swarm_setting_loads_both_sections(self):
		c	= configs( self.initialize('membership=fleet1.csv swarm=$(CONFIG)/vehicle/fleet/swarm.yaml') )
		self.assertEqual( c['prey'].speed, 12.0 )
		self.assertEqual( c['prey'].minSeparation, 60.0 )
		self.assertAlmostEqual( c['prey'].maxTurnAngle, math.radians(3.0) )
		self.assertEqual( c['predator'].speed, 14.0 )
		self.assertEqual( c['predator'].killDist, 25.0 )

	@unittest.skipUnless( os.path.exists(SHIPPED), 'cos-data checkout not present' )
	def test_shipped_swarm_yaml_reproduces_the_previous_behaviour(self):
		c	= configs( self.initialize('swarm=x', open(SHIPPED, 'rb').read()) )
		self.assertEqual( c['prey'].speed, 0.5 )
		self.assertEqual( c['predator'].speed, 0.5 )
		for k in PreyConfig.FIELDS:
			self.assertAlmostEqual( getattr(c['prey'], k), getattr(PreyConfig(), k) if k != 'speed' else 0.5, msg=k )


if __name__ == '__main__':
	unittest.main()
