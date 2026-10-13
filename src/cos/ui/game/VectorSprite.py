#!/usr/bin/python
# Filename: VectorSprite.py
# Description: Vector shapes

from cos.ui.game.Arrow import Arrow

import pygame, math

SEA_CURRENT_COLOR	= (52, 168, 251)
WIND_CURRENT_COLOR	= (170, 179, 166)
SEA_WAVE_COLOR		= (178,  34,  34)

ARROW_SCALE			= 5.0		# Pixels per sqrt(m/s) of the vector's magnitude
ARROW_MIN			= 8.0		# Pixels; one arrow head, so weak fields still show their direction
ARROW_MAX			= 48.0		# Pixels

class VectorSprite:
	def __init__(self, vector, color, layer=1):
		""" Constructor
		Arguments
			vector -- Vector to represent
			color -- Color of tthe vector
			layer -- Layer index
		"""
		P			= vector['P']
		X			= vector['X']
		magnitude	= math.hypot( X[0], X[1] )

		self.color	= color
		self.layer	= layer
		self.at		= None
		if magnitude == 0.0:
			return

		# Arrows are sized in pixels so they read the same at any map scale; sqrt keeps strong fields on screen
		self.at		= ( P[0], P[1] )
		self.dir	= pygame.Vector2( X[0]/magnitude, X[1]/magnitude )
		self.length	= min( ARROW_MAX, max(ARROW_MIN, ARROW_SCALE*math.sqrt(magnitude)) )
		return

	def render(self, ctxt, screen):
		""" Renders the vector
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		if (self.at is None) or (ctxt.layer != self.layer):
			return

		start	= pygame.Vector2( ctxt.encoder.transform_point(self.at)[:2] )
		Arrow( start, start + self.dir*self.length, 1, 6, 8, self.color ).draw( screen )
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
		self.layer	= 9
		self.color	= color

		for v in config["vectors"]:
			self.glyphs.append( VectorSprite(v, self.color, self.layer) )
		return

	def update(self, ctxt, config):
		""" Updates the weather system
		Arguments
			config -- Configuration attributes
		"""
		self.glyphs.clear()
		for v in config["vectors"]:
			self.glyphs.append( VectorSprite(v, self.color, self.layer) )
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


