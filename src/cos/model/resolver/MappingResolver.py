#!/usr/bin/python
# Filename: MappingResolver.py
# Description: Implementation of the MappingResolver class

from cos.model.resolver.Resolver import Resolver
from cos.model.rule.Context import Context


class MappingResolver(Resolver):
	def __init__(self, resolver=None, prefix:str=None):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
			prefix -- Prefix for the resolver
		""" 
		Resolver.__init__(self, prefix)
		self.values	= {}
		return

	def resolve(self, ctxt:Context, variable:str):
		""" Reset th resolver
		Arguments
			ctxt -- Simulation context
			rulectxt -- Rule context
		""" 
		return self.values.get(variable, None)

	def __setitem__(self, key, value):
		""" TODO: __setitem__
		Arguments
			key -- Key identifier
			value -- TODO
		""" 
		self.values[key] = value
		return

	def __getitem__(self, key):
		""" TODO: __getitem__
		Arguments
			key -- Key identifier
		""" 
		return self.values[key]

	def __len__(self):
		""" TODO: __len__
		""" 
		return len(self.values)

	def items(self):
		""" TODO: items
		""" 
		return self.values.items()

	def keys(self):
		""" TODO: keys
		""" 
		return self.values.keys()

	def values(self):
		""" TODO: values
		""" 
		return self.values.values()



if __name__ == "__main__":
	test = MappingResolver()

