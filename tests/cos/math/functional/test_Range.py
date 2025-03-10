#!/usr/bin/python
# Filename: Range_test.py
# Description: Test cases for the Range class

from cos.math.functional.Range import Range
import unittest

class RangeTestCase(unittest.TestCase):
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
		
	def test_range(self):
		test = Range((5, 10))

		self.assertEqual( test(0), 5 )		#  5
		self.assertEqual( test(8), 8 )		#  8
		self.assertEqual( test(10), 10 )	# 10
		self.assertEqual( test(11), 10 )	# 10


if __name__ == '__main__':
    unittest.main()
