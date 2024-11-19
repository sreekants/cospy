#!/usr/bin/python
# Filename: Weather.py
# Description: Implementation of the Weather class

from cos.model.environment.EnvironmentService import EnvironmentService
from cos.core.kernel.Context import Context

from enum import Enum

class WeatherType(Enum):
	CLEAR_SKY			= 0x00000001,
	CLOUDY				= 0x00000008,
	FOGGY				= 0x00000010,
	LIGHT_RAIN			= 0x00001000,
	HEAVY_RAIN			= 0x00002000,
	SNOW				= 0x00004000,
	HIGH_SEA			= 0x00100000,
	WIND				= 0x00200000,
	HURRICANE			= 0x00400000

class ElementType(Enum):
	SEA_CURRENT			= 3,
	WIND_CURRENT		= 4,
	SEA_WAVE			= 5

class Weather(EnvironmentService):
	def __init__(self, world):
		""" Constructor
		Arguments
			world -- Reference ot the simulation world
		"""
		EnvironmentService.__init__(self, world, 'Weather')

		self.environ = {}
		for type in ElementType:
			self.environ[type] = []
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		EnvironmentService.on_start(self, ctxt, config)

		# Initialize the environment actors (wind, sea etc.)
		self.init_group(ctxt, self.environ, [
				(ElementType.SEA_CURRENT,	"/World/Weather/SEA_CURRENT"),
				(ElementType.WIND_CURRENT,	"/World/Weather/WIND_CURRENT"),
				(ElementType.SEA_WAVE,		"/World/Weather/SEA_WAVE")
			])
		return

	def on_timer(self, ctxt:Context, unused):
		""" Callback handling timer events
		Arguments
			ctxt -- Simulation context
			unused -- Unused variable
		"""
		self.update()
		return

	def update(self):
		""" #TODO: update
		"""
		self.update_groups(self.environ)
		return


if __name__ == "__main__":
	test = Weather()


