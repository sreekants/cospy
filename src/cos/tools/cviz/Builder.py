#!/usr/bin/python
# Filename: Builder.py
# Description: Builder class for the visualization environment

from cos.core.api.World import World as WorldService
from cos.core.api.Sea import Sea as SeaService
from cos.ui.game.VehicleSprite import VehicleSprite as Vehicle

from cos.ui.game.VesselSprite import VesselSprite as Vessel
from cos.ui.game.LandSprite import LandSprite as Land
from cos.ui.game.SeaSprite import SeaSprite as Sea
from cos.ui.game.SkySprite import SkySprite as Sky
from cos.ui.game.BoundingBox import BoundingBox
from cos.ui.game.VectorSprite import SeaCurrentSystem, WindCurrentSystem, SeaWaveSystem

import uuid

class AssetBuilder:
	def __init__(self, world):
		""" Constructor
		"""
		self.world	= world
		return
	
	def add( self, type, config ):
		""" Adds an actor to the simulation world
		Arguments
			type -- Type of the object
			config -- Configuration attributes
		"""
		# Adds an object to the world
		obj 	= None

		if type in ["vessel", "cos"]:
			obj 	= Vessel(config)
			bbox	= obj.rect
			rect	= [bbox.left, bbox.top, bbox.right-bbox.left, bbox.bottom-bbox.top]
			self.world.groups[type].append(obj)
		elif type == "land":
			obj 	= Land(config)
			rect	= None
			self.add_sorted(self.world.bodies, obj)
		elif type == "sea":
			obj 	= Sea(config)
			rect	= None
			self.add_sorted(self.world.reliefs, obj)
		elif type == "sky":
			obj 	= Sky(config)
			rect	= None
			self.add_sorted(self.world.reliefs, obj)
		elif type == "sea.current":
			obj 	= SeaCurrentSystem(config)
			rect	= None
			self.world.forces[type].append(obj)
		elif type == "wind.current":
			obj 	= WindCurrentSystem(config)
			rect	= None
			self.world.forces[type].append(obj)
		elif type == "sea.wave":
			obj 	= SeaWaveSystem(config)
			rect	= None
			self.world.forces[type].append(obj)
			return

		if obj == None:
			return None

		self.world.register(type, obj)
		return obj

	def add_sorted(self, container, obj):
		nobj	= len(container)
		if nobj == 0:
			container.append(obj)
			return
		
		ndx = 0
		for next in container:
			if obj.depth < next.depth:
				container.insert(ndx, obj)
				return

			ndx	= ndx+1

		container.append(obj)
		return

class Builder:
	def __init__(self):
		""" Constructor
		"""
		return

	def build(self, world):
		""" Builds the world
		Arguments
			world -- Reference ot the simulation world
		"""
		self.assets		= AssetBuilder(world)

		self.create_cos(world)
		self.create_environ(world)
		self.create_physics(world)
		return

	def create_environ(self, world):
		""" Builds the environment
		Arguments
			world -- Reference ot the simulation world
		"""
		worldProxy	= WorldService()
		desc 		= worldProxy.describe("world")
		objects		= desc.get("objects", None)
		self.create_actors(world, objects)
		self.create_landscape(world, objects)
		return

	def create_cos(self, world):
		""" Builds the simulation actors
		Arguments
			world -- Reference ot the simulation world
		"""
		# Create our 'COS vehicle'
		world.cos	= Vehicle({"guid":str(uuid.uuid1()).lower()})
		return

	def create_actors(self, world, objects):
		""" Builds the actors
		Arguments
			world -- Reference ot the simulation world
			objects -- Object list
		"""
		if objects == None:
			return

		for vessel in objects["vessels"]:
			self.assets.add( "vessel", vessel )
		return

	def create_landscape(self, world, objects):
		""" Builds the landscape
		Arguments
			world -- Reference ot the simulation world
			objects -- Object list
		"""
		if objects == None:
			return

		geography	= objects.get("geography", None)
		if geography == None:
			return

		for land in geography["land"]:
			self.assets.add( "land", land )

		for sea in geography["sea"]:
			self.assets.add( "sea", sea )

		for sky in geography["sky"]:
			self.assets.add( "sky", sky )

		return

	def create_physics(self, world):
		""" Builds the physics engine
		Arguments
			world -- Reference ot the simulation world
		"""
		seaProxy	= WorldService()
		for type in ["sea.current","sea.wave", "wind.current"]:
			desc 		= seaProxy.describe(type)
			objects		= desc.get("objects", None)
			if objects == None:
				continue

			systems		= objects[type]
			for sys in systems:
				self.assets.add(type, sys)
		return


if __name__ == "__main__":
	test = Builder()


