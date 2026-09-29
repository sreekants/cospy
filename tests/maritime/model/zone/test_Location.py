#!/usr/bin/python
# Filename: test_Location.py
# Description: Test cases for the location settings and the nominal depth fallback (REQ.022)

import os, tempfile, shutil, unittest

from maritime.model.zone.Location import Location
from maritime.model.zone.ZoneAwareness import ZoneAware
from maritime.model.resolver.SeaResolver import SeaResolver
from tests.maritime.model.zone.test_Ledger import Ctxt, Shape, Vessel, CONFIG
from tests.maritime.model.zone.test_Practice import RuleContext as PracticeRuleContext
from tests.maritime.model.risk.test_ConcernWeights import source_module
from tests.maritime.model.risk.test_Rb import fields, report
from maritime.model.zone.ZoneRules import ZoneRules
from cos.subsystem.data.Partition import AUDIT_FIELDS

GroundingExaminer	= source_module( 'rules.examiner.navigation.GroundingExaminer' ).GroundingExaminer
BerthingExaminer	= source_module( 'rules.examiner.navigation.BerthingExaminer' ).BerthingExaminer
RiskExaminer		= source_module( 'rules.examiner.risk.RiskExaminer' ).RiskExaminer


class Grounder(ZoneAware):
	def __init__(self, ctxt, config=None):
		self.id		= 'Grounder'
		self.init_zones( ctxt, config or {'zones': None, 'territory': None} )
		self.cache_shapes( ctxt )
	def subscribe(self, method, handler):
		pass


class Seabed(Shape):
	def __init__(self, name, type, depth):
		Shape.__init__( self, name, type )
		self.nominal_depth	= depth


class Situation:
	def __init__(self, os_):
		self.os		= os_
		self.ts		= None


class RuleCtxt:
	def __init__(self, os_):
		self.situation	= Situation( os_ )


class LocationTestCase(unittest.TestCase):
	def setUp(self):
		Location._shared.clear()
		self.dir	= tempfile.mkdtemp()
		return

	def tearDown(self):
		Location._shared.clear()
		shutil.rmtree( self.dir, ignore_errors=True )
		return

	def write(self, text):
		path	= os.path.join( self.dir, 'location.yaml' )
		with open(path, 'w') as f:
			f.write( text )
		return path

	def test_location_file_declares_4000(self):
		location	= Location.shared( Ctxt() )
		self.assertEqual( location.nominal_depth, 4000.0 )
		self.assertEqual( location.path, os.path.join(CONFIG, 'simulation', 'tk', 'turkeli', 'location.yaml') )

	def test_loaded_once(self):
		self.assertIs( Location.shared(Ctxt()), Location.shared(Ctxt()) )

	def test_value_is_taken_from_the_file(self):
		path	= self.write( 'location:\n  depth:\n    nominal: 12.5\n' )
		self.assertEqual( Location.shared(Ctxt(), path).nominal_depth, 12.5 )

	def test_missing_file_or_value_is_fatal(self):
		with self.assertRaises( ValueError ):
			Location.shared( Ctxt(), os.path.join(self.dir, 'absent.yaml') )
		for text in ('location: {}\n', 'location:\n  depth:\n    nominal: 0\n',
					 'location:\n  depth:\n    nominal: -10\n', 'location:\n  depth:\n    nominal: true\n',
					 'location:\n  depth:\n    nominal: deep\n'):
			Location._shared.clear()
			with self.assertRaises( ValueError ):
				Location.shared( Ctxt(), self.write(text) )

	def test_fallback_is_counted(self):
		location	= Location( 4000.0 )
		self.assertEqual( location.seabed_depth(8.0), 8.0 )
		self.assertEqual( location.seabed_depth(None), 4000.0 )
		self.assertEqual( (location.queries, location.fallbacks), (2, 1) )
		self.assertIn( '1 of 2', location.describe() )

	def test_survey_never_returns_no_depth(self):
		unmapped	= Grounder( Ctxt([Shape('Strait', 'STRAIT')]) )
		self.assertEqual( unmapped.survey(Vessel(1))[2], 4000.0 )

		mapped		= Grounder( Ctxt([Seabed('Channel', 'CHANNEL', 9.0)]) )
		self.assertEqual( mapped.survey(Vessel(1))[2], 9.0 )

	def test_examiner_can_name_its_location_file(self):
		path	= self.write( 'location:\n  depth:\n    nominal: 6.0\n' )
		exam	= Grounder( Ctxt([Shape('Canal', 'CANAL')]), {'zones': None, 'territory': None, 'location': path} )
		self.assertEqual( exam.survey(Vessel(1))[2], 6.0 )

	def test_fallback_never_grounds(self):
		exam	= Grounder( Ctxt() )
		ship	= Vessel( 1 )
		ship.draft	= 25.0
		self.assertGreater( exam.clearance(ship, exam.survey(ship)[2]), 3000.0 )

	def test_sea_resolver_depth_falls_back(self):
		ctxt		= Ctxt( [Shape('Strait', 'STRAIT')] )
		resolver	= SeaResolver( None )
		resolver.reset( ctxt, RuleCtxt(Vessel(1)) )
		self.assertEqual( resolver.Depth(), 4000.0 )


	def test_sea_resolver_without_an_own_ship_is_unresolved(self):
		# The one permitted None (REQ-022-A1): no vessel, so no depth was asked for
		resolver	= SeaResolver( None )
		resolver.reset( Ctxt([Shape('Strait', 'STRAIT')]), RuleCtxt(None) )
		self.assertIsNone( resolver.Depth() )

	def test_provenance_marks_the_fallback(self):
		self.assertEqual( Location.provenance(None), 'nominal' )
		self.assertEqual( Location.provenance(5.0), 'measured' )
		self.assertEqual( Location.provenance(0.0), 'measured' )


