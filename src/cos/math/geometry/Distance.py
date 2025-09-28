#!/usr/bin/python
# Filename: Distance.py
# Description: Implementation of the distance functions

import math

class Distance:
	def __init__(self):
		""" Constructor
		"""
		return

	@staticmethod
	def euclidean(x1, x2):
		""" Returns euclidean distance
		Arguments
			x1 -- Start point
			x2 -- End point
		"""
		return math.sqrt( (x1[0]-x2[0])**2 + (x1[1]-x2[1])**2 )

	@staticmethod
	def euclidean_squared(x1, x2):
		""" Returns euclidean squared distance
		Arguments
			x1 -- Start point
			x2 -- End point
		"""
		return (x1[0]-x2[0])**2 + (x1[1]-x2[1])**2

	@staticmethod
	def manhattan(x1, x2):
		""" Returns manhattan distance
		Arguments
			x1 -- Start point
			x2 -- End point
		"""
		return abs(x1[0]-x2[0]) + abs(x1[1]-x2[1])

	@staticmethod
	def diagonal(x1, x2, D=1.0, D2=1.0):
		""" Returns diagonal distance
		Arguments
			x1 -- Start point
			x2 -- End point
			D -- #TODO
			D2 -- #TODO
		"""
		dx = abs(x1[0] - x2[0])
		dy = abs(x1[1] - x2[1])
		return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

	@staticmethod
	def chebyshev(x1, x2):
		""" Returns the chebyshev distance
		Arguments
			x1 -- Start point
			x2 -- End point
		"""
		return Distance.diagonal(x1, x2, 1.0, 1.41421356237)

	@staticmethod
	def octile(x1, x2):
		""" Returns the octile distance
		Arguments
			x1 -- Start point
			x2 -- End point
		"""
		return Distance.diagonal(x1, x2, 1.0, 2.0)

	@staticmethod
	def norm(x1, x2):
		""" Returns the normized distance
		Arguments
			x1 -- Start point
			x2 -- End point
		"""
		dx		= x2[0]-x1[0]
		dy		= x2[1]-x1[1]
		length	= math.sqrt((dx)**2 + (dy)**2)
		if length == 0.0:
			return (0.0, 0.0)

		return (dx/length, dy/length)

	@staticmethod
	def point_to_line(p, P1, P2):
		""" Distance from a point to a line
		Arguments
			p -- Point from which to measure distance
			P1 -- Start point of the line
			P2 -- End point of the line
		""" 
		# Refer: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
		# Topic: Line defined by two points

		x0		= p[0]
		y0		= p[1]
		x1		= P1[0]
		y1		= P1[1]
		x2		= P2[0]
		y2		= P2[1]
		dx		= x2-x1
		dy		= y2-y1

		return abs(dy*x0-dx*y0+x2*y1-y2*x1)/math.sqrt(dy**2+dx**2)


if __name__ == "__main__":
	test = Distance()


