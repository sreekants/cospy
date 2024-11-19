#!/usr/bin/python
# Filename: Vessel_test.py
# Description: Test cases for the Vessel class

from cos.core.api.Vessel import Vessel
import unittest

class VesselTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.id		= 'bedc897f-512b-45a2-aea4-bcfc248d2a8d'
		self.vessel	= Vessel()
		return
		
	@classmethod
	def tearDownClass(self):
		return
		
	def setUp(self):
		return
		
	def tearDown(self):
		return
		
	def test_describe(self):
		print( f'{self.vessel.describe(self.id)}\n' )

	def test_update(self):
		print( f'{self.vessel.update(self.id)}\n' )

	def test_bind(self):
		config = {
				"behavior":"dynamics=cos.behavior.motion.LinearMotionBehavior",
				'settings': None,
				"pose":{
					"X":[
							0,0,0,			# position 
							0,0,0,			# velocity
							0,0,0,			# acceleration
							0,0,0 			# jerk
							],
					"R":[
							90,0,0,			# orientation 
							0,0,0,			# angular velocity
							0,0,0,			# angular acceleration
							0,0,0 			# angular jerk
							]
				}
			}		
		print( f'{self.vessel.bind(self.id, config)}\n' )

	def test_init(self):
		position = {
				"bounds":{
					"type":"box",
					"points":[
							0,0,0,		# top left 
							10,100,0	# bottom right
							]
				}
			}		
		print( f'{self.vessel.init(self.id, position)}\n' )

if __name__ == '__main__':
    unittest.main()
