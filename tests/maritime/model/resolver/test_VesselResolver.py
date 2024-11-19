#!/usr/bin/python
# Filename: VesselResolver_test.py
# Description: Test cases for the VesselResolver class

from maritime.model.vessel.Builder import Builder
from maritime.model.resolver.VesselResolver import OwnShipResolver
from RESOURCES import VESSELS

import unittest

class VesselResolverTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		global VESSELS
		self.vessel = Builder.fromjson( 
			'maritime.model.vessel.PowerDrivenVessel',
			VESSELS[0],
			None  )

		
		self.resolver	= OwnShipResolver(self.vessel)
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_Type(self):
		print( self.resolver.Type() )
		return

	def test_Position(self):
		print( f'Position: {self.resolver.resolve(None, 'OwnShip.Position')}' )
		return

	def test_Velocity(self):
		print( f'Velocity: {self.resolver.resolve(None, 'OwnShip.Velocity')}' )
		return

	def test_Acceleration(self):
		print( f'Acceleration: {self.resolver.Acceleration()}' )
		print( f'Acceleration: {self.resolver.resolve(None, 'OwnShip.Acceleration')}' )
		return

	def test_Heading(self):
		print( f'Heading: {self.resolver.resolve(None, 'OwnShip.Heading')} degrees' )
		return

	def test_EngineState(self):
		print( f'EngineState: {self.resolver.resolve(None, 'OwnShip.EngineState')}' )
		return

if __name__ == '__main__':
    unittest.main()
