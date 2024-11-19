#!/usr/bin/python
# Filename: Sea_test.py
# Description: Test cases for the Sea class

from cos.core.api.Sea import Sea
import unittest

class SeaTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.sea	= Sea()
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_describe_sea_current(self):
		print( f'{self.sea.describe('sea.current')}\n' )

	def test_describe_wind_current(self):
		print( f'{self.sea.describe('wind.current')}\n' )

if __name__ == '__main__':
    unittest.main()
