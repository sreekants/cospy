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
		Note
			A resolver's dispatch table is keyed purely by the trailing property
			name (see Resolver.get_property), not by its declared prefix, so two
			resolvers over different entities can expose a same-named property -
			FleetResolver and TargetResolver both have 'Distance' - and be
			ambiguous unless something narrows the search first:
			'(OwnShip,Fleet).Distance' would otherwise resolve through whichever
			of the two happens to be registered first, regardless of which one
			the term actually names.

			A resolver whose prefix AND dispatch table both match the token
			(applies() and has_property()) is unambiguously its rightful owner,
			so its result is final even when that result is None - a real
			'currently unobserved' rather than 'wrong resolver'. Falling through
			to the unfiltered scan in that case would risk handing the term to
			an unrelated resolver that merely happens to define the same
			property name.

			A resolver whose prefix matches but whose dispatch table does not
			(e.g. TargetResolver against '(OwnShip,TargetShip).EncounterSituation',
			which is ColregResolver's property) is not treated as an owner, so
			the term still falls through to the unfiltered scan below. That scan
			is also what resolves a resolver with no prefix (prefix=None, e.g.
			MappingResolver) or a stale one (ColregResolver's own prefix does not
			actually match the term above), exactly as before this method
			started preferring prefix matches at all.
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

		for info in self.resolvers.container:
			resolver	= info[1]
			if resolver.applies(token) and resolver.has_property(token):
				rctxt.result	= resolver.resolve(ctxt, token)
				return rctxt.result

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
		result = resolver_info[1].resolve( rctxt.ctxt, rctxt.variable )
		if result is None:
			return False

		rctxt.result	= result
		return True


if __name__ == "__main__":
	test = CompositeResolver()

