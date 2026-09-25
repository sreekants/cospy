#!/usr/bin/python
# Filename: test_Ledger.py
# Description: Test cases for the Ro write path (PLAN-E1, REQ.017-019)

import os, sys, datetime, importlib, unittest
from xml.dom import minidom

from maritime.model.zone.Ledger import Ledger, FindingGuard, FACT, SOURCE_EXAMINER, SOURCE_COLREG
from maritime.model.zone.ZoneRules import ZoneRules
from maritime.model.zone.ZoneAwareness import ZoneAware
from maritime.model.rule.ScoredRule import ScoredRule
from cos.subsystem.data.Partition import AUDIT_FIELDS

ROOT	= os.path.abspath( os.path.join(os.path.dirname(__file__), '..', '..', '..', '..') )
CONFIG	= os.path.join( ROOT, 'config' )
SRC		= os.path.join( ROOT, 'src' )


def source_module(name):
	""" Imports a module from src/rules, which tests/rules shadows in a whole-suite run """
	for key in [ k for k in sys.modules if (k == 'rules') or k.startswith('rules.') ]:
		origin	= getattr( sys.modules[key], '__file__', None ) or ''
		if not origin.startswith( SRC ):
			del sys.modules[key]

	saved		= sys.path[:]
	sys.path[:]	= [ SRC ] + [ p for p in saved
							  if not os.path.isfile(os.path.join(p or '.', 'rules', '__init__.py')) ]
	try:
		return importlib.import_module( name )
	finally:
		sys.path[:]	= saved


class Log:
	def __init__(self):
		self.errors	= []
	def error(self, module, text):
		self.errors.append( (module, text) )
	def info(self, module, text):
		pass


class Data:
	def __init__(self):
		self.rows	= []
	def push(self, topic, row):
		self.rows.append( (topic, row) )


class Config:
	def resolve(self, path):
		return path.replace( '$(CONFIG)', CONFIG ) \
				   .replace( '$(SIMULATION)', os.path.join(CONFIG, 'simulation', 'tk', 'turkeli') )


class FS:
	def read_file_as_bytes(self, path):
		with open( path, 'rb' ) as f:
			return f.read()


class Objects:
	def __init__(self, sea):
		self.sea	= sea
	def get_all(self, path):
		return self.sea


class Sim:
	def __init__(self, sea=()):
		self.data		= Data()
		self.config		= Config()
		self.fs			= FS()
		self.objects	= Objects( list(sea) )
		self.clock		= datetime.datetime( 2026, 9, 25, 22, 0, 0 )
	def now(self):
		return self.clock
	def advance(self, seconds):
		self.clock	= self.clock + datetime.timedelta( seconds=seconds )


class IPC:
	def push(self, *args):
		pass


class Ctxt:
	def __init__(self, sea=()):
		self.sim	= Sim( sea )
		self.log	= Log()
		self.ipc	= IPC()


class Shape:
	""" A map shape: everything contains the vessel """
	def __init__(self, name, type):
		self.name	= name
		self.type	= type
		self.config	= {}
	def contains(self, position):
		return True


class Vessel:
	def __init__(self, imo, location=(0.0, 0.0)):
		self.config		= {'identifier': {'imo': imo}}
		self.location	= location


class FindingGuardTestCase(unittest.TestCase):
	def test_continuing_condition_is_one_finding(self):
		guard	= FindingGuard( scope='change', release=10.0 )
		found	= [ guard.admit(('v', 'grounding.contact', 'a'), t) for t in range(100) ]
		self.assertEqual( sum(found), 1 )

	def test_recurrence_after_release_is_a_second_finding(self):
		guard	= FindingGuard( scope='change', release=10.0 )
		key		= ('v', 'grounding.contact', 'a')
		first	= [ guard.admit(key, t) for t in range(0, 20) ]
		second	= [ guard.admit(key, t) for t in range(60, 80) ]		# Refloated for 40 s
		self.assertEqual( sum(first) + sum(second), 2 )

	def test_clear_ends_an_occurrence_at_once(self):
		guard	= FindingGuard( scope='change', release=1000.0 )
		key		= ('v', 'grounding.contact', 'a')
		self.assertTrue( guard.admit(key, 0) )
		guard.clear( key )
		self.assertTrue( guard.admit(key, 1) )

	def test_episode_scope_never_repeats(self):
		guard	= FindingGuard( scope='episode' )
		key		= ('v', 'night.lights_missing', '2026-09-25')
		self.assertTrue( guard.admit(key, 0) )
		self.assertFalse( guard.admit(key, 100000) )

	def test_interval_scope_repeats_while_continuing(self):
		guard	= FindingGuard( scope='interval', release=10.0, interval=60.0 )
		found	= [ guard.admit(('v', 'e', 's'), t) for t in range(0, 180) ]
		self.assertEqual( sum(found), 3 )

	def test_dwell_ignores_a_spike(self):
		guard	= FindingGuard( scope='change', release=10.0, dwell=2.0 )
		self.assertFalse( guard.admit(('v', 'speed', 'a'), 0) )
		self.assertFalse( guard.admit(('v', 'speed', 'b'), 100) )
		self.assertEqual( sum(guard.admit(('v', 'speed', 'c'), t) for t in range(200, 210)), 1 )

	def test_distinct_vessels_are_distinct_findings(self):
		guard	= FindingGuard( scope='change', release=10.0 )
		self.assertTrue( guard.admit(('v1', 'e', 's'), 0) )
		self.assertTrue( guard.admit(('v2', 'e', 's'), 0) )

	def test_state_is_bounded(self):
		guard	= FindingGuard( scope='change', release=10.0 )
		for t in range(10000):
			guard.admit( (f'v{t}', 'e', 's'), float(t) )
		# Pruned once per release window: at most two windows of keys
		self.assertLessEqual( len(guard), 2 * 10 + 1 )

	def test_unknown_scope_is_refused(self):
		with self.assertRaises( ValueError ):
			FindingGuard( scope='always' )


