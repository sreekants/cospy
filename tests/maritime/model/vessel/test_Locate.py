#!/usr/bin/python
# Filename: test_Locate.py
# Description: Test cases for Vessel.locate_at: a swarm move is seen by location and the rule snapshots

import types, unittest
import numpy as np

from maritime.model.vessel.Vessel import Vessel
from cos.math.geometry.Rectangle import Rectangle
from cos.core.simulation.Snapshot import Snapshot
from cos.behavior.motion.PreyBehavior import PreyAdapter, WorldAdapter
from cos.behavior.swarm.Prey import Config as PreyConfig
from cos.behavior.swarm.Predator import Config as PredatorConfig
from cos.behavior.swarm.Swarm import Swarm
from cos.math.geometry.Point import Point
from cos.math.geometry.Vector import Vector


def vessel(name, x, y):
	config	= { 'name': name, 'identifier': {'imo': '1', 'mmsi': '2'}, 'weight': 1.0, 'length': [10, 5, -1],
				'pose': {'position': [x, y, 0], 'X': [0]*12, 'R': [0]*12} }
	v	= Vessel( types.SimpleNamespace(log=None, sim=None), 'Vessel', name, config )
	v.actor.rect	= Rectangle( x-10, y-5, 20, 10 )
	return v


class OpenSea:
	def has_collision(self, rect):
		return False


class LocateTestCase(unittest.TestCase):
	def test_locate_at_moves_the_location(self):
		v	= vessel( 'A', 0, 0 )
		v.locate_at( [120.0, 80.0, 0] )
		np.testing.assert_allclose( v.location, [120.0, 80.0, 0.0] )
		self.assertEqual( v.boundary.center, Rectangle(110, 75, 20, 10).center )

	def test_a_swarm_step_is_seen_by_location_and_snapshot(self):
		members	= [ vessel('A', 1000, 1000), vessel('B', 1030, 1000), vessel('C', 1000, 1030) ]
		preys	= [ PreyAdapter( Point(1000, 1000), Vector(1, 0), members[0] ),
					PreyAdapter( Point(1030, 1000), Vector(1, 0), members[1] ),
					PreyAdapter( Point(1000, 1030), Vector(1, 0), members[2] ) ]
		cfg			= PreyConfig()
		cfg.speed	= 5.0

		swarm	= Swarm()
		swarm.setPreys( cfg, preys )
		swarm.setPredators( PredatorConfig(), [] )		# As PreyBehavior does for a fleet with no predators
		swarm.move( WorldAdapter(OpenSea()) )

		for prey, v in zip( preys, members ):
			np.testing.assert_allclose( v.location[:2], [prey.pos.x, prey.pos.y] )

		self.assertFalse( np.allclose(members[0].location[:2], [1000, 1000]) )		# It moved

		snapshot	= Snapshot.capture( 1, members )
		for v in members:
			np.testing.assert_allclose( snapshot.states[v.guid].x, v.location )

if __name__ == '__main__':
    unittest.main()
