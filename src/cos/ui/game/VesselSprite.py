#!/usr/bin/python
# Filename: VesselSprite.py
# Description: Implementation of mobile vessel sprites.

from cos.ui.game.AnimatedSprite import AnimatedSprite
from cos.ui.game.Config import *
import  pygame, math

AQUABLUE=(57, 196, 242)
BARBIEPINK=(240, 95, 92)

class VesselIcon(AnimatedSprite):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		super(VesselIcon, self).__init__( config, None, (255, 255, 255) )

		self.name	= config["name"]
		self.id		= config["identifier"]
		self.layer	= 6

		self.initialize()
		return
	
	def initialize(self, length=15, width=10, bowlen=4, color=AQUABLUE):
		self.length		= length
		self.width		= width
		self.bowlen		= bowlen
		self.color		= color
		return

	def render_at(self, ctxt, screen:pygame.Surface, rect:pygame.Rect):
		""" Renders the sprite to the screen at a position
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
			rect -- Bounding rectangle of the image
		"""
		self.render_polygon(screen, rect.center, self.angle)
		return


	def render_polygon(self, surface:pygame.Surface, pos, angle):
		points = []

		left		= -self.length/2
		top			= -self.width/2
		right		= self.length/2
		bottom		= self.width/2

		# Build the polygon shape by transforming it around the center
		points.append(self.rotxfrm(pos, left, top+2, angle))
		points.append(self.rotxfrm(pos, left, bottom-2, angle))
		points.append(self.rotxfrm(pos, right,bottom, angle))
		points.append(self.rotxfrm(pos, right+3,bottom-1, angle))
		points.append(self.rotxfrm(pos, self.length+self.bowlen, 0, angle))
		points.append(self.rotxfrm(pos, right+3,top+1, angle))
		points.append(self.rotxfrm(pos, right, top, angle))

		# Render the polygon
		pygame.draw.polygon(surface, self.color, points)
		pygame.draw.lines(surface, (64, 64, 64), True, points)
		return

	def rotxfrm(self, pivot, x, y, angle):
		deg			= -math.radians(angle)
		r			= math.sqrt(x**2+y**2)
		theta		= math.atan2(y, x)
		return [ pivot[0]+r*math.cos(theta+deg), pivot[1]+r*math.sin(theta+deg) ]

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


