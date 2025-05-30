#!/usr/bin/python
# Filename: Resolver.py
# Description: Implementation of the COLREG master resolver class

from cos.model.resolver.CompositeResolver import CompositeResolver
from cos.model.resolver.MappingResolver import MappingResolver

from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext
from cos.core.kernel.BootLoader import BootLoader

import yaml

class Resolver(CompositeResolver):
	def __init__(self):
		""" Constructor
		""" 
		CompositeResolver.__init__(self)
		return

	def init(self, ctxt:Context, configfile):
		""" Loads the resolvers
		Arguments
			ctxt -- Simulation context
			configfile -- Configuration file
		""" 

		if configfile is not None:
			sim			= ctxt.sim
			file		= sim.config.resolve(configfile)
			config		= yaml.safe_load( sim.fs.read_file_as_bytes(file) )
			resolvers	= config['language']['resolvers']

			for r in resolvers:
				# Instantiate the resolver class
				klassname, klass	= BootLoader.load_class( r['module'] )
				
				# Assign it to the scope
				resolver			= klass( self )
				prefix				= r['prefix']
				if prefix is not None:
					resolver.prefix	= prefix

				self.add( r['scope'], resolver)
				
				resolver.init( ctxt, r )

		return

	def reset(self, ctxt:Context, rulectxt:RuleContext):
		""" TODO: reset
		Arguments
			ctxt -- Simulation context
			rulectxt -- TODO
		""" 
		[r[1].reset(ctxt, rulectxt) for r in self.resolvers.container]
		return

if __name__ == "__main__":
	test = Resolver()