class ZoneRulesConcernTestCase(unittest.TestCase):
	def setUp(self):
		self.rules	= ZoneRules()
		self.rules.load( Ctxt(), '$(CONFIG)/examiner/zones.yaml' )

	def test_configuration_is_consistent(self):
		self.assertEqual( self.rules.errors(), [] )

	def test_every_priced_event_has_a_concern(self):
		for event in self.rules.penalties:
			self.assertIn( self.rules.concern(event), self.rules.vocabulary, event )

	def test_colreg_clause_falls_back_to_the_rule_set(self):
		self.assertEqual( self.rules.penalty('COLREG.Rule14.a'), self.rules.penalty('COLREG') )
		self.assertEqual( self.rules.concern('COLREG.Rule10.b.iii/EnterTrafficSeparationScheme'),
						  self.rules.concern('COLREG') )

	def test_unmapped_event_is_reported(self):
		self.rules.penalties['made.up']	= 1.0
		self.assertTrue( any('made.up' in p for p in self.rules.errors()) )

	def test_vocabulary_matches_the_territory(self):
		import yaml
		risk	= yaml.safe_load( open(os.path.join(CONFIG, 'simulation', 'tk', 'turkeli', 'risk.yaml')) )
		self.assertEqual( sorted(self.rules.vocabulary), sorted(risk['risk']['concerns']) )


class LedgerTestCase(unittest.TestCase):
	def setUp(self):
		self.ctxt	= Ctxt( [Shape('Turkeli.Harbour', 'HARBOUR')] )
		self.ledger	= Ledger()
		self.ledger.load( self.ctxt, 'test' )

	def test_row_matches_the_declared_schema(self):
		self.ledger.record( self.ctxt, SOURCE_EXAMINER, 'GroundingExaminer', Vessel(9000001),
							'grounding.contact', self.ledger.shapes(self.ctxt, Vessel(1)), 95.0, -0.5 )

		topic, row	= self.ctxt.sim.data.rows[0]
		self.assertEqual( topic, FACT )

		doc		= minidom.parse( os.path.join(CONFIG, 'data', 'maritime.xml') )
		for fact in doc.getElementsByTagName('Fact'):
			if fact.getElementsByTagName('TableName')[0].childNodes[0].nodeValue == FACT:
				fields	= [ m.getElementsByTagName('FieldName')[0].childNodes[0].nodeValue
							for m in fact.getElementsByTagName('Measure') ]
		self.assertEqual( len(row) + AUDIT_FIELDS, len(fields) )

		named	= dict( zip(fields[AUDIT_FIELDS:], row) )
		self.assertEqual( named['vessel_id'], 9000001 )
		self.assertEqual( named['source'], SOURCE_EXAMINER )
		self.assertEqual( named['event'], 'grounding.contact' )
		self.assertEqual( named['area'], 'Turkeli.Harbour' )
		self.assertEqual( named['zone'], 'port' )
		self.assertEqual( named['concern'], 'safety' )
		self.assertEqual( named['penalty'], 95.0 )

	def test_zero_penalty_is_not_recorded(self):
		self.assertFalse( self.ledger.record(self.ctxt, SOURCE_EXAMINER, 'X', Vessel(1), 'grounding.contact', [], 0.0) )
		self.assertEqual( self.ctxt.sim.data.rows, [] )

	def test_unmapped_event_is_not_recorded(self):
		self.assertFalse( self.ledger.record(self.ctxt, SOURCE_EXAMINER, 'X', Vessel(1), 'made.up', [], 1.0) )
		self.assertEqual( self.ctxt.sim.data.rows, [] )
		self.assertTrue( self.ctxt.log.errors )


