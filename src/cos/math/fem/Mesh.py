#!/usr/bin/python
# Filename: Mesh.py
# Description: Mesh surface constructed from points

from cos.math.partition.Delaunator import Delaunator
from cos.math.geometry.Triangle import Triangle
import numpy as np

class Mesh:
	def __init__(self, points):
		self.mesh = []

		if points is None:
			return

		# Triangulate it.
		triangles = Delaunator(points).triangles

		# Convert the points into coordinates
		for i in range(0, len(triangles), 3):
			self.mesh.append( Triangle(
				points[triangles[i]],
				points[triangles[i + 1]],
				points[triangles[i + 2]])
				)
			
		return

	def gradient(self, pt, fn):
		for triangle in self.mesh:
			if triangle.encloses(pt[0], pt[0]):
				Σ	= np.array()
				for c in triangle.coords():
					np.append(Σ,  fn(c,pt))


				return Σ/(2.0*triangle.area())

				return	

			
		return None
		

if __name__ == "__main__":
	test = Mesh()

