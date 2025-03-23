#!/usr/bin/python
# Filename: Pipeline_test.py
# Description: Test cases for the Pipeline class

from cos.math.functional.Pipeline import Pipeline
from cos.math.functional.Interpolate import Interpolate
from cos.math.functional.Range import Range

import unittest

class PipelineTestCase(unittest.TestCase):
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
		test = Pipeline()
		test.append( Interpolate((-40,0), (-40,32)) )
		test.append( Range((0, 40)) )

		self.assertEqual( test(0), 32 )			#  32F
		self.assertEqual( test(-40), 0 )		# -40F mapped to min range
		self.assertEqual( test(80), 40 )		# 176F mapped to max range



if __name__ == '__main__':
    unittest.main()
