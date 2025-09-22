#!/usr/bin/python
# Filename: Vector.py
# Description: Implementation of the vector calculus functions

from cos.math.geometry.Point import Point
import math


class Vector:
    def __init__(self, x, y):
        """ Constructor
        """
        self.x  = x
        self.y  = y
        return
    
    def to_point(self, p:Point, q:Point):
        """ Distance from a point to a vector
        Arguments
            p -- Point from which to measure distance
            q -- Point on the vector
        """ 

		# Refer: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
		# Topic: A vector projection proof

        x0		= p.x
        y0		= p.y
        x1		= q.x
        y1		= q.y
        a       = self.x
        b       = self.y
        c       = -(a*x1) - (b*y1)

        return abs(a*x0-b*y0+c)/math.sqrt(a**2+b**2)

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def norm(self) -> float:
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, s: float):
        return Vector(self.x * s, self.y * s)

    def __str__(self):
        return f'({self.x}, {self.y})'

if __name__ == "__main__":
    test = Vector(10, 20)
