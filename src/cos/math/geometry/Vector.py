#!/usr/bin/python
# Filename: Vector.py
# Description: Implementation of the vector calculus functions

import math

class Vector:
    def __init__(self, x, y):
        """ Constructor
        """
        self.x  = x
        self.y  = y
        return
        
    def dot(self, other) -> float:
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
