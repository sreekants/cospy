#!/usr/bin/python
# Filename: Encoder.py
# Description: Implementation of the Encoder class

import numpy as np
from math import sin,cos
import pygame

class Encoder:
	def __init__(self):
		self.transform	= np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
		self.move		= np.array([0.0,0.0,0.0])
		return

	def transform_rect(self, rect):
		""" Transforms a [left, top, width, height] rectangle to screen coordinates
		"""
		topleft		= self.transform_point( (rect[0], rect[1]) )

		# Width and height are extents, not a corner: scale them, never translate them
		size		= ( rect[2]*self.transform[0][0], rect[3]*self.transform[1][1] )
		return pygame.Rect( topleft[0], topleft[1], size[0], size[1] )

	def transform_point(self, pt):
		""" Transforms a map point to screen coordinates
		"""
		return Encoder.dot2D(self.transform, self.move, (float(pt[0]),float(pt[1]),1.) )

	def inverse_point(self, pt):
		""" Transforms a screen point (e.g. the mouse) back to map coordinates
		"""
		return ( (pt[0]-self.move[0])/self.transform[0][0], (pt[1]-self.move[1])/self.transform[1][1] )

	def fit(self, extent, screen):
		""" Scales and centres a map of the given extent on the screen
		Arguments
			extent -- Map size in map units (width, height)
			screen -- Screen size in pixels (width, height)
		"""
		scale			= min( screen[0]/extent[0], screen[1]/extent[1] )
		self.transform	= np.array([[scale,0.0,0.0],[0.0,scale,0.0],[0.0,0.0,1.0]])
		self.move		= np.array([ (screen[0]-extent[0]*scale)/2.0, (screen[1]-extent[1]*scale)/2.0, 0.0 ])
		return

	def transform_polygon(self, polygon):
		points	= []
		for pt in polygon:
			pt = self.transform_point( pt )
			points.append( (int(pt[0]), int(pt[1])) )

		return points

	def zoom(self, scale):
		self.transform	= self.transform * scale
		return

	def translate(self, x, y):
		self.move[0]	= self.move[0] + x
		self.move[1]	= self.move[1] + y
		return

	@staticmethod
	def rotateX(angle):
		cs	= cos(angle*np.pi/180.)
		sn	= sin(angle*np.pi/180.)
		return np.array([[1.0,0.0,0.0],[0.0,cs,-sn],[0.0,sn,cs]])
	
	@staticmethod
	def rotateY(angle):
		cs	= cos(angle*np.pi/180.)
		sn	= sin(angle*np.pi/180.)
		return np.array([[cs,0.0,sn],[0.0,1.0,0.0],[-sn,0.0,cs]])
	
	@staticmethod
	def rotateZ(angle):
		cs	= cos(angle*np.pi/180.)
		sn	= sin(angle*np.pi/180.)
		return np.array([[cs,-sn,0.0],[sn,cs,0.0],[0.0,0.0,1.0]])
	
	@staticmethod
	def dot(m,a):
		c1	= np.sum(m[0,:] * a)
		c2	= np.sum(m[1,:] * a)
		c3	= np.sum(m[2,:] * a)
		return np.array([c1,c2,c3])

	@staticmethod
	def dot2D(m,d,a):
		c1	= np.sum(m[0,:] * a)
		c2	= np.sum(m[1,:] * a)
		return np.array([c1+d[0],c2+d[1]])


if __name__ == "__main__":
	test = Encoder()

