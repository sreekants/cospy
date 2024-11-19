#!/usr/bin/python
# Filename: Vessel_test.py
# Description: Test cases for the Vessel class

from RESOURCES import VESSELS

import unittest

class VesselTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
