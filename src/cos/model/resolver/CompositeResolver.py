#!/usr/bin/python
# Filename: CompositeResolver.py
# Description: Implementation of the CompositeResolver class

from cos.model.resolver.Resolver import Resolver
from cos.model.rule.Context import Context
from cos.core.utilities.Patterns import Composite

class CompositeResolverContext:
	def __init__(self):
		""" Constructor
		""" 
		self.ctxt		= None
		self.variable	= None
		self.result		= None
		return

class CompositeResolver(Resolver):
	def __init__(self):
		""" Constructor
		""" 
		Resolver.__init__(self, None)
		self.resolvers	= Composite()
		return

	def add(self, resolver:Resolver)->Resolver:
		""" TODO: add
		Arguments
			resolver -- TODO
		""" 
		self.resolvers.add_component( resolver )
		return resolver

	def resolve(self, ctxt:Context, variable:str):
		""" TODO: resolve
		Arguments
			ctxt -- Simulation context
			variable -- TODO
		""" 
		if variable is None:
			return None

		result = Resolver.to_number(variable)
		if result is not None:
			return result

		rctxt			= CompositeResolverContext()
		rctxt.ctxt		= ctxt
		rctxt.variable	= variable
		self.resolvers.for_each_first( self.__resolve, rctxt )
		return rctxt.result

	def applies(self, variable:str)->bool:
		""" TODO: applies
		Arguments
			variable -- TODO
		""" 
		for r in self.resolvers.container:
			if r.applies(variable):
				return r

		return None

	@staticmethod
	def __resolve(resolver:Resolver, rctxt:CompositeResolverContext):
		""" TODO: __resolve
		Arguments
			resolver -- TODO
			rctxt -- TODO
		""" 
		result = resolver.resolve( rctxt.ctxt, rctxt.variable )
		if result is None:
			return False

		rctxt.result	= result
		return True


if __name__ == "__main__":
	test = CompositeResolver()

