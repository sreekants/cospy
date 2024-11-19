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
		topleft		= Encoder.dot2D(self.transform, self.move, (rect[0],rect[1],1.) )
		bottomright	= Encoder.dot2D(self.transform, self.move, (rect[2],rect[3],1.) )
		return pygame.Rect( topleft[0], topleft[1], bottomright[0], bottomright[1] )

	def transform_polygon(self, polygon):
		result	= polygon
		points	= []
		for pt in polygon:
			pt = Encoder.dot2D(self.transform, self.move, (float(pt[0]),float(pt[1]),1.) )
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