class Grounder(ZoneAware):
	""" A ZoneAware examiner reduced to what violate() needs """
	id		= 'Grounder'

	def __init__(self, ctxt):
		self.init_zones( ctxt, {'zones': None, 'territory': None} )


class ZoneAwareTestCase(unittest.TestCase):
	def setUp(self):
		self.ctxt	= Ctxt( [Shape('Turkeli.Strait', 'STRAIT')] )
		self.exam	= Grounder( self.ctxt )
		self.shapes	= self.exam.ledger.shapes( self.ctxt, Vessel(1) )

	def tick(self, vessel, n):
		for _ in range(n):
			self.exam.violate( self.ctxt, vessel, 'grounding.contact', self.shapes, value=-1.0 )
			self.ctxt.sim.advance( 1 )

	def test_hundred_ticks_aground_is_one_finding(self):
		self.tick( Vessel(1), 100 )
		self.assertEqual( len(self.ctxt.sim.data.rows), 1 )

	def test_ground_refloat_ground_is_two_findings(self):
		vessel	= Vessel(1)
		self.tick( vessel, 20 )
		self.exam.settle( vessel, 'grounding.contact', self.shapes )		# Clear water seen
		self.tick( vessel, 20 )
		self.assertEqual( len(self.ctxt.sim.data.rows), 2 )

	def test_two_vessels_both_recorded(self):
		self.tick( Vessel(1), 1 )
		self.tick( Vessel(2), 1 )
		self.assertEqual( len(self.ctxt.sim.data.rows), 2 )

	def test_finding_count_is_invariant_to_duration(self):
		# Held for 10 or 300 ticks, one finding either way
		self.tick( Vessel(1), 10 )
		self.tick( Vessel(2), 300 )
		self.assertEqual( len(self.ctxt.sim.data.rows), 2 )


class NightKeyTestCase(unittest.TestCase):
	def test_two_vessels_in_one_daylight_pass_keep_their_night_record(self):
		NightTimeExaminer	= source_module( 'rules.examiner.navigation.NightTimeExaminer' ).NightTimeExaminer

		ctxt		= Ctxt( [Shape('Turkeli.Strait', 'STRAIT')] )
		exam		= NightTimeExaminer.__new__( NightTimeExaminer )
		exam.id		= 'NightTime'
		exam.init_zones( ctxt, {'zones': None, 'territory': None} )
		shapes		= exam.ledger.shapes( ctxt, Vessel(1) )
		rules		= exam.rules.rules_at( shapes )
		missing		= ['masthead']

		ctxt.sim.clock	= datetime.datetime( 2026, 9, 25, 23, 0, 0 )
		for v in (Vessel(1), Vessel(2)):
			exam.score( ctxt, v, shapes, rules, missing, missing )

		# A daylight pass evaluates both vessels; nothing is cleared
		ctxt.sim.clock	= datetime.datetime( 2026, 9, 26, 12, 0, 0 )
		for v in (Vessel(1), Vessel(2)):
			self.assertFalse( exam.is_night(ctxt, rules) )

		# Still the night of the 25th after midnight: no repeat for either
		ctxt.sim.clock	= datetime.datetime( 2026, 9, 26, 2, 0, 0 )
		for v in (Vessel(1), Vessel(2)):
			exam.score( ctxt, v, shapes, rules, missing, missing )
		self.assertEqual( len(ctxt.sim.data.rows), 2 )

		# The next night is a new finding for each
		ctxt.sim.clock	= datetime.datetime( 2026, 9, 26, 22, 0, 0 )
		for v in (Vessel(1), Vessel(2)):
			exam.score( ctxt, v, shapes, rules, missing, missing )
		self.assertEqual( len(ctxt.sim.data.rows), 4 )


class ClauseNameTestCase(unittest.TestCase):
	def test_failed_body_resolves_to_its_clause(self):
		from cos.model.rule.Automata import Automata

		automata	= Automata( None )
		automata.load( os.path.join(CONFIG, 'maritime', 'regulation', 'colreg', 'Rule14.legata') )
		clause		= automata.definition.root.children[0]
		body		= clause.children[0]
		self.assertEqual( ScoredRule.clause_name(body), 'COLREG.Rule14.a' )


if __name__ == '__main__':
	unittest.main()
