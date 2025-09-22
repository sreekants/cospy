#!/usr/bin/python
# Filename: Position.py
# Description: Implementation of the Position class

from cos.math.geometry.Vector import Vector

import math

class Position:
	def __init__(self, x, y):
		""" Constructor
		"""
		self.x  = x
		self.y  = y
		return
	
	def at(self, v, t: float):
		"""Linear motion: p(t) = p0 + v * t"""
		return Vector(self.x, self.y) + v*t

	def dot(self, other) -> float:
		return self.x*other.x + self.y*other.y

	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)

	def __mul__(self, s: float):
		return Position(self.x * s, self.y * s)

	def __str__(self):
		return f'({self.x}, {self.y})'

		

if __name__ == "__main__":
	test = Position()

