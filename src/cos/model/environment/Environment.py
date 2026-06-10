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
		self.files		= {}
		return

	def set_background(self, image):
		self.files['background']	= image
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
		""" Returns the word description
		"""
		return {
			"type":"world",
			"objects":{
				"vessels": self.get_objects("vessel"),
				"geography":self.get_geography()
			}
		}

	def get_geography(self):
		""" Returns the geography of the world
		"""
		return {
				"sea": self.get_objects("sea"),
				"sky": self.get_objects("sky"),
				"land": self.get_objects("land")
				}

	def encode_object(self, category, type):
		""" Helper funciton to encode an object
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

	def get_background(self):
		""" Returns an image background for the front end
		"""
		return	self.files.get('background', None)

	def get_vessels(self):
		""" Returns objects in the environment of type - vessels
		"""
		return self.encode_object( "vessels", "vessel" )

	def get_sea(self):
		""" Returns objects in the environment of type - sea
		"""
		return self.encode_object( "sea", "sea" )

	def get_land(self):
		""" Returns objects in the environment of type - land
		"""
		return self.encode_object( "land", "land" )

	def get_sky(self):
		""" Returns objects in the environment of type - sky
		"""
		return self.encode_object( "sky", "sky" )

	def get_objects(self, type):
		""" Returns objects in the simulation of a type 
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
		""" Returns an object of a parciruclar type
		Arguments
			namespace -- Type namespace
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


