#!/usr/bin/python
# Filename: CollisionDetector.py
# Description: Simple 2D collision detector

from shapely import geometry

from cos.ui.game.Config import(
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

class ScreenArea:
	def __init__(self, viewarea):
		""" Constructor
		Arguments
			viewarea -- Screen viewport
		"""
		self.width	= viewarea[0]
		self.height	= viewarea[1]
		return

	def intersect(self, rect):
		""" Checks of a rectangle intersects with the screen area
		Arguments
			rect -- Rectangle to evaluate
		"""
		if self.inside(rect.topleft[0], rect.topleft[1])==False:
			return False

		if self.inside(rect.bottomleft[0], rect.bottomleft[1])==False:
			return False

		if self.inside(rect.topright[0], rect.topright[1])==False:
			return False

		if self.inside(rect.bottomright[0], rect.bottomright[1])==False:
			return False

		return True

	def inside(self, x, y):
		""" Checks if a coordinate is within the screen area
		Arguments
			x -- X coordinate
			y -- Y coordinate
		"""
		if x <0 or x > self.width:
			return False

		if y <0 or y > self.width:
			return False

		return True

class CollisionDetector:
	def __init__(self, obstructions):
		""" Constructor
		Arguments
			obstructions -- Obstructions in the simulation
		"""
		self.screen			= ScreenArea((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.obstructions	= obstructions
		return

	def has_collision(self, rect):
		""" Checss if a colision has occured in the simulation
		Arguments
			rect -- Bouding box of the body to evaluate
		"""
		# Ensure the sprite is on screen. (ie, we collide with the screen boundry)
		if self.screen.intersect(rect) == False:
			return True

		# Iterate through the obstructions in the world
		for bodies in self.obstructions:
			for body in bodies:
				if body.intersect(rect):
					return True

		return False

	def contains(self, pt):
		""" Checks if a point is enclosed in a body
		Arguments
			pt -- Point to evaluate
		"""
		for bodies in self.obstructions:
			for body in bodies:
				if body.contains(pt):
					return True
		return False

if __name__ == "__main__":
	test = CollisionDetector()


