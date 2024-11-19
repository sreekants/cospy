#!/usr/bin/python
# Filename: LandSprite.py
# Description: Land shapes

from cos.ui.game.PolygonSprite import PolygonSprite

class LandSprite(PolygonSprite):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		PolygonSprite.__init__(self, config)
		return

if __name__ == "__main__":
	test = LandSprite()


