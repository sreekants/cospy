#!/usr/bin/python
# Filename: VectorSprite.py
# Description: Vector shapes

from cos.ui.game.Arrow import Arrow
from cos.math.geometry.Distance import Distance

import pygame

SEA_CURRENT_COLOR	= (52, 168, 251)
WIND_CURRENT_COLOR	= (170, 179, 166)
SEA_WAVE_COLOR		= (178,  34,  34)

class VectorSprite:
	def __init__(self, vector, color, layer=1):
		""" Constructor
		Arguments
			vector -- Vector to represent
			color -- Color of tthe vector
			layer -- Layer index
		"""
		P		= vector['P']
		X		= vector['X']
		norm	= Distance.norm((0.0,0.0), (X))
		if norm == None:
			self.glyph	= None
			return

		length	= 15.0
		dx		= norm[0]*length
		dy		= norm[1]*length
		if abs(dx)<4 and abs(dy)<4:
			self.glyph = None
			return

		start				= pygame.Vector2( P[0],P[1] )
		end					= pygame.Vector2( P[0]+dx,P[1]+dy )
		self.glyph			= Arrow( start, end, 1, 6, 8, color )
		self.glyph.layer	= layer
		return

	def render(self, ctxt, screen):
		""" Renders the vector
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		if self.glyph is None:
			return

		self.glyph.render( ctxt, screen )
		return


class VectorField:
	def __init__(self, config, color):
		""" Constructor
		Arguments
			config -- Configuration attributes
			color -- Color of the vector
		"""
		self.glyphs	= []
		self.guid	= config["guid"]
		self.layer	= 1
		self.color	= color

		for v in config["vectors"]:
			self.glyphs.append( VectorSprite(v, self.color) )
		return

	def update(self, ctxt, config):
		""" Updates the weather system
		Arguments
			config -- Configuration attributes
		"""
		self.glyphs.clear()
		for v in config["vectors"]:
			self.glyphs.append( VectorSprite(v, self.color) )
		return

	def render(self, ctxt, screen):
		""" Renders the vector field
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		if ctxt.layer != self.layer:
			return

		for glyph in self.glyphs:
			glyph.render( ctxt, screen )
		return


class WeatherSystem(VectorField):
	def __init__(self, config, color):
		""" Constructor
		Arguments
			config -- Configuration attributes
			color -- Color of the field
		"""
		VectorField.__init__(self, config, color)
		return

class SeaCurrentSystem(WeatherSystem):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		WeatherSystem.__init__(self, config, SEA_CURRENT_COLOR)
		return

class WindCurrentSystem(WeatherSystem):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		WeatherSystem.__init__(self, config, WIND_CURRENT_COLOR)
		return

class SeaWaveSystem(WeatherSystem):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		WeatherSystem.__init__(self, config, SEA_WAVE_COLOR)
		return


if __name__ == "__main__":
	test = VectorSprite({'P': [550.0, 110.0, 0.0], 'X': [0.7, -0.2, 0.0], 'R': [0.0, 0.0, 0.0]}, (52, 168, 251))


