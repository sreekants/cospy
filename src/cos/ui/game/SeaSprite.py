#!/usr/bin/python
# Filename: SeaSprite.py
# Description: Sea shapes

from cos.ui.game.PolygonSprite import PolygonSprite
from cos.ui.game import Palette
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
		self.code	= code
		self.zone	= ZONE_CODES[0] <= code < ZONE_CODES[1]

		# Standard blue theme (Palette): physical water is shaded by depth, zones are styled by
		# type. The colour stored with the shape is kept only for types the palette does not know.
		self.physical	= Palette.is_physical( code )
		self.style		= Palette.zone_style( code ) if self.zone else None
		if self.physical:
			self.color	= Palette.depth_colour( self.depth )
		return

	def render(self, ctxt, screen):
		""" Renders the polygon unless it is a zone and zones are hidden
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		if self.zone and (getattr(ctxt, 'show_zones', True) == False):
			return

		overlay	= getattr( ctxt, 'zone_overlay', None )
		if (self.style is None) or (overlay is None):
			PolygonSprite.render(self, ctxt, screen)		# Physical water, or an unknown type
			return

		if (self.visible == False) or (ctxt.layer != self.layer):
			return

		# Zones go onto one translucent overlay that the world blits once, below the vessels
		points			= ctxt.encoder.transform_polygon( self.array )
		fill, outline	= self.style
		if len(points) < 3:
			return
		if fill is not None:
			pygame.draw.polygon( overlay, fill, points )
		if outline is not None:
			pygame.draw.polygon( overlay, outline, points, 1 )
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


