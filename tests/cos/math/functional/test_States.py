#!/usr/bin/python
# Filename: States_test.py
# Description: Test cases for the States class

from cos.math.functional.States import States

import unittest

class StatesTestCase(unittest.TestCase):
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
		
	def test_load(self):
		test = States()
		test.load('device.json')
		self.assertEqual(test('A*'), '110')
		self.assertEqual(test('B*'), '0')


if __name__ == '__main__':
    unittest.main()
