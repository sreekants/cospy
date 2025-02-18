#!/usr/bin/python
# Filename: RangeResolver.py
# Description: Implementation of the RangeResolver class

from cos.model.resolver.Resolver import Resolver
import fnmatch

class RangeResolver(Resolver):
	def __init__(self, pattern:str, value:range, prefix:str=None):
		""" Constructor
		Arguments
			pattern -- TODO
			value -- TODO
			prefix -- TODO
		""" 
		Resolver.__init__(self, prefix)
		self.pattern	= pattern
		self.bound		= value
		return

	def applies(self, variable:str):
		""" TODO: applies
		Arguments
			variable -- TODO
		""" 
		return fnmatch.fnmatch(variable, self.pattern)

	def IN(self, value):
		""" TODO: IN
		Arguments
			value -- TODO
		""" 
		return (value in self.bound)


	def HAS(self, value):
		""" HAS
		Arguments
			value -- TODO
		""" 
		return (value in self.bound)


if __name__ == "__main__":
	test = RangeResolver()

