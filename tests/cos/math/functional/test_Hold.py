#!/usr/bin/python
# Filename: Hold_test.py
# Description: Test cases for the Hold class

from cos.math.functional.Hold import Hold

import numpy as np
import unittest

class HoldTestCase(unittest.TestCase):
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
		
	def test_hold(self):
		test = Hold(10)

		self.assertEqual( test(np.nan), 10 )
		self.assertEqual( test(1), 1 )
		self.assertEqual( test(2), 2)
		self.assertEqual( test(np.nan), 2 )
		self.assertEqual( test(5), 5 )

if __name__ == '__main__':
    unittest.main()
