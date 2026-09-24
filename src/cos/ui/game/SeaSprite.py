#!/usr/bin/python
# Filename: SeaSprite.py
# Description: Sea shapes

from cos.ui.game.PolygonSprite import PolygonSprite
from shapely import Polygon, geometry
import pygame

ZONE_CODES	= (200000, 400000)

class SeaSprite(PolygonSprite):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		PolygonSprite.__init__(self, config)

		# Maritime zones (2xxxxx) and traffic schemes (3xxxxx) describe regulation,
		# not water: they can be hidden without losing the map (SeaBuilder codes)
		code		= int( config.get("type", 0) or 0 )
		self.zone	= ZONE_CODES[0] <= code < ZONE_CODES[1]
		return

	def render(self, ctxt, screen):
		""" Renders the polygon unless it is a zone and zones are hidden
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		if self.zone and (getattr(ctxt, 'show_zones', True) == False):
			return

		PolygonSprite.render(self, ctxt, screen)
		return

	def commit(self, ctxt, screen):
		""" Updates the screen
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		if self.zone and (getattr(ctxt, 'show_zones', True) == False):
			return

		if self.area is not None:
			pos = ctxt.encoder.inverse_point( pygame.mouse.get_pos() )
			if self.area.contains( geometry.Point((pos[0],pos[1])) ):
				ctxt.info.append_sea( f'{self.name} (Sea)' )
		return

if __name__ == "__main__":
	test = SeaSprite()


