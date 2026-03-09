#!/usr/bin/python
# Filename: Toroid.py
# Description: Implementation of the Toroid class

from cos.math.geometry.Rectangle import Rectangle
from cos.math.geometry.Vector import Vector

class Toroid:
	def __init__(self, zone:Rectangle):
		self.zone = zone
		return

	def bound(self, pos: Vector) -> Vector:
		"""Wrap position around zone (toroidal world)."""
		x = (pos.x-self.zone.x) % self.zone.width
		y = (pos.y-self.zone.y) % self.zone.height
		return Vector(self.zone.x + x, self.zone.y + y)


	def shortestBoundedPathTo(self, a: Vector, b: Vector) -> Vector:
		"""
		Shortest displacement vector from a -> b in a toroidal world.
		Arguments
			a -- start point
			b -- end point
		"""
		dx = b.x - a.x
		dy = b.y - a.y

		# Wrap dx into (-W/2, W/2]
		if dx > self.zone.width / 2:
			dx -= self.zone.width
		elif dx < -self.zone.width / 2:
			dx += self.zone.width

		# Wrap dy into (-H/2, H/2]
		if dy > self.zone.height / 2:
			dy -= self.zone.height
		elif dy < -self.zone.height / 2:
			dy += self.zone.height

		return Vector(dx, dy)


	def boundedDist(self, a: Vector, b: Vector) -> float:
		return self.shortestBoundedPathTo(a, b).norm()


		

if __name__ == "__main__":
	test = Toroid()

