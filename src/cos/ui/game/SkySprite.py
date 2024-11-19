#!/usr/bin/python
# Filename: SkySprite.py
# Description: Sky shapes

from cos.ui.game.PolygonSprite import PolygonSprite
import pygame

class SkySprite(PolygonSprite):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		PolygonSprite.__init__(self, config)
		self.layer	= 4
		return


if __name__ == "__main__":
	test = SkySprite()


