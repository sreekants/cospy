#!/usr/bin/python
# Filename: test_Rb.py
# Description: Test cases for the Rb long form, fact_rb (REQ.018)

import os, sys, shutil, sqlite3, subprocess, tempfile, unittest
from xml.dom import minidom

import yaml

from tests.maritime.model.risk.test_ConcernWeights import source_module, ROOT, CONFIG
from cos.subsystem.data.Partition import AUDIT_FIELDS

RiskExaminer	= source_module( 'rules.examiner.risk.RiskExaminer' ).RiskExaminer
VOCABULARY		= ['safety', 'traffic', 'environmental', 'operational']


def fields(table):
	doc	= minidom.parse( os.path.join(CONFIG, 'data', 'maritime.xml') )
	for fact in doc.getElementsByTagName('Fact'):
		if fact.getElementsByTagName('TableName')[0].childNodes[0].nodeValue == table:
			return [ m.getElementsByTagName('FieldName')[0].childNodes[0].nodeValue
					 for m in fact.getElementsByTagName('Measure') ]


class Data:
	def __init__(self):
		self.rows	= []
	def push(self, topic, row):
		self.rows.append( (topic, row) )


class Log:
	def __init__(self):
		self.errors	= []
	def error(self, module, text):
		self.errors.append( text )
	def info(self, module, text):
		pass


class Sim:
	def __init__(self):
		self.data	= Data()
	class config:
		@staticmethod
		def resolve(path):
			return path
	class fs:
		@staticmethod
		def read_file_as_bytes(path):
			return open( path, 'rb' ).read()


class Ipc:
	def get_node(self, path):
		return None

	def pump_node(self, node):
		return 0


class Ctxt:
	def __init__(self):
		self.sim	= Sim()
		self.log	= Log()
		self.ipc	= Ipc()


class Rules:
	vocabulary	= VOCABULARY


def report(exposure):
	return { 'time': '2026-09-25 12:00:00', 'vessel': 'bedc897f-512b-45a2-aea4-bcfc248d2a86', 'imo': '9627837', 'recid': 101, 'zone': 'port', 'matrix': '[0];',
			 'hazards': {'collision': 0.1, 'grounding': 0.0, 'loss_of_comms': 0.0, 'any': 0.1, 'sum': 0.1},
			 'individual_risk': 0.0,
			 'exposure': exposure, 'cost': sum(exposure.values()), 'increment': 0.0,
			 'survival': 1.0, 'cumulative': 0.0,
			 'exposure_basis': 'rate', 'exposure_period': 3600.0, 'exposure_dt': 1.0,
			 'depth': 4000.0, 'depth_source': 'nominal' }


class RecordTestCase(unittest.TestCase):
	def setUp(self):
		self.exam		= RiskExaminer.__new__( RiskExaminer )
		self.exam.id	= 'Risk'
		self.ctxt		= Ctxt()

	def test_one_row_per_concern_zeros_included(self):
		exposure	= {'safety': 120.0, 'traffic': 30.0, 'environmental': 0.0, 'operational': 5.0}
		self.exam.record( self.ctxt, report(exposure) )

		rb	= [ row for topic, row in self.ctxt.sim.data.rows if topic == 'fact_rb' ]
		self.assertEqual( len(rb), 4 )

		named	= [ dict(zip(fields('fact_rb')[AUDIT_FIELDS:], row)) for row in rb ]
		self.assertEqual( {r['concern'] for r in named}, set(VOCABULARY) )
		self.assertEqual( [r['exposure'] for r in named if r['concern'] == 'environmental'], [0.0] )
		self.assertEqual( {r['zone'] for r in named}, {'port'} )
		self.assertAlmostEqual( sum(r['exposure'] for r in named), report(exposure)['cost'] )

	def test_payload_width_matches_the_schema(self):
		self.exam.record( self.ctxt, report({c: 1.0 for c in VOCABULARY}) )
		for topic, row in self.ctxt.sim.data.rows:
			if topic == 'fact_rb':
				self.assertEqual( len(row) + AUDIT_FIELDS, len(fields('fact_rb')) )

	def test_columns_join_fact_concern_without_translation(self):
		rb, ro	= set( fields('fact_rb') ), set( fields('fact_concern') )
		self.assertTrue( {'vessel_id', 'zone', 'concern'} <= (rb & ro) )

	def test_vocabulary_mismatch_stops_the_examiner_at_load(self):
		risk	= yaml.safe_load( open(os.path.join(CONFIG, 'simulation', 'tk', 'turkeli', 'risk.yaml')) )['risk']
		self.exam.bn	= None
		self.exam.rules	= Rules()
		self.exam.rules.vocabulary	= VOCABULARY + ['comfort']

		f	= tempfile.NamedTemporaryFile( 'w', suffix='.yaml', delete=False )
		yaml.safe_dump( {'risk': risk}, f )
		f.close()
		self.addCleanup( os.unlink, f.name )

		with self.assertRaises( ValueError ) as raised:
			self.exam._RiskExaminer__load_matrix( self.ctxt, f.name )
		self.assertIn( 'REQ-018-04', str(raised.exception) )


class HarnessTestCase(unittest.TestCase):
	""" The RB checks in verify_facts.py, against a scratch copy of the template """

	def database(self, exposures, cost):
		folder	= tempfile.mkdtemp()
		self.addCleanup( shutil.rmtree, folder )
		path	= os.path.join( folder, 'run.s3db' )
		shutil.copy( os.path.join(CONFIG, 'data', 'maritime.s3db'), path )

		db		= sqlite3.connect( path )
		db.execute( "insert into fact_risk_assessment (case_id, report_time, own_ship, zone, cost) "
					"values (7, 't1', 9627837, 'port', ?)", (cost,) )
		for concern, value in exposures.items():
			db.execute( "insert into fact_rb (case_id, report_time, vessel_id, zone, concern, exposure) "
						"values (7, 't1', 9627837, 'port', ?, ?)", (concern, value) )
		db.commit()
		db.close()
		return path

	def run_harness(self, path):
		result	= subprocess.run( [sys.executable, os.path.join(ROOT, 'tests', 'rules', 'examiner', 'verify_facts.py'), path],
								  capture_output=True, text=True )
		return { line.split()[1]: line.split()[0] for line in result.stdout.splitlines()
				 if line.strip().startswith(('PASS', 'FAIL', 'SKIP')) and ' RB-' in line }

	def test_reconciling_sample_passes(self):
		exposure	= {'safety': 120.0, 'traffic': 30.0, 'environmental': 0.0, 'operational': 5.0}
		checks		= self.run_harness( self.database(exposure, 155.0) )
		self.assertEqual( checks, {'RB-X1': 'PASS', 'RB-X2': 'PASS', 'RB-X3': 'PASS'} )

	def test_missing_concern_and_bad_sum_fail(self):
		exposure	= {'safety': 120.0, 'traffic': 30.0, 'operational': 5.0}
		checks		= self.run_harness( self.database(exposure, 999.0) )
		self.assertEqual( checks, {'RB-X1': 'FAIL', 'RB-X2': 'FAIL', 'RB-X3': 'FAIL'} )


if __name__ == '__main__':
	unittest.main()
