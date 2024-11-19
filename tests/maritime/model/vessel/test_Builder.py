#!/usr/bin/python
# Filename: Builder_test.py
# Description: Test cases for the Builder class

from maritime.model.vessel.Builder import Builder
from RESOURCES import VESSELS

import unittest


class BuilderTestCase(unittest.TestCase):
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
		
	def test_fromjson(self):
		global VESSELS
		for profile in VESSELS:
			vessel = Builder.fromjson( 
				'maritime.model.vessel.PowerDrivenVessel',
				profile,
				None  )
			print( vessel )
		
		return


if __name__ == '__main__':
    unittest.main()
