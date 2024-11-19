#!/usr/bin/python
# Filename: DeviceManager_test.py
# Description: Test cases for the DeviceManager class

from cos.core.kernel.DeviceManager import DeviceManager
from cos.core.device.NullDevice import Creator as NullDeviceCreator
from cos.core.simulation.Simulation import Simulation

import unittest

class DeviceManagerTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.devmgr		= Simulation.instance().devices
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_register(self):
		self.devmgr.register( 'GPS', NullDeviceCreator() )

		for n in range(0,10):
			gps = self.devmgr.create('MyLoc', 'GPS', None, None)
			gps.send( 'Hello world' )

		print( '\r\n'.join(Simulation.instance().objects.dump()) )

if __name__ == '__main__':
    unittest.main()
