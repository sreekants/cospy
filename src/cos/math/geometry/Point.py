#!/usr/bin/python
# Filename: Point.py
# Description: Implementation of the Point class

class Point:
	def __init__(self, x, y):
		""" Constructor
		"""
		self.x  = x
		self.y  = y
		return

	def distance(self, other)->float:
		return self.x*other.x + self.y*other.y

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)

	def __str__(self):
		return f'({self.x}, {self.y})'

		

if __name__ == "__main__":
	test = Point()

