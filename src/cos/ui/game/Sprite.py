#!/usr/bin/python
# Filename: Sprite.py
# Description: Base class for all sprite

import pygame

from pygame.locals import (
    RLEACCEL
)

BLACK =(0,0,0)

# Define the Player object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Sprite(pygame.sprite.Sprite):
	def __init__(self, config, image, mask=BLACK):
		""" Constructor
		Arguments
			config -- Configuration attributes
			image -- Image of the sprite
			mask -- Mask to apply for the sprite
		"""
		pygame.sprite.Sprite.__init__(self)

		if image is None:
			self.orig = None
		else:
			self.orig = pygame.image.load(image).convert()
			self.orig.set_colorkey(mask, RLEACCEL)

		self.surf		= self.orig
		self.center		= None
		self.rect		= None
		self.guid		= config["guid"]
		self.layer		= 0
		self.angle		= 0
		self.zoom		= 1
		self.mask		= mask
		return

	def prepare(self, ctxt, screen):
		""" Prepares the sprite
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		return

	def commit(self, ctxt, screen):
		""" Renders the sprite to the memory buffer
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		return

	def render(self, ctxt, screen):
		""" Renders the sprite to the screen
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		if ctxt.layer != self.layer:
			return

		if self.rect is not None:
			self.render_at( ctxt, screen, ctxt.encoder.transform_rect(self.rect) )
		return

	def render_at(self, ctxt, screen, rect):
		""" Renders the sprite to the screen at a position
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
			rect -- Bounding rectangle of the image
		"""
		if rect is not None:
			screen.blit(self.surf, rect)
		return
	
	def rotate(self, angle):
		""" Rotates the sprite
		Arguments
			angle -- Angle to rotate
		"""
		if self.angle == angle:
			return
		self.angle	= angle

		if self.orig is not None:	
			self.surf = pygame.transform.rotozoom(self.orig, self.angle, self.zoom)
			self.surf.set_colorkey(self.mask, RLEACCEL)
		return

	def scale(self, size):
		""" Rotates the sprite
		Arguments
			size -- Size to scale
		"""
		if self.zoom == size:
			return
		self.zoom	= size

		if self.orig is not None:	
			self.surf = pygame.transform.rotozoom(self.orig, self.angle, self.zoom)
			self.surf.set_colorkey(self.mask, RLEACCEL)
		return

	def get_rect(self):
		""" Returns the rectangle of the sprite
		"""
		return self.surf.get_rect()

if __name__ == "__main__":
	test = Sprite()


