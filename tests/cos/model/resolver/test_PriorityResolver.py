#!/usr/bin/python
# Filename: test_PriorityResolver.py
# Description: Test cases for the PriorityResolver class

from cos.model.resolver.PriorityResolver import PriorityResolver
from cos.model.resolver.Resolver import NamedResolver

import unittest

class PriorityResolverTestCase(unittest.TestCase):
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
		test = PriorityResolver( [
			(1, NamedResolver('low')),
			(11, NamedResolver('critical')), 
			(5, NamedResolver('medium')), 
			(10, NamedResolver('high')), 
			])

		# Ensure the sequence is in decreasing priority. The order of the 
		# string is how the resolver is executed.
		self.assertEqual( test.describe(), 'critical,high,medium,low' )

if __name__ == '__main__':
    unittest.main()
