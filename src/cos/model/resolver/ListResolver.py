#!/usr/bin/python
# Filename: ListResolver.py
# Description: Implementation of the ListResolver class

from cos.model.resolver.Resolver import Resolver
import fnmatch

class ListResolver(Resolver):
	def __init__(self, pattern:str, values, prefix:str=None):
		""" Constructor
		Arguments
			pattern -- TODO
			values -- TODO
			prefix -- TODO
		""" 
		Resolver.__init__(self, prefix)
		self.pattern	= pattern
		self.values		= [v.lower() for v in values]
		return

	def applies(self, variable:str):
		""" TODO: applies
		Arguments
			variable -- TODO
		""" 
		return fnmatch.fnmatch(variable, self.pattern)

	def IN(self, value:str):
		""" TODO: IN
		Arguments
			value -- TODO
		""" 
		if value.islower() == False:
			value = value.lower()

		return (value in self.values)


if __name__ == "__main__":
	test = ListResolver()

