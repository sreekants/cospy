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

	def test_clearance_beyond_edge(self):
		# Point on the extension of an edge, not on the edge itself
		test = Polygon( [[0, 0], [10, 0], [10, 10], [0, 10]] )
		self.assertAlmostEqual( test.clearance(100, 0), 90.0 )

	def test_clearance_duplicate_vertices(self):
		test = Polygon( [[0, 0], [0, 0], [10, 0], [10, 10], [10, 10], [0, 10]] )
		self.assertAlmostEqual( test.clearance(5, 20), 10.0 )
		self.assertAlmostEqual( test.clearance(5, 5), 5.0 )


if __name__ == '__main__':
    unittest.main()
