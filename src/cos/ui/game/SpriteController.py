#!/usr/bin/python
# Filename: SpriteController.py
# Description: Implementation of a controller for a sprite behavior.

from cos.core.simulation.Actor import Actor
from cos.core.kernel.Context import Context
from cos.core.simulation.Simulation import Simulation

class SpriteController:
	def __init__(self, sprite, config):
		""" Constructor
		Arguments
			sprite -- Reference to the sprite
			config -- Configuration attributes
		"""
		# Set the behavior
		ctxt			= Context( Simulation.instance() )
		self.guid		= config["guid"]
		self.actor		= Actor(ctxt, config)
		self.actor.create( ctxt, None, config)
		return

	def get_position(self):
		""" Returns the position of the sprite
		"""
		return self.actor.get_position()

	def init( self, rect ):
		""" Initializes the sprite
		Arguments
			rect -- Rectangle of the sprite
		"""
		return self.actor.init(rect)

	def update(self, world):
		""" Updates the sprite
		Arguments
			world -- Reference ot the simulation world
		"""
		return self.actor.update(world)



if __name__ == "__main__":
	test = SpriteController()


