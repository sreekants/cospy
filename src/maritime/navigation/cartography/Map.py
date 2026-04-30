#!/usr/bin/python
# Filename: Map.py
# Description: Fasade for Map related classes

from cos.math.geometry.Rectangle import Rectangle

class Map:
	def __init__(self, ctxt):
		""" Constructor
		"""
		self.zones_cache	= {}
		return

	def reset(self):
		self.zones_cache	= {}
		return
	
	def in_tss(self, pt):
		return False

	def get_tss_bearing(self, _pt):
		"""Returns the required heading (degrees) for the TSS lane at pt, or None if unknown."""
		return None

	def get_bodies(self, type, bound:Rectangle):
		result		= list()
		return result

	def get_zones(self, type, bound:Rectangle):
		# Search the cache for the file
		if type in self.zones_cache:
			return self.zones_cache[type]
		
		result		= list()
		return result

if __name__ == "__main__":
	test = Map()


