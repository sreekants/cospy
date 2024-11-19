#!/usr/bin/python
# Filename: Topic_test.py
# Description: Test cases for the Topic class

from cos.core.api.Topic import Topic

import unittest

class TopicTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.topic	= Topic()
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_list(self):
		print( self.topic.echo([]) )


if __name__ == '__main__':
    unittest.main()
