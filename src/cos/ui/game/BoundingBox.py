#!/usr/bin/python
# Filename: BoundingBox.py
# Description: IImplementation of a rectangular bounding box for simulation objects

import pygame

BLACK =(0,0,0)

class BoundingBox:
	def __init__(self, rect, color=BLACK, width=0 ):
		""" Constructor
		Arguments
			rect -- Bounding box rectangel
			color -- Color of the rectangle
		"""
		self.color 	= color
		self.rect	= rect
		self.width	= width
		self.layer	= 0
		return

	def render(self, ctxt, screen):
		""" Renders the bounding box
		Arguments
			ctxt -- Simulation context
			screen -- Reference ot the simulation screen
		"""
		if ctxt.layer != self.layer:
			return

		pygame.draw.rect( screen, self.color, ctxt.encoder.tranform_rect(self.rect), self.width )
		return

	def update(self):
		""" Updates the screen
		"""
		return

if __name__ == "__main__":
	test = BoundingBox()


