#!/usr/bin/python
# Filename: ColregResolver_test.py
# Description: Test cases for the ColregResolver class

from maritime.model.vessel.Builder import Builder
from maritime.model.resolver.TargetResolver import TargetResolver
from maritime.model.resolver.ColregResolver import ColregResolver
from RESOURCES import VESSELS

import unittest

class ColregResolverTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		global VESSELS

		self.vessels	= []
		for profile in VESSELS:
			self.vessels.append( Builder.fromjson( 
				'maritime.model.vessel.PowerDrivenVessel',
				profile,
				None  ) )
			
		
		self.resolver	= ColregResolver(TargetResolver(self.vessels[0], self.vessels[1], 10))
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_Range(self):
		print( f'Situation: {self.resolver.Situation()}' )
		return

if __name__ == '__main__':
    unittest.main()
