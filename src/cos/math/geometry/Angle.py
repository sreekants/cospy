#!/usr/bin/python
# Filename: Distance.py
# Description: Implementation of the angle functions

import math

class Angle:
	def __init__(self):
		""" Constructor
		"""
		return

	def norm(x1, x2):
		""" REturns the normalized vector between two points
		Arguments
			x1 -- Start point
			x2 -- End point
		"""
		dx		= x2[0]-x1[0]
		dy		= x2[1]-x1[1]
		length	= math.sqrt((dx)**2 + (dy)**2)
		if length == 0.0:
			return 0.0

		return (dx/length, dy/length)

if __name__ == "__main__":
	test = Distance()


