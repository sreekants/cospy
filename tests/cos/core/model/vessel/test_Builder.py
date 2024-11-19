#!/usr/bin/python
# Filename: Builder_test.py
# Description: Test cases for the Builder class

from cos.model.vessel.Builder import Builder
from cos.model.vessel.Vessel import Type
from cos.core.simulation.Configuration import Configuration
import unittest

class BuilderTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.builder	= Builder()
		self.cfg	= Configuration('cos.ini', 'SOS_CONFIG')
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_Load(self):
		path = self.cfg.get_folder( "Folders", "ConfigFolder" )
		self.builder.build( f"{path}/vessel.s3db", "Type.POWER_DRIVEN" )

if __name__ == '__main__':
    unittest.main()
