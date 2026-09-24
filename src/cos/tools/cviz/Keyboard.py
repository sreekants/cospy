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
	K_d, 
	K_z,
    KEYDOWN,
	KMOD_CTRL,
	KMOD_ALT,
    QUIT,
)

ZOOM_STEP	= 1.03		# Zoom factor per frame while +/- is held (about 2.4x per second at 30 fps)

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

		# Panning and zooming are polled in poll() while the key is held down

		if event.key == K_d and (event.mod & KMOD_CTRL):
			self.world.toggle_debug()

		if event.key == K_z and (event.mod & KMOD_CTRL):
			self.world.toggle_zones()

		return True, True

	def poll(self, pressed):
		""" Pans and zooms for as long as a key is held down, once per frame
		Arguments
			pressed -- Key state from pygame.key.get_pressed()
		"""
		if pressed[K_PLUS] or pressed[K_EQUALS]:
			self.world.zoom(+1, ZOOM_STEP)

		if pressed[K_MINUS]:
			self.world.zoom(-1, ZOOM_STEP)

		if pressed[K_UP]:
			self.world.pan_down()

		if pressed[K_DOWN]:
			self.world.pan_up()

		if pressed[K_LEFT]:
			self.world.pan_right()

		if pressed[K_RIGHT]:
			self.world.pan_left()
		return

		

if __name__ == "__main__":
	test = Keyboard()

