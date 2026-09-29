#!/usr/bin/python
# Filename: test_Rule14.py
# Description: Test cases for COLREG Rule 14, head-on (COS.022)

import os, datetime, queue, unittest

import numpy as np

from tests.maritime.model.risk.test_ConcernWeights import source_module, CONFIG

Rule14			= source_module( 'rules.colreg.rule14.Rule14' ).Rule14
passing_side	= source_module( 'maritime.model.resolver.ColregResolver' ).passing_side
Resolver		= source_module( 'maritime.regulation.colreg.Resolver' ).Resolver
Automata		= source_module( 'cos.model.rule.Automata' ).Automata
RuleContext		= source_module( 'cos.model.rule.Context' ).Context
Situation		= source_module( 'cos.model.rule.Situation' ).Situation

LEGATA	= os.path.join( CONFIG, 'maritime', 'regulation', 'colreg', 'Rule14.legata' )


class Vessel:
	def __init__(self, name, location, velocity):
		self.id			= name
		self.name		= name
		self.location	= np.array( location, dtype=float )
		self.velocity	= np.array( velocity, dtype=float )
		self.config		= {'name': name, 'identifier': {'imo': 1}}
		self.fleet		= None
		self.boundary	= None

	@property
	def heading(self):
		return float( np.degrees(np.arctan2(self.velocity[1], self.velocity[0])) )

	def step(self, dt):
		self.location	= self.location + self.velocity * dt


class Log:
	def error(self, *args):
		pass
	info	= trace	= warning	= error


class Sim:
	def __init__(self):
		self.clock	= datetime.datetime( 2026, 9, 25, 12, 0, 0 )
	def now(self):
		return self.clock
	class fs:
		@staticmethod
		def read_file_as_bytes(path):
			return open( path, 'rb' ).read()
	class config:
		@staticmethod
		def resolve(path):
			return path.replace( '$(CONFIG)', CONFIG )
	class objects:
		@staticmethod
		def get_all(path):
			return []


class Ctxt:
	def __init__(self):
		self.sim	= Sim()
		self.log	= Log()


def meeting(offset):
	""" Two ships on reciprocal courses east/west, 2 km apart; offset > 0 puts TS south of OS's track """
	return Vessel( 'OS', (0, 0), (5, 0) ), Vessel( 'TS', (2000, offset), (-5, 0) )


class GeometryTestCase(unittest.TestCase):
	def test_reciprocal_courses_ahead_closing_is_head_on(self):
		os_, ts	= meeting( 50 )
		self.assertTrue( Rule14.head_on(os_, ts, 13, 500, 4000) )

	def test_crossing_is_not_head_on(self):
		os_, ts	= Vessel( 'OS', (0, 0), (5, 0) ), Vessel( 'TS', (1000, -1000), (0, 5) )
		self.assertFalse( Rule14.head_on(os_, ts, 13, 500, 4000) )

	def test_formation_is_not_head_on(self):
		os_, ts	= Vessel( 'OS', (0, 0), (5, 0) ), Vessel( 'TS', (100, 0), (5, 0) )
		self.assertFalse( Rule14.head_on(os_, ts, 13, 500, 4000) )

	def test_opening_range_is_not_head_on(self):
		os_, ts	= Vessel( 'OS', (0, 0), (-5, 0) ), Vessel( 'TS', (2000, 0), (5, 0) )
		self.assertFalse( Rule14.head_on(os_, ts, 13, 500, 4000) )

	def test_wide_passing_distance_is_no_risk_of_collision(self):
		os_, ts	= meeting( 450 )
		self.assertFalse( Rule14.head_on(os_, ts, 13, 100, 4000) )

	def test_beyond_range_is_not_recorded(self):
		os_, ts	= meeting( 50 )
		self.assertFalse( Rule14.head_on(os_, ts, 13, 500, 1000) )

	def test_coincident_vessels_do_not_raise(self):
		os_, ts	= Vessel( 'OS', (10, 10), (5, 0) ), Vessel( 'TS', (10, 10), (-5, 0) )
		self.assertFalse( Rule14.head_on(os_, ts, 13, 500, 4000) )
		self.assertEqual( Rule14.between(np.zeros(2), np.array([1.0, 0.0])), 180.0 )

	def test_passing_side_with_y_south(self):
		os_	= Vessel( 'OS', (0, 0), (5, 0) )		# heading east
		self.assertEqual( passing_side(os_, Vessel('TS', (0, 10), (0, 0))), 'Starboard' )	# south
		self.assertEqual( passing_side(os_, Vessel('TS', (0, -10), (0, 0))), 'Port' )		# north


