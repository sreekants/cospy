#!/usr/bin/python
# Filename: ObjectManager_test.py
# Description: Test cases for the ObjectManager class


from cos.core.kernel.ObjectManager import ObjectManager

import unittest

class ObjectManagerTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.om	= ObjectManager()
		self.om.register( "/Test", "StringArray", ["Foo"] )
		self.om.register( "/Test", "String", "TESTSTR" )
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return

	def test_exists(self):
		self.assertTrue( self.om.exists("/Test/String") )
		self.assertFalse( self.om.exists("/Test/???") )

	def test_register(self):
		self.assertFalse( self.om.exists("/Test/Array") )
		self.om.register( "/Test", "Array", [10, 100, 20] )
		self.assertTrue( self.om.exists("/Test/Array") )

	def test_link(self):
		self.om.link( "/Test", "Link", "/Test/String" )
		self.assertTrue( self.om.exists("/Test/Link") )
		self.assertEqual( self.om.get("/Test/Link"), "TESTSTR" )


if __name__ == '__main__':
    unittest.main()
