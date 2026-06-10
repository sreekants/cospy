#!/usr/bin/python
# Filename: SkySprite.py
# Description: Sky shapes

from cos.ui.game.PolygonSprite import PolygonSprite
from shapely import Polygon, geometry
import pygame

class SkySprite(PolygonSprite):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		PolygonSprite.__init__(self, config)
		self.layer	= 4
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
				ctxt.info.append_sky( f'{self.name} (Sky)' )
		return


if __name__ == "__main__":
	test = SkySprite()


