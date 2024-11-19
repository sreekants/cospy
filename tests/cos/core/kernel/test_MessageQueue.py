#!/usr/bin/python
# Filename: MessageQueue_test.py
# Description: Test cases for the MessageQueue class

from cos.core.kernel.MessageQueue import MessageQueue

import unittest

class MessageQueueTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.mq = MessageQueue()
		self.mq.subscribe("/TestCount", self)
		self.mq.subscribe("/TestTopic", self)
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_push(self):
		self.mq.push("/TestTopic", "Hello World")
		self.assertGreater(self.mq.count("/TestTopic"), 0)

	def test_count(self):
		n	= self.mq.count("/TestCount")
		self.mq.push("/TestCount", "Hello World")
		self.assertEqual(self.mq.count("/TestCount"), n+1)

	def test_count2(self):
		n	= self.mq.count("/UNSUBSCRIBED")
		self.assertEqual(n, 0)
		self.mq.push("/UNSUBSCRIBED", "Hello World")
		self.assertEqual(self.mq.count("/UNSUBSCRIBED"), 0)

	def test_pop(self):
		n	= self.mq.count("/TestTopic")
		self.mq.push("/TestTopic", "Hello World")
		self.mq.pop("/TestTopic")
		self.assertEqual(self.mq.count("/TestTopic"), n)

	def test_clear(self):
		n	= self.mq.count("/TestTopic")
		self.mq.push("/TestTopic", "Hello World")
		self.mq.clear("/TestTopic")
		self.assertEqual(self.mq.count("/TestTopic"), 0)

if __name__ == '__main__':
    unittest.main()
