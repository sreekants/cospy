#!/usr/bin/python
# Filename: ScenarioGenerator_test.py
# Description: Test cases for the ScenarioGenerator class

from cos.cluster.runtime.ScenarioGenerator import ScenarioGenerator
from cos.core.kernel.Configuration import Configuration

import unittest, os

class ScenarioGeneratorTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		templatedir	= Configuration.resolve_path('$(COS_ROOT)/templates/cluster/config')
		self.configdir	= Configuration.resolve_path('$(COS_ROOT)/config')
		self.test 	= ScenarioGenerator( templatedir,
			'${COS_DIR}/apps/coslaunch/main.py -config $$COS_CONFIG$$',
			{
			("COUNTRY","LOCATION"):ScenarioGenerator.sites(self.configdir),
			"WEATHER":["clearsky","cloudy","foggy","heavyrain","highsea","hurricane","lightrain","snow","wind"],
			"TRAFFIC":["hdta","mdta","ldta","ctz","rdta","vdta","seasonal"],
			"LEGAL_CASES":["singapore"],
			"TECHNICAL_CASES":["basic","stpa"],
		})

		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_generate(self):
		self.test.generate('output','tasks.conf', 10)
		return

	def sample(self, count, seed):
		self.test.maxcount	= count
		cases	= self.test.permutation( [], list(self.test.scenarios.keys()), [] )
		self.test.shuffle( cases, seed )
		return [tuple(case[1]) for case in cases[:count]]

	def test_sites_exist(self):
		sites	= ScenarioGenerator.sites(self.configdir)
		self.assertIn( ('no','alesund'), sites )
		self.assertIn( ('tk','turkeli'), sites )
		self.assertNotIn( ('tk','alesund'), sites )
		return

	def test_paired_declarations(self):
		case	= (0, [(("COUNTRY","LOCATION"),("no","alesund")), ("WEATHER","foggy")])
		text	= self.test.declarations(case).replace_text('$$COUNTRY$$/$$LOCATION$$/$$WEATHER$$')
		self.assertEqual( text, 'no/alesund/foggy' )
		return

	def test_validate_existing_paths(self):
		self.test.maxcount	= -1
		cases	= self.test.permutation( [], list(self.test.scenarios.keys()), [] )
		self.test.validate( cases )
		return

	def test_validate_missing_paths(self):
		cases	= [ (0, [(("COUNTRY","LOCATION"),("tk","alesund"))]) ]
		with self.assertRaises( ValueError ) as err:
			self.test.validate( cases )
		self.assertIn( 'simulation/tk/alesund', str(err.exception) )
		self.assertIn( 'map/tk/alesund', str(err.exception) )
		return

	def test_select_country(self):
		cases	= self.test.permutation( [], list(self.test.scenarios.keys()), [] )
		tk		= self.test.select( cases, 'tk' )
		sites	= [ s for s in ScenarioGenerator.sites(self.configdir) if s[0] == 'tk' ]
		self.assertEqual( len(tk), len(cases) // len(ScenarioGenerator.sites(self.configdir)) * len(sites) )
		for case in tk:
			self.assertEqual( dict(case[1])[("COUNTRY","LOCATION")][0], 'tk' )
		self.assertIs( self.test.select(cases, None), cases )
		return

	def test_select_unknown_country(self):
		cases	= self.test.permutation( [], list(self.test.scenarios.keys()), [] )
		with self.assertRaises( ValueError ):
			self.test.select( cases, 'xx' )
		return

	def test_generate_country(self):
		configs	= self.test.generate('output','tasks.conf', 10, seed=42, country='tk')
		self.assertEqual( len(configs), 10 )
		for path in configs:
			with open( os.path.join(path, 'cos.ini'), 'rt' ) as f:
				self.assertIn( 'COUNTRY=tk\n', f.read() )
		return

	def test_shuffle_reproducible(self):
		self.assertEqual( self.sample(100, 42), self.sample(100, 42) )
		self.assertNotEqual( self.sample(100, 42), self.sample(100, 43) )
		return

	def test_shuffle_varies_all_dimensions(self):
		cases	= self.sample(100, 42)
		for dim, values in self.test.scenarios.items():
			if len(values) > 1:
				distinct	= { dict(case)[dim] for case in cases }
				self.assertGreater( len(distinct), 1, dim )
		return


if __name__ == '__main__':
    unittest.main()
