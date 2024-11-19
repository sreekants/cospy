#!/usr/bin/python
# Filename: WindCurrent.py
# Description: Implementation of the WindCurrent class

from cos.model.environment.WeatherSystem import WeatherSystem
from cos.behavior.motion.MotionBehavior import DynamicForce

class WindCurrent(WeatherSystem):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		WeatherSystem.__init__( self, DynamicForce.WIND_CURRENT, config )
		return



if __name__ == "__main__":
	test = WindCurrent()


