#!/usr/bin/python
# Filename: WeatherBuilder.py
# Description: Implementation of the WeatherBuilder class

from cos.model.environment.Builder import Builder
from cos.model.environment.Weather import ElementType
from cos.core.kernel.Context import Context
from cos.core.kernel.BootLoader import BootLoader
from cos.core.utilities.ActiveRecord import ActiveRecord
from cos.core.utilities.ArgList import ArgList

class WeatherBuilder(Builder):
	def __init__(self, args:dict):
		""" Constructor
		Arguments
			args -- List of arguments
		"""
		Builder.__init__(self, "Builder/Environment", args["Type"], None, None,
			{
			"SEA_CURRENT": (ElementType.SEA_CURRENT, "cos.model.environment.SeaCurrent", 'sea_current', 'sea_currents'),
			"WIND_CURRENT": (ElementType.WIND_CURRENT, "cos.model.environment.WindCurrent", 'wind_current', 'wind_currents'),
			"SEA_WAVE": (ElementType.SEA_WAVE, "cos.model.environment.SeaWave", 'sea_wave', 'sea_waves')
			} )

		return

	def build(self, ctxt:Context, args:ArgList, path:str, type:str):
		""" #TODO: build
		Arguments
			ctxt -- Simulation context
			args -- List of arguments
			path -- #TODO
			type -- Type of the object
		"""
		profile	= self.prototypes[type]
		db		= ActiveRecord.create(profile[2], path, profile[3])

		klassname, klass	= BootLoader.load_class( profile[1] )

		category	= Builder.capitalize(profile[2])
		inst		= klass( profile )
		inst.load( ctxt, args, db.get_all(), path )

		ctxt.sim.objects.register( f'/World/Weather/{type}', inst.id, inst )
		return inst



if __name__ == "__main__":
	test = WeatherBuilder()


