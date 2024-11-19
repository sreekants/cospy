#!/usr/bin/python
# Filename: BasicHydrodynamicVessel_test.py
# Description: Test cases for the BasicHydrodynamicVessel class

from cos.behavior.motion.BasicHydrodynamicBehavior import BasicHydrodynamicBehavior
from cos.math.geometry.Rectangle import Rectangle

import unittest
import matplotlib.pyplot as plt

class World:
	def __init__(self):
		return
	
	def has_collision(self, rect:Rectangle, config):
		return False
	
class BasicHydrodynamicVesselTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.world		= World()
		self.vessel		= BasicHydrodynamicBehavior({
				
							})
		self.vessel.load("config.yaml")
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_move(self):
		ticks = int((5*60)/0.01)
		for tick in range(0, ticks):
			bbox	= self.vessel.move( self.world, tick, None)

	def test_plot(self):
		# Plot
		plt.figure(figsize=(8, 8))  # Set the figure size
		plt.plot( self.vessel.easts, self.vessel.norths, linestyle='-')
		plt.title('Ship Position')
		plt.xlabel('East Position')
		plt.ylabel('North Position')
		plt.gca().set_aspect('equal', adjustable='box')  # Set equal aspect ratio
		plt.grid(True)

		plt.figure(2)
		plt.plot( self.vessel.time, self.vessel.speeds )
		plt.title('Forward Speed Over Time')
		plt.xlabel('Time')
		plt.ylabel('Forward Speed')
		plt.grid(True)

		plt.figure(2)
		plt.plot(self.vessel.time, self.vessel.speeds)
		plt.show()
		return
	
if __name__ == '__main__':
    unittest.main()