class LegataTestCase(unittest.TestCase):
	def judge(self, os_, ts, head_on):
		ctxt		= Ctxt()
		resolver	= Resolver()
		resolver.init( ctxt, '$(CONFIG)/legata.yaml' )
		automata	= Automata( None )
		automata.load( LEGATA )

		rule_ctxt	= RuleContext( ctxt, resolver, None, [os_, ts], None )
		rule_ctxt.situation	= Situation( os_, ts )
		if head_on:
			rule_ctxt.situation.maneuvers['HeadOn']	= ctxt.sim.now()
		resolver.reset( ctxt, rule_ctxt )

		result	= automata.evaluate( rule_ctxt )
		return sorted( { e.parent.name for e in (result.error or []) } )

	def test_port_to_port_complies(self):
		os_, ts	= Vessel( 'OS', (0, 0), (5, 0) ), Vessel( 'TS', (0, -60), (-5, 0) )
		self.assertEqual( self.judge(os_, ts, True), [] )

	def test_starboard_to_starboard_violates(self):
		os_, ts	= Vessel( 'OS', (0, 0), (5, 0) ), Vessel( 'TS', (0, 60), (-5, 0) )
		self.assertEqual( self.judge(os_, ts, True), ['COLREG.Rule14.a'] )

	def test_not_head_on_is_not_judged(self):
		os_, ts	= Vessel( 'OS', (0, 0), (5, 0) ), Vessel( 'TS', (0, 60), (-5, 0) )
		self.assertEqual( self.judge(os_, ts, False), [] )


class ObserveTestCase(unittest.TestCase):
	def rule(self):
		rule			= Rule14.__new__( Rule14 )
		rule.angle		= Rule14.ANGLE
		rule.range		= Rule14.RANGE
		rule.dcpa		= Rule14.DCPA
		rule.onsets		= {}
		rule.sitations	= queue.Queue()
		return rule

	class RuleContext:
		def __init__(self, vessels, subjects=None):
			self.vessels	= vessels
			self.subjects	= subjects or vessels

	def encounter(self, offset):
		rule, ctxt	= self.rule(), Ctxt()
		os_, ts		= meeting( offset )
		queued		= []
		for _ in range(400):		# 2 s passes, 800 s: well past the closest approach
			rule.observe( ctxt, self.RuleContext([os_, ts], [os_]) )
			while not rule.sitations.empty():
				queued.append( rule.sitations.get() )
			os_.step( 2 ); ts.step( 2 )
		return rule, queued

	def test_one_judgement_per_encounter_after_cpa(self):
		rule, queued	= self.encounter( -50 )
		self.assertEqual( len(queued), 1 )
		self.assertIn( 'HeadOn', queued[0].maneuvers )
		self.assertEqual( passing_side(queued[0].os, queued[0].ts), 'Port' )
		self.assertEqual( rule.onsets, {} )

	def test_starboard_pass_is_queued_on_the_starboard_side(self):
		rule, queued	= self.encounter( 50 )
		self.assertEqual( len(queued), 1 )
		self.assertEqual( passing_side(queued[0].os, queued[0].ts), 'Starboard' )

	def test_only_vessels_under_test_are_judged(self):
		rule, ctxt	= self.rule(), Ctxt()
		os_, ts		= meeting( 50 )
		rule.observe( ctxt, self.RuleContext([os_, ts], [os_]) )
		self.assertEqual( list(rule.onsets), [('OS', 'TS')] )


if __name__ == '__main__':
	unittest.main()
