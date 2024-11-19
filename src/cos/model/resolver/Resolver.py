#!/usr/bin/python
# Filename: Resolver.py
# Description: Implementation of the base class for all resolvers

from cos.model.rule.Definition import Definition
from cos.model.rule.Context import Context

import os, inspect

class Resolver:
	def __init__(self, prefix:str=None):
		""" Constructor
		Arguments
			prefix -- TODO
		""" 
		self.prefix		= prefix
		self.resolvers	= Resolver.generate_dispatch(self.__class__, '__simattribute')
		return

	def reset(self, ctxt:Context, rulectxt):
		""" TODO: reset
		Arguments
			ctxt -- Simulation context
			rulectxt -- TODO
		""" 
		return

	def resolve(self, ctxt:Context, variable:str):
		""" TODO: resolve
		Arguments
			ctxt -- Simulation context
			variable -- TODO
		""" 
		if (self.resolvers is None) or (len(self.resolvers) == 0):
			return

		ndx		= variable.rfind('.')
		if ndx <= 0:
			return None

		fnname	= variable[ndx+1:]
		method	= self.resolvers.get(fnname, None)
		if method is None:
			return None

		return method(self)

	def applies(self, variable:str)->bool:
		""" TODO: applies
		Arguments
			variable -- TODO
		""" 
		if self.prefix is None:
			return None

		if variable.startswith(self.prefix):
			return self

		return None

	@staticmethod
	def to_number(variable:str):
		""" TODO: to_number
		Arguments
			variable -- TODO
		""" 
		if variable.isdecimal():
			return int(variable)
		if variable.replace('.', '', 1).isdigit() :
			return float(variable)
		return None

	@staticmethod
	def generate_dispatch(cls, decoratorName):
		""" TODO: generate_dispatch
		Arguments
			cls -- TODO
			decoratorName -- TODO
		""" 
		resolvers	= {}

		for m in dir(cls):
			attrib	= getattr(cls, m)
			if hasattr(attrib, decoratorName):
				resolvers[attrib.__name__]	= attrib

		return resolvers

class NamedResolver(Resolver):
	def __init__(self, name):
		""" Constructor
		Arguments
			name -- Name of the object
		""" 
		Resolver.__init__(self, None)
		self.name	= name
		return


def simproperty(funcobj):
	""" TODO: simproperty
	Arguments
		funcobj -- TODO
	""" 
	funcobj.__simattribute	= True
	return funcobj

if __name__ == "__main__":
	test = Resolver()

