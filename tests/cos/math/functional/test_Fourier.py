#!/usr/bin/python
# Filename: Fourier_test.py
# Description: Test cases for the Fourier class

from cos.math.functional.Fourier import Fourier
import numpy as np
import unittest

class FourierTestCase(unittest.TestCase):
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
		
	def test_fourier(self):
		test = Fourier([2.0])
		print(test(1.0))
		print(2.0*np.cos(np.pi/2.0))


if __name__ == '__main__':
    unittest.main()
