#!/usr/bin/python
# Filename: SeaSprite.py
# Description: Sea shapes

from cos.ui.game.PolygonSprite import PolygonSprite

class SeaSprite(PolygonSprite):
	def __init__(self, config):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		PolygonSprite.__init__(self, config)
		return


if __name__ == "__main__":
	test = SeaSprite()


