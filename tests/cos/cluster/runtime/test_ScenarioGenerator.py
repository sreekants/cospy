#!/usr/bin/python
# Filename: ScenarioGenerator_test.py
# Description: Test cases for the ScenarioGenerator class

from cos.cluster.runtime.ScenarioGenerator import ScenarioGenerator
from cos.core.kernel.Configuration import Configuration

import unittest

class ScenarioGeneratorTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		templatedir	= Configuration.resolve_path('$(COS_ROOT)/templates/cluster/config')
		self.test 	= ScenarioGenerator( templatedir,
			'${COS_DIR}/apps/coslaunch/main.py -config $$COS_CONFIG$$',
			{
			"LOCATION":["alesund","trondheim","molde","liekanger"],
			"WEATHER":["clearsky","cloudy","foggy","heavyrain","highsea","hurricane","lightrain","snow","wind"],
			"TRAFFIC":["hdta","mdta","ldta","ctz","rdta","vdta","seasonal"],
			"SITUATION":["crossing","headon","overtaking","giveway","standon","restricted.visibility","narrow.channels","anchored"],
			"ZONE":["tss","narrow.channels","deep.water","roundabouts","inshore","precautionary","restricted.visibility","anchor.areas","restricted.speed","clearance"],
			"JURISDICTION":["territorial","contiguous","exclusive.economic","high.sea","international","archipelagic"],
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


if __name__ == '__main__':
    unittest.main()
