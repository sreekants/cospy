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
		
		self.momentum	= physics['momentum']
		self.draft		= physics['draft'] 	


		maneuver = config.get('maneuverability',None)
		if maneuver:
			self.max_yaw_rate 	= maneuver['max_yaw_rate']  # degrees per timestep


		self.__load_behavior(config)
		self.__load_activity(config)
		self.__load_cargo(config)
		return config

	def __load_cargo(self, config):
		cargo = config.get('cargo',None)

		self.cargo_flammable		= cargo['flammable'] if cargo else False
		self.cargo_refrigerated		= cargo['refrigerated'] if cargo else False
		self.cargo_livestock		= cargo['livestock'] if cargo else False
		self.cargo_biohazard		= cargo['biohazard'] if cargo else False
		self.cargo_heavy_lift		= cargo['heavy_lift'] if cargo else False
		self.cargo_hazardous		= cargo['hazardous'] if cargo else False
		self.cargo_bulk_solid		= cargo['bulk_solid'] if cargo else False
		self.cargo_bulk_liquid		= cargo['bulk_liquid'] if cargo else False
		self.cargo_liquid_gas		= cargo['liquid_gas'] if cargo else False
		self.cargo_containerized	= cargo['containerized'] if cargo else False
		self.cargo_general_cargo	= cargo['general_cargo'] if cargo else False

	def __load_activity(self, config):
		# Setup activities
		activity = config.get('activity',None)
		if activity:
			self.type 		= activity['type']  
			self.activity 	= activity['activity']  

		activity = config.get('fishing',None)
		if activity:
			self.fishing_aft_dist 	= activity['fishing_aft_dist']  # metres; min distance from aft of any vessel while fishing

		return

	def __load_behavior(self, config):
		b = config.get('behavior',None)

		self.tss_min_dist     	= 0.0 if not b else b['tss_min_dist']  		# metres; normal separation inside tss
		self.overtake_lat_min 	= 0.0 if not b else b['overtake_lat_min']  	# metres; lateral separation while overtaking
		self.tss_angle_tol    	= 0.0 if not b else b['tss_angle_tol']   	# degrees; tolerance before lane correction kicks in

		self.crossing_aft_min	= 0.0 if not b else b['crossing_aft_min']  	# metres; crossing at aft of tss vessel
		self.crossing_fore_min	= 0.0 if not b else b['crossing_fore_min'] 	# metres; crossing in front of approaching tss vessel

		self.range_visibility 	= 0.0 if not b else b['range_visibility'] 
		self.range_ample_time 	= 0.0 if not b else b['range_ample_time'] 
		self.range_safety 		= 0.0 if not b else b['range_safety'] 
		
		self.stop_on_traffic	= False if not b else b['stop_on_traffic']
		return

if __name__ == "__main__":
	test = VesselModel()