class Layered(Shape):
	def __init__(self, name, type, settings=None):
		Shape.__init__( self, name, type )
		if settings is not None:
			self.config	= {'settings': settings}


class NominalLayerTestCase(unittest.TestCase):
	""" REQ-022-06: shape settings, then named zone, then Sea.Type, then location.yaml """
	def setUp(self):
		Location._shared.clear()
		self.rules			= ZoneRules()
		self.rules.defaults	= {'nominal_depth': 1.0}		# Not a layer: location.yaml is the base
		self.rules.types	= {'WATERWAY': {'nominal_depth': 8.0}, 'CANAL': {'nominal_depth': 6.0}}
		self.rules.zones	= {'Inner.Basin': {'nominal_depth': 12.0}}

	def tearDown(self):
		Location._shared.clear()

	def test_no_override_leaves_the_location_depth(self):
		self.assertIsNone( self.rules.nominal_depth([Layered('Open', 'STRAIT')]) )

	def test_type_then_named_then_shape(self):
		self.assertEqual( self.rules.nominal_depth([Layered('Reach', 'WATERWAY')]), 8.0 )
		self.assertEqual( self.rules.nominal_depth([Layered('Inner.Basin', 'WATERWAY')]), 12.0 )
		self.assertEqual( self.rules.nominal_depth([Layered('Inner.Basin', 'WATERWAY', 'nominal_depth=3.5')]), 3.5 )

	def test_shallowest_within_a_layer(self):
		self.assertEqual( self.rules.nominal_depth([Layered('Reach', 'WATERWAY'), Layered('Cut', 'CANAL')]), 6.0 )

	def test_survey_falls_back_to_the_layered_depth_and_counts_it(self):
		exam		= Grounder( Ctxt([Layered('Reach', 'WATERWAY')]) )
		exam.rules	= self.rules
		self.assertEqual( exam.survey(Vessel(1))[2], 8.0 )
		self.assertEqual( exam.location.fallbacks, 1 )

	def test_a_measured_depth_beats_every_override(self):
		exam		= Grounder( Ctxt([Seabed('Reach', 'WATERWAY', 4.0)]) )
		exam.rules	= self.rules
		self.assertEqual( exam.survey(Vessel(1))[2], 4.0 )

	def test_sea_resolver_uses_the_same_layers(self):
		resolver	= SeaResolver( None )
		resolver.reset( Ctxt([Layered('Reach', 'WATERWAY')]), RuleCtxt(Vessel(1)) )
		self.assertEqual( resolver.Depth(), 4000.0 )			# zones.yaml sets no nominal_depth
		resolver.rules.types	= self.rules.types
		self.assertEqual( resolver.Depth(), 8.0 )


class FallbackFindingTestCase(unittest.TestCase):
	""" REQ-022-A4: a nominal reading never produces a grounding or berthing finding """
	def setUp(self):
		Location._shared.clear()

	def tearDown(self):
		Location._shared.clear()

	def run_examiner(self, klass, shape, types=None):
		ctxt	= Ctxt( [shape] )
		exam	= klass.__new__( klass )
		exam.id, exam.callbacks	= klass.__name__, {}
		exam.init_zones( ctxt, {'zones': None, 'territory': None}, requires=['os'] )
		exam.cache_shapes( ctxt )
		exam.sea	= [shape]
		if types is not None:
			exam.rules.types	= types

		vessel	= Vessel( 1 )
		vessel.draft	= 25.0			# Aground in 5 m of water, afloat in 4 000 m
		exam.evaluate( ctxt, PracticeRuleContext([vessel]) )
		return [ row[1][4] for row in ctxt.sim.data.rows ]

	def test_grounding(self):
		self.assertEqual( self.run_examiner(GroundingExaminer, Shape('Open', 'STRAIT')), [] )
		self.assertEqual( self.run_examiner(GroundingExaminer, Seabed('Shoal', 'STRAIT', 5.0)), ['grounding.contact'] )

	def test_berthing(self):
		self.assertEqual( self.run_examiner(BerthingExaminer, Shape('Basin', 'HARBOUR')), [] )
		self.assertEqual( self.run_examiner(BerthingExaminer, Seabed('Quay', 'HARBOUR', 5.0)), ['berthing.contact'] )

	def test_a_shallow_zone_override_is_still_no_finding(self):
		# The override sets the depth the risk network sees; a nominal reading is never a finding
		shallow	= {'STRAIT': {'nominal_depth': 3.0}, 'HARBOUR': {'nominal_depth': 3.0}}
		self.assertEqual( self.run_examiner(GroundingExaminer, Shape('Open', 'STRAIT'), shallow), [] )
		self.assertEqual( self.run_examiner(BerthingExaminer, Shape('Basin', 'HARBOUR'), shallow), [] )


class ProvenanceRowTestCase(unittest.TestCase):
	""" REQ-022-A5: risk rows say whether the depth was measured or nominal """
	def test_depth_and_its_source_are_recorded(self):
		exam		= RiskExaminer.__new__( RiskExaminer )
		exam.id		= 'Risk'
		ctxt		= Ctxt()
		row			= report( {'safety': 1.0, 'traffic': 0.0, 'environmental': 0.0, 'operational': 0.0} )
		row['depth'], row['depth_source']	= 4000.0, 'nominal'
		exam.record( ctxt, row )

		written	= [ v for t, v in ctxt.sim.data.rows if t == 'fact_risk_assessment' ][0]
		named	= dict( zip(fields('fact_risk_assessment')[AUDIT_FIELDS:], written) )
		self.assertEqual( (named['depth'], named['depth_source']), (4000.0, 'nominal') )


if __name__ == '__main__':
	unittest.main()
