#!/usr/bin/python
# Filename: World.py
# Description: Class that holds the entire universe of objects in the simulation

from cos.core.kernel.CompositeService import CompositeService
from cos.core.kernel.Service import Service
from cos.core.kernel.Context import Context
from cos.core.simulation.Simulation import Simulation
from cos.core.simulation.CollisionDetector import CollisionDetector
from cos.ui.game.Config import SCREEN_WIDTH, SCREEN_HEIGHT
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

	def on_init(self, ctxt:Context, module):
		""" Callback for simulation initialization. Loads the map scale before any faculty
		loads map data, so that every builder converts map units to metres as it loads
		Arguments
			ctxt -- Simulation context
			module -- Module information
		"""
		CompositeService.on_init(self, ctxt, module)
		self.scales.load( ctxt )
		ctxt.sim.log.info( 'World', f'Map scale: {self.scales.map[0]:g} x {self.scales.map[1]:g} metres per map unit' )
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		ctxt.sim.world	= self

		# Setup the physics modules
		# Vessel range in metres: map.bounds, or the screen-sized default area scaled to metres
		background		= self.environ.get_background() or {}
		bounds			= background.get('bounds', None)
		if bounds is None:
			bounds		= (0.0, 0.0) + self.scales.transpose( (SCREEN_WIDTH, SCREEN_HEIGHT) )

		self.collider	= CollisionDetector([
							ctxt.sim.objects.get_all("/World/Land")
							], bounds )

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
		match type:
			case "world":
				return self.environ.get_world()
			case "vessels":
				return self.environ.get_vessels()
			case "land":
				return self.environ.get_land()
			case "sea":
				return self.environ.get_sea()
			case "sky":
				return self.environ.get_sky()
			case "sea.current":
				return self.environ.encode_object("sea.current","sea.current")
			case "wind.current":
				return self.environ.encode_object("wind.current","wind.current")
			case "sea.wave":
				return self.environ.encode_object("sea.wave","sea.wave")
			case "background":
				return self.environ.get_background()
		
		return {}

	def get_objects(self, type):
		""" Returns all object of a particular type
		Arguments
			type -- Type of the object
		"""
		return self.environ.get_objects(type)


if __name__ == "__main__":
	test = World()


