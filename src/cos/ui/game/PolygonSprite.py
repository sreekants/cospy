#!/usr/bin/python
# Filename: Polygon.py
# Description: Basic polygon shape

from cos.ui.game.Config import *
from shapely import Polygon, geometry
import pygame

class PolygonSprite:
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		self.id		= config["id"]
		self.guid	= config["guid"]
		self.name	= config["name"]

		visible		= config.get("visible", 'Y')
		if (visible == 'Y') or (visible == 'True'):
			self.visible	= True
		else:
			self.visible	= False

		self.depth		= config.get("depth", 0.0)

		# TODO: Opacity does not yet work. The depth needs to deal with opacity 
		# or render ordered has to be sorted by depth accordingly
		opacity		= None			
	
		self.color	= self.getcolor(config, opacity)
		self.points	= self.getpolygon(config)
		self.area	= Polygon(self.points)
		self.layer	= 0
		return

	def render(self, ctxt, screen):
		""" Renders the polygon
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		if self.visible == False:
			return
		
		if ctxt.layer != self.layer:
			return

		pygame.draw.polygon( screen, self.color, ctxt.encoder.transform_polygon(self.points) )
		return

	def update(self):
		""" Updates the polygon
		"""
		return

	def commit(self, ctxt, screen):
		""" Updates the screen
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		if self.area is not None:
			pos = pygame.mouse.get_pos()

			# TODO: To scale mouse to position
			
			if self.area.contains( geometry.Point((pos[0],pos[1])) ):
				text = ctxt.font.render( f'{self.name} ({pos[0]},{pos[1]})', False, (0, 0, 0))
				screen.blit( text, (100,0))
		return

	def getcolor(self, config, opacity=None):
		""" Returns the color of the polygon
		Arguments
			config -- Configuration attributes
			opacity -- Opacity of the sprite
		"""
		rgb		= []
		color	= config["color"][1:]
		for i in (0, 2, 4):
			decimal = int( color[i:i+2], 16 )
			rgb.append(decimal)

		if opacity is not None:
			rgb.append(opacity)
		return tuple(rgb)

	def getpolygon(self, config):
		""" Returns the polygon path
		Arguments
			config -- Configuration attributes
		"""
		path	= config["path"]
		points	= []
		for item in path.split(' '):
			pt		= item.split(',')
			points.append( (int(pt[0]), int(pt[1])) )

		return points



if __name__ == "__main__":
	test = Polygon()


