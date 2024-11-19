#!/usr/bin/python
# Filename: Shape.py
# Description: Implementation of the Shape class

from cos.core.kernel.Object import Object
from cos.core.kernel.Context import Context

from cos.math.geometry.Polygon import Polygon
from shapely import geometry


class Shape(Object):
	def __init__(self, ctxt:Context, category, type, id, config):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			category -- Category of the object
			type -- Type of the object
			id -- Unique identifier
			config -- Configuration attributes
		"""
		if id == None:
			id	= self.__class__.__name__

		scope	= f'{category}/{type}'

		Object.__init__( self, scope, id, id )

		self.type	= type
		self.config = config
		self.points	= self.get_polygon(ctxt, config)
		self.area	= Polygon(self.points)
		return

	def describe(self):
		""" Describes the shape
		"""
		return self.config

	def get_polygon(self, ctxt:Context, config):
		""" Returns the polygon of the shape
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		scale	= ctxt.sim.world.scales.map
		path	= config["path"]
		points	= []
		for item in path.split(' '):
			pt		= item.split(',')
			points.append( (int(pt[0]), int(pt[1])) )

		return points


	def intersect(self, shape):
		""" Checks the bounding box of another shape is contained within this shape
		Arguments
			shape -- Shape with a bounding box to compare
		"""
		# Iterate through the obstructions in the world
		if self.area.contains(geometry.Point(shape.topleft)) or \
		   self.area.contains(geometry.Point(shape.topright)) or \
		   self.area.contains(geometry.Point(shape.bottomleft)) or \
		   self.area.contains(geometry.Point(shape.bottomright)):
				return True

		return False

	def contains(self, pt):
		""" Checks if a point is within the shape
		Arguments
			pt -- Point to validate
		"""
		if self.area.contains(geometry.Point(pt)):
			return True

		return False

if __name__ == "__main__":
	test = Shape()


