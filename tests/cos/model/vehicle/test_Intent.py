#!/usr/bin/python
# Filename: Intent_test.py
# Description: Test cases for the Intent class

from cos.model.vehicle.Intent import Intent

import unittest

class IntentTestCase(unittest.TestCase):
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
		
	def test_SET(self):
		intent	= Intent()
		intent.ADD('XXX')
		self.assertEqual(len(intent), 1)
		intent.ADD('XXX')
		self.assertEqual(len(intent), 1)

	def test_DEL(self):
		intent	= Intent()
		intent.DEL('XXX')
		self.assertEqual(len(intent), 0)
		intent.ADD('XXX')
		self.assertEqual(len(intent), 1)
		intent.DEL('XXX')
		self.assertEqual(len(intent), 0)
		intent.DEL('XXX')
		self.assertEqual(len(intent), 0)

	def test_HAS(self):
		intent	= Intent()
		intent.ADD('XXX')
		self.assertEqual(intent.HAS('XXX'), True)
		self.assertEqual(intent.HAS('YYY'), False)

	def test_IN(self):
		intent	= Intent()
		intent.ADD('XXX')
		self.assertEqual(intent.IN(['XXX']), True)
		self.assertEqual(intent.IN(['YYY']), False)
		self.assertEqual(intent.IN(['XXX','YYY']), True)
		self.assertEqual(intent.IN(['ZZZ','YYY']), False)

	def test_IN_MULTIPLE(self):
		intent	= Intent()
		intent.ADD('XXX')
		intent.ADD('AAA')
		self.assertEqual(intent.IN(['XXX']), True)
		self.assertEqual(intent.IN(['YYY']), False)
		self.assertEqual(intent.IN(['XXX','YYY']), True)
		self.assertEqual(intent.IN(['ZZZ','YYY']), False)

	def test_IS(self):
		intent	= Intent()
		intent.ADD('XXX')
		self.assertEqual(intent.IS(['XXX']), True)
		self.assertEqual(intent.IS(['X*']), True)
		self.assertEqual(intent.IS(['YYY']), False)
		self.assertEqual(intent.IS(['Y*']), False)
		self.assertEqual(intent.IS(['XXX','YYY']), False)
		self.assertEqual(intent.IS(['ZZZ','YYY']), False)

	def test_IS_MULTIPLE(self):
		intent	= Intent()
		intent.ADD('XXX')
		intent.ADD('AAA')
		intent.ADD('BBB')
		self.assertEqual(intent.IS(['XXX']), True)
		self.assertEqual(intent.IS(['YYY']), False)
		self.assertEqual(intent.IS(['XXX','YYY']), False)
		self.assertEqual(intent.IS(['ZZZ','YYY']), False)
		self.assertEqual(intent.IS(['XXX','AAA']), True)
		self.assertEqual(intent.IS(['X*','A*']), True)

if __name__ == '__main__':
    unittest.main()
