#!/usr/bin/python
# Filename: test_TargetResolver.py
# Description: Test cases for the own-ship/target-ship terms (COS.026)

import os, unittest

import numpy as np

from tests.maritime.model.risk.test_ConcernWeights import source_module, CONFIG

TargetResolver	= source_module( 'maritime.model.resolver.TargetResolver' ).TargetResolver
Resolver		= source_module( 'maritime.regulation.colreg.Resolver' ).Resolver
RuleContext		= source_module( 'cos.model.rule.Context' ).Context
Situation		= source_module( 'cos.model.rule.Situation' ).Situation
Binding			= source_module( 'rules.examiner.risk.RiskModel' ).Binding


class Vessel:
	def __init__(self, name, location, velocity, intent=()):
		self.id			= name
		self.name		= name
		self.location	= np.array( location, dtype=float )
		self.velocity	= np.array( velocity, dtype=float )
		self.intent		= list( intent )
		self.config		= {'name': name, 'identifier': {'imo': 1}}
		self.fleet		= None


class Log:
	def __init__(self):
		self.warnings	= []
	def warning(self, module, text):
		self.warnings.append( text )
	def error(self, *args):
		pass
	info	= trace	= error


class Ctxt:
	def __init__(self, weather='clearsky'):
		root	= CONFIG
		class Config:
			env	= {'WEATHER': weather}
			@staticmethod
			def resolve(path):
				return path.replace( '$(CONFIG)', root )
		class FS:
			@staticmethod
			def read_file_as_bytes(path):
				return open( path, 'rb' ).read()
		class Objects:
			@staticmethod
			def get_all(path):
				return []
		class Sim:
			config	= Config
			fs		= FS
			objects	= Objects
		self.sim	= Sim()
		self.log	= Log()


def resolver(os_, ts, weather='clearsky'):
	r			= TargetResolver()
	ctxt		= Ctxt( weather )
	r.init( ctxt, {'config': 'collision.dcpa=100'} )

	class Rule:
		situation	= Situation( os_, ts )
	r.reset( ctxt, Rule() )
	return r, ctxt


class GeometryTestCase(unittest.TestCase):
	def test_reciprocal_offset_100_gives_dcpa_100_and_tcpa_range_over_closing_speed(self):
		r, _	= resolver( Vessel('OS', (0, 0), (5, 0)), Vessel('TS', (1000, 100), (-5, 0)) )
		self.assertAlmostEqual( r.DCPA(), 100.0 )
		self.assertAlmostEqual( r.TCPA(), 1000.0 / 10.0 )
		self.assertAlmostEqual( r.TimeToEncounter(), r.TCPA() )
		self.assertAlmostEqual( r.ClosestApproachPoint(), 100.0 )

	def test_opening_pair_has_passed_its_cpa(self):
		r, _	= resolver( Vessel('OS', (0, 0), (-5, 0)), Vessel('TS', (1000, 100), (5, 0)) )
		self.assertEqual( r.TCPA(), 0.0 )
		self.assertAlmostEqual( r.DCPA(), float(np.hypot(1000, 100)) )
		self.assertFalse( r.OnCollisionCourse() )

	def test_collision_course_needs_closing_and_a_small_dcpa(self):
		near, _	= resolver( Vessel('OS', (0, 0), (5, 0)), Vessel('TS', (1000, 50), (-5, 0)) )
		wide, _	= resolver( Vessel('OS', (0, 0), (5, 0)), Vessel('TS', (1000, 150), (-5, 0)) )
		self.assertTrue( near.OnCollisionCourse() )
		self.assertFalse( wide.OnCollisionCourse() )

	def test_terms_depend_on_the_vessels(self):
		a, _	= resolver( Vessel('OS', (0, 0), (5, 0)), Vessel('TS', (1000, 50), (-5, 0)) )
		b, _	= resolver( Vessel('OS', (0, 0), (5, 0)), Vessel('TS', (500, 300), (-2, 0)) )
		self.assertNotEqual( (a.DCPA(), a.TCPA()), (b.DCPA(), b.TCPA()) )

	def test_bearing_sectors_with_y_south(self):
		os_	= Vessel( 'OS', (0, 0), (5, 0) )			# heading east
		cases	= { (100, 0): 'Position.Ahead', (0, 100): 'Position.Starboard',
					(0, -100): 'Position.Port', (-100, 0): 'Position.Astern' }
		for location, expected in cases.items():
			r, _	= resolver( os_, Vessel('TS', location, (0, 0)) )
			self.assertEqual( r.Position(), expected, location )
			self.assertEqual( r.Direction(), expected )

	def test_detect_reports_the_targets_signals(self):
		r, _	= resolver( Vessel('OS', (0, 0), (5, 0)), Vessel('TS', (100, 0), (0, 0), ['Signal.FogHorn']) )
		self.assertEqual( r.Detect(), ['Signal.FogHorn'] )

	def test_no_target_gives_no_value(self):
		r, _	= resolver( Vessel('OS', (0, 0), (5, 0)), None )
		self.assertFalse( r.is_valid() )
		for term in (r.DCPA, r.TCPA, r.OnCollisionCourse, r.Visible, r.Position, r.Detect):
			self.assertIsNone( term() )


class VisibilityTestCase(unittest.TestCase):
	def test_clear_weather_is_visible(self):
		r, _	= resolver( Vessel('OS', (0, 0), (5, 0)), Vessel('TS', (1000, 0), (-5, 0)), 'clearsky' )
		self.assertEqual( r.Visibility(), 15.0 )
		self.assertTrue( r.Visible() )

	def test_fog_hides_a_kilometre(self):
		r, _	= resolver( Vessel('OS', (0, 0), (5, 0)), Vessel('TS', (1000, 0), (-5, 0)), 'foggy' )
		self.assertAlmostEqual( r.Visibility(), (0.03 + 0.5) / 2 )
		self.assertFalse( r.Visible() )

	def test_unknown_weather_falls_back_and_says_so(self):
		r, ctxt	= resolver( Vessel('OS', (0, 0), (5, 0)), Vessel('TS', (1000, 0), (-5, 0)), 'nosuchweather' )
		self.assertEqual( r.Visibility(), 10.0 )
		self.assertTrue( ctxt.log.warnings )


class IntegrationTestCase(unittest.TestCase):
	def test_terms_resolve_through_the_composite_resolver(self):
		ctxt		= Ctxt( 'clearsky' )
		composite	= Resolver()
		composite.init( ctxt, '$(CONFIG)/legata.yaml' )
		os_, ts		= Vessel('OS', (0, 0), (5, 0)), Vessel('TS', (1000, 50), (-5, 0))
		rule_ctxt	= RuleContext( ctxt, composite, None, [os_, ts], None )
		rule_ctxt.situation	= Situation( os_, ts )
		composite.reset( ctxt, rule_ctxt )

		self.assertAlmostEqual( rule_ctxt.resolve('(OwnShip,TargetShip).DCPA'), 50.0 )
		self.assertTrue( rule_ctxt.resolve('(OwnShip,TargetShip).OnCollisionCourse') )
		self.assertTrue( rule_ctxt.resolve('(OwnShip,TargetShip).Visible') )

	def test_risk_binding_reads_collision_course_as_a_state(self):
		self.assertEqual( Binding({'discretize': 'state'}).discretize(True), 'yes' )
		self.assertEqual( Binding({'discretize': 'bins', 'width': 20.0, 'count': 10}).discretize(100.0), 'state_6' )


if __name__ == '__main__':
	unittest.main()
