#!/usr/bin/python
# Filename: BeaconSprite.py
# Description: Implementation of a Beacon sprite

from cos.ui.game.Sprite import Sprite
from cos.ui.game.Config import *

class BeaconSprite(Sprite):
	def __init__(self):
		""" Constructor
		"""
		super(BeaconSprite, self).__init__(
			"img/beacon.png",
			(0, 0, 0) )

		self.rect = self.get_rect()
		return

	# Move the cloud based on a constant speed
	# Remove it when it passes the left edge of the screen
	def update(self):
		""" Update the sprite in the next time loop
		"""
		self.rect.move_ip(-5, 0)    # TODO: Move the sprite appropriately
		if self.rect.right < 0:
			self.kill()



if __name__ == "__main__":
	test = BeaconSprite()


