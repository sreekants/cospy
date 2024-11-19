#!/usr/bin/python
# Filename: PriorityResolver.py
# Description: Implementation of the PriorityResolver class

from cos.model.resolver.Resolver import Resolver, NamedResolver
from cos.model.rule.Context import Context
from cos.core.utilities.Patterns import Composite

import heapq

class PriorityResolver(Resolver):
	def __init__(self, resolvers):
		""" Constructor
		Arguments
			resolvers -- TODO
		""" 
		Resolver.__init__(self, None)

		# Heap sort the resolvers by increased priority
		pq	= []
		for r in resolvers:
			heapq.heappush(pq, (-r[0], r[1]))

		self.resolvers	= Composite()
		while len(pq):
			self.resolvers.container.append( heapq.heappop(pq)[1] )

		return

	def describe(self):
		""" TODO: describe
		""" 
		names	= []
		for r in self.resolvers.container:
			names.append( r.name )

		return ','.join(names)

	def resolve(self, ctxt:Context, variable:str):
		""" TODO: resolve
		Arguments
			ctxt -- Simulation context
			variable -- TODO
		""" 
		# Resolve the terms in the order of priority
		# (stored in sorted order in the container)
		for r in self.resolvers.container:
			result = r.resolve( ctxt, variable )
			if result is not None:
				return result

		return None

if __name__ == "__main__":
	test = PriorityResolver( [
		(1, NamedResolver('low')),
		(11, NamedResolver('critical')),
		(5, NamedResolver('medium')),
		(10, NamedResolver('high')),
		])

	print( test.describe() )
