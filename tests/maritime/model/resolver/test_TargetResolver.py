#!/usr/bin/python
# Filename: VesselResolver_test.py
# Description: Test cases for the VesselResolver class

from maritime.model.vessel.Builder import Builder
from maritime.model.resolver.TargetResolver import TargetResolver
from RESOURCES import VESSELS

import unittest

class VesselResolverTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		global VESSELS

		self.vessels	= []
		for profile in VESSELS:
			self.vessels.append( Builder.fromjson( 
				'maritime.model.vessel.PowerDrivenVessel',
				profile,
				None  ) )
			
		
		self.resolver	= TargetResolver(self.vessels[0], self.vessels[1], 10)
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_Range(self):
		print( f'InRange: {self.resolver.resolve(None, '(OwnShip,TargetShip).InRange')}' )
		print( f'InRange: {self.resolver.InRange()}' )
		print( f'OutOfRange: {self.resolver.resolve(None, '(OwnShip,TargetShip).OutOfRange')}' )
		return

	def test_Approach(self):
		print( f'Approach: {self.resolver.resolve(None, '(OwnShip,TargetShip).Approach')}' )
		return

if __name__ == '__main__':
    unittest.main()
