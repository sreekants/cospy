#!/usr/bin/python
# Filename: World_test.py
# Description: Test cases for the World class

from cos.core.api.World import World
import unittest

class WorldTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.world	= World()
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
	
	def test_describe_world(self):
		print( f'{self.world.describe('world')}\n' )

	def test_describe_sea(self):
		print( f'{self.world.describe('sea')}\n' )

	def test_describe_land(self):
		print( f'{self.world.describe('land')}\n' )

	def test_describe_vessels(self):
		print( f'{self.world.describe('vessels')}\n' )


if __name__ == '__main__':
    unittest.main()
