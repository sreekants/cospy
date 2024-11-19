#!/usr/bin/python
# Filename: Polygon.py
# Description: Implementation of the Polygon class

from cos.math.geometry.Distance import Distance

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
		""" Shortest distance from a point to the a line in the polygon exterior
		Arguments
			x -- X coordinate
			y -- Y coordinate
		""" 
		
		p			= (x, y)
		V			= tuple(self.geom.exterior.coords)
		nedges		= len(V)
		if nedges < 2:
			return 0.0
		
		start		= V[0]
		P1		 	= (start[0], start[1])
		distance	= float('infinity')

		for i in range(1, nedges):
			e		= V[i%nedges]	# Next edge is modulo(i+1)
			P2	 	= (e[0], e[1])
			d		= Distance.point_to_line( p, P1, P2 )
			if d < distance:
				distance	= d

			P1		= P2

		return distance

	@property
	def vertices(self):
		return tuple(self.geom.exterior.coords)

	@property
	def bounds(self):
		return self.geom.bounds

if __name__ == "__main__":
	test = Polygon( [[0, 0], [1, 0], [1, 1], [0, 1]] )


