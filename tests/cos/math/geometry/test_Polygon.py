#!/usr/bin/python
# Filename: Polygon_test.py
# Description: Test cases for the Polygon class

from cos.math.geometry.Polygon import Polygon
from cos.math.geometry.Distance import Distance

import unittest


class PolygonTestCase(unittest.TestCase):
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
		test = Polygon( [[0, 0], [.5,.5], [1, 0], [1, 1], [0, 1]] )
		print( test.clearance(.1,.1) )


if __name__ == '__main__':
    unittest.main()
