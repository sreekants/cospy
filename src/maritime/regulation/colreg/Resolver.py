#!/usr/bin/python
# Filename: Resolver.py
# Description: Implementation of the COLREG master resolver class

from cos.model.resolver.CompositeResolver import CompositeResolver
from cos.model.resolver.MappingResolver import MappingResolver

from maritime.model.resolver.ColregResolver import ColregResolver
from maritime.model.resolver.EEZResolver import EEZResolver
from maritime.model.resolver.HarbourResolver import HarbourResolver
from maritime.model.resolver.MEZResolver import MEZResolver
from maritime.model.resolver.TargetResolver import TargetResolver
from maritime.model.resolver.TSSResolver import TSSResolver, LaneResolver
from maritime.model.resolver.VesselResolver import *
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext

class Resolver(CompositeResolver):
	def __init__(self):
		""" Constructor
		""" 
		CompositeResolver.__init__(self)
		self.variables = self.add(MappingResolver())
		self.constants = self.add(MappingResolver())

		# Add the COLREG resolvers
		self.eez		= self.add(EEZResolver())
		self.harbour	= self.add(HarbourResolver())
		self.lane		= self.add(LaneResolver())
		self.mez		= self.add(MEZResolver())
		self.target		= self.add(TargetResolver())
		self.tss		= self.add(TSSResolver())
		self.os			= self.add(OwnShipResolver())
		self.ts			= self.add(TargetShipResolver())

		self.regulation	= self.add(ColregResolver(self.target))
		return


	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" TODO: reset
		Arguments
			ctxt -- Simulation context
			rulectxt -- TODO
		""" 
		[r.reset(ctxt, rulectxt) for r in self.resolvers.container]
		return

if __name__ == "__main__":
	test = Resolver()

