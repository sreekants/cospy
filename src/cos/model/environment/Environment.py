#!/usr/bin/python
# Filename: Environment.py
# Description: Implementation of the Environment class

from cos.model.environment.EnvironmentService import EnvironmentService
from cos.core.kernel.Context import Context

class Environment(EnvironmentService):
	def __init__(self, world):
		""" Constructor
		Arguments
			world -- Reference ot the simulation world
		"""
		EnvironmentService.__init__(self, world, 'Environment')

		# - self.reliefs is used for position updates
		# - self.bodies is used for rigid bodies
		self.reliefs	= []	# Traversable bodies (Sea)
		self.bodies		= []	# Obstructon bodies (Land)

		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		EnvironmentService.on_start(self, ctxt, config)

		self.sim		= ctxt.sim

		# Adds an object to the world
		self.bodies		= self.sim.objects.get_all("/World/Land")
		self.reliefs	= self.sim.objects.get_all("/World/Sea")
		return

	def get_world(self):
		""" #TODO: get_world
		"""
		return {
			"type":"world",
			"objects":{
				"vessels": self.get_objects("vessel"),
				"geography":self.get_geography()
			}
		}

	def get_geography(self):
		""" #TODO: get_geography
		"""
		return {
				"sea": self.get_objects("sea"),
				"sky": self.get_objects("sky"),
				"land": self.get_objects("land")
				}

	def encode_object(self, category, type):
		""" #TODO: encode_object
		Arguments
			category -- Category of the object
			type -- Type of the object
		"""
		return {
			"type":category,
			"objects":{
				category: self.get_objects(type)
			}
		}

	def get_vessels(self):
		""" #TODO: get_vessels
		"""
		return self.encode_object( "vessels", "vessel" )

	def get_sea(self):
		""" #TODO: get_sea
		"""
		return self.encode_object( "sea", "sea" )

	def get_land(self):
		""" #TODO: get_land
		"""
		return self.encode_object( "land", "land" )

	def get_sky(self):
		""" #TODO: get_sky
		"""
		return self.encode_object( "sky", "sky" )

	def get_objects(self, type):
		""" #TODO: get_objects
		Arguments
			type -- Type of the object
		"""
		scopes = {
			"wind.current":"/World/Weather/WIND_CURRENT",
			"sea.current":"/World/Weather/SEA_CURRENT",
			"sea.wave":"/World/Weather/SEA_WAVE",
			"vessel":"/World/Vehicle/Vessel",
			"sky":"/World/Sky",
			"sea":"/World/Sea",
			"land":"/World/Land"
		}

		return self.__get_objects_by_type( scopes[type] )

	def __get_objects_by_type(self, namespace):
		""" #TODO: __get_objects_by_type
		Arguments
			namespace -- #TODO
		"""
		if type == None:
			return []

		result		= list()
		objects		= self.sim.objects.get_all(namespace)

		for o in objects:
			result.append( o.describe() )
		return result

if __name__ == "__main__":
	test = Environment()


