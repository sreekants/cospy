#!/usr/bin/python
# Filename: test_Runner.py
# Description: Test cases for the Runner: faculty affinity, the clock and snapshots (COS.040, COS.024)

import time, types, unittest

import numpy as np

from cos.core.kernel.ObjectManager import ObjectManager
from cos.core.kernel.ObjectManager import ObjectType
from cos.core.simulation.Runner import Runner, Affinity
from cos.core.simulation.Snapshot import Snapshot
from cos.core.time.Clock import Clock
from cos.model.vehicle.Vehicle import Vehicle

AFFINITY	= 'Motion:Subsystem|Rules:Rules'


class Config:
	def __init__(self, affinity=None, cycles=-1):
		self.values	= {'RunCycles': str(cycles)}
		if affinity is not None:
			self.values['Affinity']	= affinity
	def exists_value(self, section, key):
		return key in self.values
	def get_value(self, section, key):
		return self.values[key]
	def get_int(self, section, key):
		return int(self.values[key])


class Log:
	def __init__(self):
		self.lines	= []
	def info(self, module, text):
		self.lines.append( text )
	debug	= error	= warning	= info


class Actor:
	def __init__(self):
		self.x, self.dx, self.d2x, self.rect	= np.zeros(3), np.zeros(3), np.zeros(3), None
	def get_position(self):
		return self.x


class Boat:
	""" Stands in for a vehicle: the Vehicle properties read its actor """
	def __init__(self):
		self.guid	= 'boat'
		self.actor	= Actor()
	location	= Vehicle.location


class Motion:
	def __init__(self, sim, boat):
		self.sim, self.boat	= sim, boat
		self.stamps			= []
	def on_timer(self, ctxt, unused):
		tick	= self.sim.clock.tick
		self.boat.actor.x	= np.array( (float(tick), 0.0, 0.0) )
		Snapshot.publish( Snapshot.capture(tick, [self.boat]) )
		self.stamps.append( (tick, time.perf_counter()) )


class Rules:
	def __init__(self, sim, boat, work):
		self.sim, self.boat, self.work	= sim, boat, work
		self.passes		= []
	def on_timer(self, ctxt, unused):
		first	= ( self.sim.clock.tick, float(self.boat.location[0]) )
		end		= time.perf_counter() + self.work
		while time.perf_counter() < end:		# CPU-bound, as rule evaluation is
			pass
		last	= ( self.sim.clock.tick, float(self.boat.location[0]) )
		self.passes.append( (first, last, self.sim.clock.live) )


def simulation(affinity, work=0.3):
	sim			= types.SimpleNamespace()
	sim.config	= Config( affinity )
	sim.log		= Log()
	sim.clock	= Clock()
	sim.objects	= ObjectManager()
	sim.ipc		= None
	boat		= Boat()

	sim.objects.faculty	= 'Subsystem'
	motion		= Motion( sim, boat )
	sim.objects.register( '/Services/Kernel', 'Motion', motion )
	sim.objects.faculty	= 'Rules'
	rules		= Rules( sim, boat, work )
	sim.objects.register( '/Services/Regulation', 'Rules', rules )
	sim.objects.faculty	= None
	return sim, motion, rules


def run(sim, seconds):
	runner	= Runner()
	runner.run( sim )
	time.sleep( seconds )
	runner.stop()
	return runner


class AffinityTestCase(unittest.TestCase):
	def test_first_group_runs_its_faculties_and_every_unnamed_one(self):
		a	= Affinity( AFFINITY )
		self.assertTrue( a.owns(0, 'Subsystem') )
		self.assertTrue( a.owns(0, None) )
		self.assertTrue( a.owns(0, 'Environment') )
		self.assertFalse( a.owns(0, 'Rules') )
		self.assertTrue( a.owns(1, 'Rules') )
		self.assertFalse( a.owns(1, 'Subsystem') )
		self.assertFalse( a.owns(1, None) )

	def test_no_setting_is_one_group_that_runs_everything(self):
		a	= Affinity( None )
		self.assertEqual( len(a.groups), 1 )
		self.assertTrue( a.owns(0, 'Rules') )
		self.assertTrue( a.owns(0, None) )


class RunnerTestCase(unittest.TestCase):
	def setUp(self):
		Snapshot.reset()
		self.addCleanup( Snapshot.reset )

	def test_motion_does_not_wait_for_a_slow_rule_pass(self):
		sim, motion, rules	= simulation( AFFINITY, work=0.3 )
		run( sim, 2.0 )

		gaps	= np.diff( [t for _, t in motion.stamps] )
		self.assertGreater( len(rules.passes), 2 )
		self.assertGreater( len(motion.stamps), 20 )
		self.assertLess( float(np.max(gaps)), 0.1 )

	def test_a_pass_reads_one_tick_and_that_ticks_positions(self):
		sim, motion, rules	= simulation( AFFINITY, work=0.3 )
		run( sim, 1.5 )

		for first, last, live in rules.passes:
			self.assertEqual( first, last )				# Motion moved on, the pass did not
			self.assertEqual( first[0], first[1] )		# The boat's x is its tick
			self.assertGreater( live, first[0] )		# Motion ran ahead during the pass

	def test_passes_skip_the_ticks_in_between(self):
		sim, motion, rules	= simulation( AFFINITY, work=0.3 )
		run( sim, 1.5 )

		judged	= [first[0] for first, _, _ in rules.passes]
		self.assertTrue( all(b - a > 1 for a, b in zip(judged, judged[1:])) )
		self.assertTrue( any('lag mean' in line for line in sim.log.lines) )

	def test_without_affinity_every_service_runs_each_tick_in_order(self):
		sim, motion, rules	= simulation( None, work=0.0 )
		run( sim, 0.5 )

		ticks	= [t for t, _ in motion.stamps]
		judged	= [first[0] for first, _, _ in rules.passes]
		self.assertEqual( judged, ticks )
		self.assertEqual( ticks, list(range(1, len(ticks)+1)) )


class SnapshotTestCase(unittest.TestCase):
	def tearDown(self):
		Snapshot.pin( None )
		Snapshot.reset()

	def test_a_capture_is_a_copy(self):
		boat	= Boat()
		boat.actor.x	= np.array( (1.0, 2.0, 0.0) )
		snap	= Snapshot.capture( 7, [boat] )
		boat.actor.x[0]	= 99.0

		self.assertEqual( snap.states['boat'].x[0], 1.0 )

	def test_vehicles_read_the_pinned_snapshot_and_live_state_otherwise(self):
		boat	= Boat()
		boat.actor.x	= np.array( (1.0, 0.0, 0.0) )
		Snapshot.pin( Snapshot.capture(1, [boat]) )
		boat.actor.x	= np.array( (5.0, 0.0, 0.0) )

		self.assertEqual( boat.location[0], 1.0 )
		Snapshot.pin( None )
		self.assertEqual( boat.location[0], 5.0 )

if __name__ == '__main__':
    unittest.main()
