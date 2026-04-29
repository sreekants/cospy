#!/usr/bin/python
# Filename: Map.py
# Description: Fasade for Map related classes

from cos.math.geometry.Rectangle import Rectangle

class Map:
	def __init__(self, ctxt):
		""" Constructor
		"""
		return

	def in_tss(self, pt):
		return False

	def get_tss_bearing(self, _pt):
		"""Returns the required heading (degrees) for the TSS lane at pt, or None if unknown."""
		return None

	def get_bodies(self, type, bound:Rectangle):
		result		= list()
		return result


if __name__ == "__main__":
	test = Map()


