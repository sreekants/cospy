#!/usr/bin/python
# Filename: Logger_test.py
# Description: Test cases for the Logger class

from cos.core.kernel.Logger import Logger

import unittest

class LoggerTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.log = Logger("test.s3db")
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_error(self):
		self.log.error("COLREG.Rule1", "Failed on ship 1")

	def test_warning(self):
		self.log.warning("COLREG.Rule1", "Failed on ship 1")

	def test_info(self):
		self.log.info("COLREG.Rule1", "Failed on ship 1")

if __name__ == '__main__':
    unittest.main()
