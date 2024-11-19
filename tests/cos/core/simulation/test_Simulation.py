#!/usr/bin/python
# Filename: Simulation_test.py
# Description: Test cases for the Simulation class

from cos.core.simulation.Simulation import Simulation
from cos.core.simulation.Logger import Logger

import unittest

class SimulationTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.sim = Simulation.instance()
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_folders(self):
		self.sim.folders.clear()
		self.sim.folders["XXX"]	= "YYY"
		self.assertEqual( len(self.sim.folders), 1 )

	def test_subsystems(self):
		self.sim.set_component("NetworkLogger", Logger(None) )
		print( self.sim.get_component("NetworkLogger") )

	def test_start(self):
		self.sim.start()
		self.sim.stop()

if __name__ == '__main__':
    unittest.main()
