#!/usr/bin/python
# Filename: PortAuthority_test.py
# Description: Test cases for the PortAuthority class

from maritime.traffic.control.PortAuthority import PortAuthority
from maritime.traffic.control.TrafficController import Message
from maritime.model.geography.TrafficLane import TrafficLane

import unittest

class PortAuthorityTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.test = PortAuthority()
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_occupancy(self):
		# Test occupancy for a zone
		self.test.add_zone( TrafficLane( None, 'bd9d11e4-8f0a-47f3-aafb-4fa4694685f1', {
							"id": 100,
							"guid":'bd9d11e4-8f0a-47f3-aafb-4fa4694685f1',
							"name": 'Zone.10',
							"path": "100,100 100,200 400,200 400,100",
							"depth": 1000
							})
						)
		self.test.post(Message('me', 'RESERVE', 'Zone.10'))
		self.test.run(None)
		print(self.test.get_occupant('Zone.10'))

		self.test.post(Message('someone else', 'RELEASE', 'Zone.10'))
		self.test.run(None)
		print(self.test.get_occupant('Zone.10'))

		self.test.post(Message('me', 'RELEASE', 'Zone.10'))
		self.test.run(None)
		print(self.test.get_occupant('Zone.10'))

if __name__ == '__main__':
    unittest.main()
