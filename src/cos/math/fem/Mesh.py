#!/usr/bin/python
# Filename: Mesh.py
# Description: Mesh surface constructed from points

from cos.math.partition.Delaunator import Delaunator

class Mesh:
	def __init__(self, points):
		self.mesh = []

		if points is None:
			return

		# Triangulate it.
		triangles = Delaunator(points).triangles

		# Convert the points into coordinates
		for i in range(0, len(triangles), 3):
			self.mesh.append([
				points[triangles[i]],
				points[triangles[i + 1]],
				points[triangles[i + 2]]])
			
		return

		

if __name__ == "__main__":
	test = Mesh()

