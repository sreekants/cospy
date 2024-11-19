#!/usr/bin/python
# Filename: SeaWave.py
# Description: Implementation of the SeaWave class

from cos.model.environment.WeatherSystem import WeatherSystem
from cos.behavior.motion.MotionBehavior import DynamicForce

class SeaWave(WeatherSystem):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		WeatherSystem.__init__( self, DynamicForce.SEA_WAVE, config )
		return



if __name__ == "__main__":
	test = SeaWave()


