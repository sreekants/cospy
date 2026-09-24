#!/usr/bin/python
# Filename: CollisionDetector.py
# Description: Simple 2D collision detector

from shapely import geometry

from cos.ui.game.Config import(
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

class ScreenArea:
	def __init__(self, viewarea, origin=(0, 0)):
		""" Constructor
		Arguments
			viewarea -- Size of the area (width, height)
			origin -- Top left corner of the area
		"""
		self.left	= origin[0]
		self.top	= origin[1]
		self.width	= viewarea[0]
		self.height	= viewarea[1]
		return

	@staticmethod
	def from_bounds(bounds):
		""" Creates an area from (left, top, right, bottom) bounds
		Arguments
			bounds -- Bounds of the area
		"""
		left, top, right, bottom	= bounds
		return ScreenArea( (right-left, bottom-top), (left, top) )

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
		if x < self.left or x > self.left+self.width:
			return False

		if y < self.top or y > self.top+self.height:
			return False

		return True

class CollisionDetector:
	def __init__(self, obstructions, bounds=None):
		""" Constructor
		Arguments
			obstructions -- Obstructions in the simulation
			bounds -- (left, top, right, bottom) area vessels may move in. Defaults
				to the screen size, which is what maps without map.bounds were drawn for
		"""
		if bounds is None:
			self.screen		= ScreenArea((SCREEN_WIDTH, SCREEN_HEIGHT))
		else:
			self.screen		= ScreenArea.from_bounds(bounds)
		self.obstructions	= obstructions
		return

	def has_collision(self, rect):
		""" Checss if a colision has occured in the simulation
		Arguments
			rect -- Bouding box of the body to evaluate
		"""
		# Ensure the sprite is within the map bounds (ie, we collide with the boundary)
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


