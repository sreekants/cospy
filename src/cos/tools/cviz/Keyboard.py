#!/usr/bin/python
# Filename: Keyboard.py
# Description: Implementation of the Keyboard class

import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_EQUALS,
    K_PLUS,
    K_MINUS,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Keyboard:
	def __init__(self, world):
		self.world		= world
		self.vessel		= None
		return

	def handle_event(self, event:pygame.event.Event):
		# Did the user hit a key?
		if event.type != KEYDOWN:
			return False, False
		
		# Was it the Escape key? If so, stop the loop
		if event.key == K_ESCAPE:
			return True, False
		
		if (event.key == K_PLUS) or (event.key == K_EQUALS):
			self.world.zoom(+1)

		if event.key == K_MINUS:
			self.world.zoom(-1)

		if event.key == K_UP:
			self.world.pan_up()

		if event.key == K_DOWN:
			self.world.pan_down()

		if event.key == K_LEFT:
			self.world.pan_left()

		if event.key == K_RIGHT:
			self.world.pan_right()

		return True, True

		

if __name__ == "__main__":
	test = Keyboard()

