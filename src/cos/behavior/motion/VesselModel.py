#!/usr/bin/python
# Filename: VesselModel.py
# Description: Implementation of the VesselModel class

from cos.behavior.motion.HydrodynamicModel import Ship

import numpy as np
import yaml

class VesselModel:
	def __init__(self):
		self.ship	= None
		return
	
	def load(self, path):
		""" Loads a simulation model
		Arguments
			path -- Path to model file
		"""
		config			= yaml.safe_load( path )

		if 'hydrodynamics' in config:
			dynamics		= config['hydrodynamics']

			self.north 		= dynamics['north']
			self.east 		= dynamics['east']
			self.yaw 		= dynamics['yaw'] * np.pi/180
			self.yaw_ref 	= dynamics['yaw_ref'] * np.pi/180
			self.speed 		= dynamics['speed']
			self.speed_ref 	= dynamics['speed_ref']
			self.yaw_rate 	= dynamics['yaw_rate']
			self.dt 		= dynamics['dt']

		# Initial states
		physics			= config['physics']

		self.ship 		= Ship(mass=physics['mass'],
							linear_damping_coeff=physics['linear_damping_coeff'],
							length=physics['length'],
							width=physics['width'],
							dt=self.dt )
		
		self.momentum			= physics['momentum']


		maneuver = config.get('maneuverability',None)
		if maneuver:
			self.max_yaw_rate 	= maneuver['max_yaw_rate']  # degrees per timestep

		behavior = config.get('behavior',None)
		if behavior:
			self.tss_min_dist     	= behavior['tss_min_dist']  	# metres; normal separation inside tss
			self.overtake_lat_min 	= behavior['overtake_lat_min']  # metres; lateral separation while overtaking
			self.tss_angle_tol    	= behavior['tss_angle_tol']   	# degrees; tolerance before lane correction kicks in

			self.crossing_aft_min	= behavior['crossing_aft_min']  # metres; crossing at aft of tss vessel
			self.crossing_fore_min	= behavior['crossing_fore_min'] # metres; crossing in front of approaching tss vessel

			self.range_visibility 	= behavior['range_visibility'] 
			self.range_ample_time 	= behavior['range_ample_time'] 
			self.range_safety 		= behavior['range_safety'] 

		# Setup activities
		activity = config.get('activity',None)
		if activity:
			self.type 		= activity['type']  
			self.activity 	= activity['activity']  

		activity = config.get('fishing',None)
		if activity:
			self.fishing_aft_dist 	= activity['fishing_aft_dist']  # metres; min distance from aft of any vessel while fishing

		return config

		

if __name__ == "__main__":
	test = VesselModel()

