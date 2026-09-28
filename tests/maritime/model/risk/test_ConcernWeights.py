#!/usr/bin/python
# Filename: test_ConcernWeights.py
# Description: Test cases for Rw, the concern weights (REQ.004)

import os, sys, glob, importlib, tempfile, unittest
from xml.dom import minidom

import yaml

from cos.subsystem.data.Partition import AUDIT_FIELDS

ROOT	= os.path.abspath( os.path.join(os.path.dirname(__file__), '..', '..', '..', '..') )
CONFIG	= os.path.join( ROOT, 'config' )
SRC		= os.path.join( ROOT, 'src' )
TERRITORIES	= sorted( glob.glob(os.path.join(CONFIG, 'simulation', '*', '*', 'risk.yaml'))
					  + glob.glob(os.path.join(ROOT, 'scenarios', 'config', 'simulation', '*', '*', 'risk.yaml')) )


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


RiskModel		= source_module( 'rules.examiner.risk.RiskModel' )
ConcernWeights	= RiskModel.ConcernWeights
LossMatrix		= RiskModel.LossMatrix
compose_ev		= RiskModel.compose_ev

CONCERNS	= ['safety', 'traffic', 'environmental', 'operational']


def weights(**w):
	return ConcernWeights( {'concerns': CONCERNS, 'weights': w} )


class Posterior:
	def __init__(self, node, probabilities):
		self.node	= node
		self.p		= probabilities
	def __getitem__(self, key):
		return self.p[ key[self.node] ]


class Engine:
	""" Posteriors for a fake network: every state equally likely """
	def __init__(self, cost):
		self.cost	= cost
	def posterior(self, node):
		states	= list( self.cost[node] )
		return Posterior( node, {s: 1.0 / len(states) for s in states} )


class ConcernWeightsTestCase(unittest.TestCase):
	def test_every_territory_declares_valid_weights(self):
		self.assertTrue( TERRITORIES )
		for path in TERRITORIES:
			risk	= yaml.safe_load( open(path) )['risk']
			self.assertEqual( ConcernWeights(risk).errors(), [], path )

	def test_uniform_is_the_null(self):
		rw	= weights( safety=1, traffic=1, environmental=1, operational=1 ).normalised()
		self.assertEqual( set(rw.values()), {0.25} )

	def test_normalised_weights_sum_to_one(self):
		rw	= weights( safety=4, traffic=2, environmental=1, operational=1 ).normalised()
		self.assertAlmostEqual( sum(rw.values()), 1.0 )
		self.assertAlmostEqual( rw['safety'], 0.5 )

	def test_missing_and_unknown_keys_are_named(self):
		problems	= weights( safety=1, traffic=1, environmental=1, comfort=1 ).errors()
		self.assertTrue( any("'operational'" in p for p in problems) )
		self.assertTrue( any("'comfort'" in p for p in problems) )

	def test_bad_values_are_refused(self):
		self.assertTrue( weights(safety=-1, traffic=1, environmental=1, operational=1).errors() )
		self.assertTrue( weights(safety='x', traffic=1, environmental=1, operational=1).errors() )
		self.assertTrue( weights(safety=0, traffic=0, environmental=0, operational=0).errors() )


class ComposeTestCase(unittest.TestCase):
	RO	= { 'port': {'safety': 2.0, 'traffic': 1.0, 'environmental': 0.0, 'operational': 3.0},
			'high_seas': {'safety': 1.0, 'traffic': 0.0, 'environmental': 1.0, 'operational': 0.0} }
	RL	= { 'port': {'safety': 100.0, 'traffic': 50.0, 'environmental': 10.0, 'operational': 5.0},
			'high_seas': {'safety': 20.0, 'traffic': 10.0, 'environmental': 2.0, 'operational': 1.0} }

	def test_elementwise_with_rw_broadcast_over_zones(self):
		rw	= weights( safety=2, traffic=1, environmental=1, operational=0 ).normalised()
		ev	= compose_ev( self.RO, rw, self.RL )
		self.assertAlmostEqual( ev['port']['safety'], 2.0 * 0.5 * 100.0 )
		self.assertAlmostEqual( ev['high_seas']['environmental'], 1.0 * 0.25 * 2.0 )
		self.assertEqual( ev['port']['operational'], 0.0 )

	def test_scaling_every_weight_leaves_r_ev_unchanged(self):
		a	= compose_ev( self.RO, weights(safety=3, traffic=1, environmental=2, operational=1).normalised(), self.RL )
		b	= compose_ev( self.RO, weights(safety=30, traffic=10, environmental=20, operational=10).normalised(), self.RL )
		for zone in a:
			for concern in a[zone]:
				self.assertAlmostEqual( a[zone][concern], b[zone][concern] )


class RecordingTestCase(unittest.TestCase):
	def territory(self, **w):
		risk	= yaml.safe_load( open(os.path.join(CONFIG, 'simulation', 'tk', 'turkeli', 'risk.yaml')) )['risk']
		risk['weights']	= w
		return risk

	def test_rw_does_not_change_rl(self):
		uniform	= self.territory( safety=1, traffic=1, environmental=1, operational=1 )
		skewed	= self.territory( safety=9, traffic=1, environmental=0, operational=3 )
		engine	= Engine( uniform['cost'] )
		self.assertEqual( LossMatrix(uniform).matrix(engine), LossMatrix(skewed).matrix(engine) )

	def test_fact_rw_width_matches_the_schema(self):
		doc	= minidom.parse( os.path.join(CONFIG, 'data', 'maritime.xml') )
		for fact in doc.getElementsByTagName('Fact'):
			if fact.getElementsByTagName('TableName')[0].childNodes[0].nodeValue == 'fact_rw':
				fields	= [ m.getElementsByTagName('FieldName')[0].childNodes[0].nodeValue
							for m in fact.getElementsByTagName('Measure') ]
		self.assertEqual( fields[AUDIT_FIELDS:], ['report_time', 'concern', 'weight', 'declared'] )

	def test_bad_weights_stop_the_examiner_at_load(self):
		RiskExaminer	= source_module( 'rules.examiner.risk.RiskExaminer' ).RiskExaminer

		class Log:
			def __init__(self):
				self.errors	= []
			def error(self, module, text):
				self.errors.append( text )
			def info(self, module, text):
				pass

		class Sim:
			class config:
				@staticmethod
				def resolve(path):
					return path
			class fs:
				@staticmethod
				def read_file_as_bytes(path):
					return open( path, 'rb' ).read()

		class Ctxt:
			sim	= Sim()
			log	= Log()

		f	= tempfile.NamedTemporaryFile( 'w', suffix='.yaml', delete=False )
		yaml.safe_dump( {'risk': self.territory(safety=1, traffic=1, environmental=1, comfort=1)}, f )
		f.close()
		self.addCleanup( os.unlink, f.name )

		exam		= RiskExaminer.__new__( RiskExaminer )
		exam.id		= 'Risk'
		exam.bn		= None
		ctxt		= Ctxt()
		with self.assertRaises( ValueError ) as raised:
			exam._RiskExaminer__load_matrix( ctxt, f.name )

		self.assertIn( 'operational', str(raised.exception) )
		self.assertIn( 'comfort', str(raised.exception) )


if __name__ == '__main__':
	unittest.main()
