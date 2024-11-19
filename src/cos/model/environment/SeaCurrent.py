#!/usr/bin/python
# Filename: SeaCurrent.py
# Description: Implementation of the SeaCurrent class

from cos.model.environment.WeatherSystem import WeatherSystem
from cos.behavior.motion.MotionBehavior import DynamicForce

class SeaCurrent(WeatherSystem):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		WeatherSystem.__init__( self, DynamicForce.SEA_CURRENT, config )
		return



if __name__ == "__main__":
	test = SeaCurrent()


