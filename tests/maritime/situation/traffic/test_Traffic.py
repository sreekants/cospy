#!/usr/bin/python
# Filename: Traffic_test.py
# Description: Test cases for the Traffic class

from cos.maritime.traffic.Traffic import Traffic

import unittest

class TrafficTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.inst = Traffic()
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_upper(self):       # Sample test code
		self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
