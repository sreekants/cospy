#!/usr/bin/python
# Filename: Boid.py
# Description: Implementation of the Boid class

from cos.math.geometry.Vector import Vector
import random, math

class Boid:
	def __init__(self):
		return

	@staticmethod
	def turn(currentVel: Vector, desiredDir: Vector, maxTurnAngle: float) -> Vector:
		"""
		Turn-limited steering: rotate current velocity toward desired direction by at most maxTurnAngle.
		Similar to util.js turn().
		"""
		cur = currentVel.normalize()
		des = desiredDir.normalize()
		if des.mag2() == 0:
			return cur  # no change

		a_cur = cur.heading()
		a_des = des.heading()
		delta = Boid._wrap_angle(a_des - a_cur)

		if abs(delta) <= maxTurnAngle:
			return Vector.from_angle(a_des)
		return Vector.from_angle(a_cur + maxTurnAngle * (1 if delta > 0 else -1))
		
	@staticmethod
	def _wrap_angle(angle: float) -> float:
		"""Wrap angle to (-pi, pi]."""
		while angle <= -math.pi:
			angle += 2 * math.pi
		while angle > math.pi:
			angle -= 2 * math.pi
		return angle



if __name__ == "__main__":
	test = Boid()

