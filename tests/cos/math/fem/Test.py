
import matplotlib.pyplot as plt
import numpy as np
from cos.math.partition.Delaunator import Delaunator
import time

def triangle(t):
    a = t[0]
    b = t[1]
    c = t[2]
    plt.fill((a[0], b[0], c[0], a[0]), (a[1], b[1], c[1], a[1]) )

def draw_points(points):
    xpoints = np.array([p[0] for p in points])
    ypoints = np.array([p[1] for p in points])

    plt.scatter(xpoints, ypoints)

def triangulate(points):
    # Triangulate the points.
    triangles = Delaunator(points).triangles

    # Convert the points into coordinates
    mesh = []

    for i in range(0, len(triangles), 3):
        mesh.append([
            points[triangles[i]],
            points[triangles[i + 1]],
            points[triangles[i + 2]]])
        
    return mesh

# Create a random set of points    
points  = np.random.randint(1,200,size=(20,2))

mesh    = triangulate(points)
    
for t in mesh:
    triangle( t )

draw_points(points)

plt.show()

