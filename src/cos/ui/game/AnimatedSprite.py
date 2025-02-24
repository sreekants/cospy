#!/usr/bin/python
# Filename: AnimatedSprite.py
# Description: Implementation of a base class for animated sprites

from cos.ui.game.Sprite import Sprite
from cos.ui.game.SpriteController import SpriteController
from cos.core.kernel.BootLoader import BootLoader
from cos.math.geometry.Rectangle import Rectangle
import pygame

BLACK=(0, 0, 0)

class AnimatedSprite(Sprite):
	def __init__(self, config, image, mask=BLACK):
		""" Constructor
		Arguments
			config -- Configuration attributes
			image -- Image of the sprite
			mask -- Mask of the sprite
		"""
		Sprite.__init__(self, config, image, mask)

		# Set the behavior
		self.control	= SpriteController( self, config )
		position		= self.control.get_position()

		if self.surf is not None:
			self.rect		= self.surf.get_rect( center=(position[0], position[1]) )
		else:
			self.rect		= pygame.Rect(position[0]-5, position[1]-5,10,10)

		self.control.init( self.rect )

		return

	def update(self, world, unused):
		""" Updates the world
		Arguments
			world -- Reference ot the simulation world
			unused -- Unused variable
		"""
		rect, state		= self.control.update(world)
		if rect == None:
			return

		self.rect	= rect
		return

if __name__ == "__main__":
	test = AnimatedSprite()


