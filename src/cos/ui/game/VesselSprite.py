#!/usr/bin/python
# Filename: VesselSprite.py
# Description: Implementation of mobile vessel sprites.

from cos.ui.game.AnimatedSprite import AnimatedSprite
from cos.ui.game.Config import *
import  pygame

class VesselSprite(AnimatedSprite):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		image	= config["sprite"]
		if image==None or len(image)==0:
			image	= 'img/vessel.png'

		super(VesselSprite, self).__init__( config, image, (255, 255, 255) )

		self.name	= config["name"]
		self.id		= config["identifier"]
		self.layer	= 6
		return

	def commit(self, ctxt, screen):
		""" Renders the sprite to thescreen
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		if self.rect is not None:
			pos = pygame.mouse.get_pos()
			if self.rect.collidepoint(pos):
				text = ctxt.font.render( f'{self.name} ({pos[0]},{pos[1]})', False, (0, 0, 0))
				screen.blit( text, (100,0))
		return


if __name__ == "__main__":
	test = VesselSprite()


