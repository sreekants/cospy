#!/usr/bin/python
# Filename: Polygon.py
# Description: Implementation of the Polygon class

import shapely

class Polygon:
	def __init__(self, points):
		""" Constructor
		Arguments
			points -- Points of the polygon
		"""
		self.geom	= shapely.Polygon(points)
		return

	def encloses(self, x, y):
		""" Checks if a point is enclosed by the polygon
		Arguments
			x -- X coordinate
			y -- Y coordinate
		"""
		return self.geom.contains( shapely.Point(x, y) )

	def contains(self, p):
		""" Checks if a point is enclosed by the polygon
		Arguments
			p -- Point reference
		"""
		return self.geom.contains(p)


	def clearance(self, x, y):
		""" Shortest distance from a point to the polygon exterior
		Arguments
			x -- X coordinate
			y -- Y coordinate
		"""
		return self.geom.exterior.distance( shapely.Point(x, y) )

	@property
	def vertices(self):
		return tuple(self.geom.exterior.coords)

	@property
	def bounds(self):
		return self.geom.bounds

if __name__ == "__main__":
	test = Polygon( [[0, 0], [1, 0], [1, 1], [0, 1]] )


