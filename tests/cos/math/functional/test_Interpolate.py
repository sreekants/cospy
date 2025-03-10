#!/usr/bin/python
# Filename: Interpolate_test.py
# Description: Test cases for the Interpolate class

from cos.math.functional.Interpolate import Interpolate

import unittest

class InterpolateTestCase(unittest.TestCase):
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
		test = Interpolate( (-40,0), (-40,32) )

		# Celcius to Farenheit convertor
		self.assertEqual( test(0), 32 )			#  32F
		self.assertEqual( test(-40), -40 )		# -40F
		self.assertEqual( test(80), 176 )		# 176F

if __name__ == '__main__':
    unittest.main()
