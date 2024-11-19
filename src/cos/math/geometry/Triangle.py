#!/usr/bin/python
# Filename: Triangle.py
# Description: Implementation of the Triangle class

import shapely

class Triangle(shapely.Polygon):
	def __init__(self, A, B, C):
		""" Constructor
		Arguments
			A -- First edge of triangle
			B -- Second edge of triangle
			C -- Third edge of triangle
		"""
		shapely.Polygon.__init__(self, [A,B,C])
		return

	@property
	def circumcenter(self):
		""" Returns the circumcenter of the triangle
		"""
		Ax = self.coords[0][0]
		Ay = self.coords[0][1]
		Bx = self.coords[1][0]
		By = self.coords[1][1]
		Cx = self.coords[2][0]
		Cy = self.coords[3][1]
		D = 2 * (Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By))
		Ux = ((Ax * Ax + Ay * Ay) * (By - Cy) + (Bx * Bx + By * By) * (Cy - Ay) + (Cx * Cx + Cy * Cy) * (Ay - By)) / D
		Uy = ((Ax * Ax + Ay * Ay) * (Cx - Bx) + (Bx * Bx + By * By) * (Ax - Cx) + (Cx * Cx + Cy * Cy) * (Bx - Ax)) / D
		return (Ux, Uy)

	@property
	def centeroid(self):
		""" Returns the centeroid of the triangle
		"""
		Ax = self.coords[0][0]
		Ay = self.coords[0][1]
		Bx = self.coords[1][0]
		By = self.coords[1][1]
		Cx = self.coords[2][0]
		Cy = self.coords[3][1]
		Ux = (Ax+Bx+Cx) / 3.0
		Uy = (Ay+By+Cy) / 3.0
		return (Ux, Uy)

	def encloses(self, x, y):
		""" Checks if a point is enclosed by the triangle
		Arguments
			x -- X coordinate
			y -- Y coordinate
		"""
		return self.contains( shapely.Point(x, y) )

if __name__ == "__main__":
	test = Triangle()


