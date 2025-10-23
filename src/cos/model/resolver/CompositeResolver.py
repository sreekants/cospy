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

	def add(self, scope:str, resolver:Resolver)->Resolver:
		""" Adds a resolver to the context
		Arguments
			scope -- Scope of the resolver
			resolver -- Resolver instance
		""" 
		self.resolvers.add_component( [scope,resolver] )
		return resolver

	def get(self, scope:str)->Resolver:
		""" Returns a resolver for a scope
		Arguments
			scope -- Scope of the resolver
		""" 
		for info in self.resolvers.container:
			if info[0] == scope:
				return info[1]

		return None

	def resolve(self, ctxt:Context, token:str):
		""" Resolves a token
		Arguments
			ctxt -- Simulation context
			token -- Token to resolve
		""" 
		if token is None:
			return None

		# Check if the token is a number
		result = Resolver.to_number(token)
		if result is not None:
			return result

		rctxt			= CompositeResolverContext()
		rctxt.ctxt		= ctxt
		rctxt.variable	= token
		if self.resolvers.for_each_first(self.__resolve, rctxt) == False:
			raise ValueError( f'Unresolved variable [{token}].')
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
	def __resolve(resolver_info:Resolver, rctxt:CompositeResolverContext):
		""" Resolves a context
		Arguments
			resolver_info -- Resolver to apply context to
			rctxt -- Context to resolve
		""" 
		if resolver_info[0] == 'tss' and rctxt.variable.find('TrafficSeparationScheme') != -1:
			print('HERE')
		result = resolver_info[1].resolve( rctxt.ctxt, rctxt.variable )
		if result is None:
			return False

		rctxt.result	= result
		return True


if __name__ == "__main__":
	test = CompositeResolver()

