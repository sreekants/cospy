#!/usr/bin/python
# Filename: Mouse.py
# Description: Implementation of the Mouse class

import pygame

from pygame.locals import (
    MOUSEBUTTONDOWN,
)

class Mouse:
	def __init__(self, world):
		self.world		= world
		self.vessel		= None
		return

	def handle_event(self, event:pygame.event.Event):
		# Left click selects the vessel under the cursor, or clears the selection
		if event.type != MOUSEBUTTONDOWN or event.button != 1:
			return False, False

		self.world.pick( event.pos )
		return True, True


if __name__ == "__main__":
	test = Mouse()
