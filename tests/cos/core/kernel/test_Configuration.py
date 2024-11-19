#!/usr/bin/python
# Filename: Configuration_test.py
# Description: Test cases for the Configuration class

from cos.core.kernel.Configuration import Configuration

import unittest

class ConfigurationTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.cfg	= Configuration('cos.ini', 'SOS_CONFIG')
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_settings(self):
		print(f'ROOT={self.cfg.get_folder("Folders","ROOT")}')
		print(f'ROOT={self.cfg.get_folder("Folders","ROOT")}')

if __name__ == '__main__':
    unittest.main()
