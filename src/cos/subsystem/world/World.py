#!/usr/bin/python
# Filename: World.py
# Description: Class that holds the entire universe of objects in the simulation

from cos.core.kernel.CompositeService import CompositeService
from cos.core.kernel.Service import Service
from cos.core.kernel.Context import Context
from cos.core.simulation.Simulation import Simulation
from cos.core.simulation.CollisionDetector import CollisionDetector
from cos.model.environment.Environment import Environment
from cos.model.environment.Weather import Weather
from cos.model.environment.Actors import Actors
from cos.model.environment.Scales import Scales

class World(CompositeService):
	def __init__(self):
		""" Constructor
		Arguments
			"""
		CompositeService.__init__(self, "Kernel", "World")

		# Set the instance world right away so it is accessible
  		# to other packages as it loads
		Simulation.instance().world	= self

		self.collider	= None

		self.environ	= self.add_component( Environment(self) )
		self.actors		= self.add_component( Actors(self) )
		self.weather	= self.add_component( Weather(self) )
		self.scales		= Scales()
		return

	@property
	def sim(self):
		""" Returns the simulation object
		"""
		return self.environ.sim

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		ctxt.sim.world	= self

		# Setup the physics modules
		self.collider	= CollisionDetector([
							ctxt.sim.objects.get_all("/World/Land")
							])

		CompositeService.on_start(self, ctxt, config)
		return

	def init(self, obj):
		""" Initializes an object
		Arguments
			obj -- Object to initialize
		"""
		self.actors.init(obj)
		return

	def has_collision(self, rect):
		""" Checks for collisions in an area
		Arguments
			rect -- Bounding area of interest
		"""
		return self.collider.has_collision(rect)

	def add( self, type, obj ):
		""" Adds an object
		Arguments
			type -- Type of the object
			obj -- Reference to the object
		"""
		if obj == None:
			return None
		# TODO:  REMOVE

		return obj


	def play(self):
		""" Runs the simulation logic
		"""
		return self.actors.play()

	def describe( self, type ):
		""" Describes a class of objects in the simulation
		Arguments
			type -- Type of the object
		"""
		if type == "world":
			return self.environ.get_world()
		if type == "vessels":
			return self.environ.get_vessels()
		if type == "land":
			return self.environ.get_land()
		if type == "sea":
			return self.environ.get_sea()
		if type == "sky":
			return self.environ.get_sky()
		if type == "sea.current":
			return self.environ.encode_object("sea.current","sea.current")
		if type == "wind.current":
			return self.environ.encode_object("wind.current","wind.current")
		if type == "sea.wave":
			return self.environ.encode_object("sea.wave","sea.wave")
		return {}

	def get_objects(self, type):
		""" Returns all object of a particular type
		Arguments
			type -- Type of the object
		"""
		return self.environ.get_objects(type)


if __name__ == "__main__":
	test = World()


