#!/usr/bin/python
# Filename: Circle.py
# Description: Implementation of the Circle class

import math

class Circle:
	def __init__(self, x, y, radius):
		""" Constructor
		Arguments
			x -- X coordinate
			y -- Y coordinate
			radius -- Radius of the circle
		"""
		self.x	= x
		self.y	= y
		self.r	= radius
		return

	@property
	def radius(self):
		""" Returns the radius
		"""
		return self.r

	@property
	def center(self):
		""" Returns the center
		"""
		return (self.x, self.y)

	@property
	def area(self):
		""" Returns the area
		"""
		return math.pi*self.r**2

	def encloses(self, x, y):
		""" Checks if a point is enclosed by the circle
		Arguments
			x -- X coordinate
			y -- Y coordinate
		"""
		return (math.sqrt( (x-self.x)**2 + (y-self.y)**2 ) < self.r)

if __name__ == "__main__":
	test = Circle()


