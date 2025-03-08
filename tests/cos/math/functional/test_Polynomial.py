#!/usr/bin/python
# Filename: Polynomial_test.py
# Description: Test cases for the Polynomial class

from cos.math.functional.Polynomial import Polynomial
import unittest

class PolynomialTestCase(unittest.TestCase):
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
		
	def test_range2(self):
		fn = Polynomial([1, 10])
		self.assertEqual(fn(1), 11)
		self.assertEqual(fn(2), 21)

	def test_range3(self):
		fn = Polynomial([1, 10, 100])
		self.assertEqual(fn(1), 111)
		self.assertEqual(fn(2), 421)

	def test_dump(self):
		fn = Polynomial([1, 10, 100])
		self.assertEqual(str(fn), '1+10x+100x^2')

		fn = Polynomial([1, 0, 0, 5])
		self.assertEqual(str(fn), '1+5x^3')

if __name__ == '__main__':
    unittest.main()
