#!/usr/bin/python
# Filename: test_CaseId.py
# Description: Test cases for case identity: the case id, replicates and the case manifest (COS.003)

import csv, os, shutil, tempfile, unittest

from cos.core.kernel.Configuration import Configuration
from cos.core.utilities.CaseId import case_id, BITS
from cos.cluster.runtime.ScenarioGenerator import ScenarioGenerator, MANIFEST

TEMPLATE	= Configuration.resolve_path('$(COS_ROOT)/templates/cluster/config')
CONFIG		= Configuration.resolve_path('$(COS_ROOT)/config')


class CaseIdTestCase(unittest.TestCase):
	def test_absent_or_empty_scenario_is_refused(self):
		for key in (None, '', '   '):
			with self.assertRaises( ValueError ):
				case_id( key )

	def test_52_bits_and_deterministic(self):
		a	= case_id( 'scenario-0:no/bergen/clearsky/ldta' )
		self.assertEqual( a, case_id('scenario-0:no/bergen/clearsky/ldta') )
		self.assertLess( a, 2**BITS )
		self.assertEqual( float(a), a )

	def test_replicates_differ(self):
		self.assertNotEqual( case_id('scenario-0:no/bergen/clearsky/ldta'),
							 case_id('scenario-1:no/bergen/clearsky/ldta') )


class ManifestTestCase(unittest.TestCase):
	def setUp(self):
		self.out	= tempfile.mkdtemp()
		self.addCleanup( shutil.rmtree, self.out )

	def generator(self, extra=None):
		dims	= { ('COUNTRY','LOCATION'): ScenarioGenerator.sites(CONFIG), 'WEATHER': ['clearsky', 'foggy'], 'TRAFFIC': ['ldta'] }
		dims.update( extra or {} )
		return ScenarioGenerator( TEMPLATE, 'coslaunch.py -c $$COS_CONFIG$$/cos.ini', dims )

	def manifest(self):
		with open( os.path.join(self.out, MANIFEST) ) as f:
			return list( csv.DictReader(f) )

	def test_replicates_get_their_own_case_and_case_id(self):
		configs	= self.generator().generate( self.out + '/', os.path.join(self.out, 'tasks.conf'), 1, seed=1, replicates=3 )
		rows	= self.manifest()
		self.assertEqual( len(configs), 3 )
		self.assertEqual( sorted(r['CASE'] for r in rows), ['0', '1', '2'] )
		self.assertEqual( len({r['case_id'] for r in rows}), 3 )

	def test_manifest_matches_the_kernel(self):
		self.generator().generate( self.out + '/', os.path.join(self.out, 'tasks.conf'), -1, seed=1 )
		for r in self.manifest():
			self.assertEqual( int(r['case_id']), case_id(r['SCENARIO']) )
			self.assertEqual( r['SCENARIO'], f"scenario-{r['CASE']}:{r['COUNTRY']}/{r['LOCATION']}/{r['WEATHER']}/{r['TRAFFIC']}" )
			self.assertTrue( os.path.isdir(os.path.join(self.out, r['folder'])) )

	def test_an_untagged_swept_dimension_is_refused(self):
		with self.assertRaises( ValueError ) as raised:
			self.generator( {'TECHNICAL_CASES': ['basic', 'stpa']} ).generate( self.out + '/', os.path.join(self.out, 'tasks.conf'), -1, seed=1 )
		self.assertIn( 'missing from SCENARIO', str(raised.exception) )


if __name__ == '__main__':
	unittest.main()
