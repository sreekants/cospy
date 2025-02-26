#!/usr/bin/python
# Filename: DeclarationsResolver.py
# Description: Implementation of the ZoneResolver class

from cos.model.resolver.Resolver import Resolver
from cos.model.resolver.NumericRange import NumericRange
from cos.model.rule.Context import Context
from cos.model.resolver.Resolver import Resolver, simproperty
from cos.core.kernel.Context import Context
from cos.model.rule.Context import Context as RuleContext
from cos.core.utilities.ActiveRecord import ActiveRecord
from cos.core.utilities.ArgList import ArgList
from maritime.model.vessel.Vessel import Vessel, Status
from maritime.model.geography.TrafficSeparationScheme import TrafficSeparationScheme

import numpy as np


class DeclarationsResolver(Resolver):
	def __init__(self, resolver=None):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
			prefix -- Prefix for the resolver
		""" 
		Resolver.__init__(self, 'Vessel')
		self.decls		= dict()
		self.methods    = dict()
		return

	def init(self, ctxt, cfg):
		""" Initializes the configuration for the resolver
		Arguments
			ctxt -- Simulation context
			cfg -- Configuration for the resolver
		""" 
		args	= ArgList(cfg["config"])
		prefix	= args['filter']
		path	= ctxt.sim.config.resolve( cfg["database"] )
		db		= ActiveRecord.create('constant', path)

		# Add the matching declaration records with the prefix
		records	= db.get_all(f'name LIKE \'{prefix}%\'')

		for rec in records:
			self.__add_value( prefix, rec )
			
		return

	def __add_value(self, prefix, rec):
		name	= rec[1][len(prefix)+1:]
		type	= rec[2]
		value	= rec[3]
		

		if type == 'String':
			self.decls[name]	= str(value)
			return
		elif type == 'Float':
			self.decls[name]	= float(value)
			return
		elif type == 'Integer':
			self.decls[name]	= int(value)
			return
		elif type == 'StringList':
			self.decls[name]	= str(value).split(',')
			return
		elif type == 'NumericRange':
			self.decls[name]	= NumericRange(eval(value))
			return

		raise ValueError(f'Unknown declaration type[type].')
		return
	
	def resolve(self, ctxt:Context, variable:str):
		""" Reset th resolver
		Arguments
			ctxt -- Simulation context
			rulectxt -- Rule context
		""" 
		variable	= self.get_key(ctxt, variable)
		if variable == None:
			return None
		
		result 		= self.decls.get( variable, None )
		if result is not None:
			return result
		
		return self.__resolve_method(ctxt, variable)
		

	def __resolve_method(self, ctxt:Context, variable:str):
			""" Reset th resolver
			Arguments
					ctxt -- Simulation context
					rulectxt -- Rule context
			""" 
			if not self.methods:
				return None

			fn              = self.methods.get( variable, None )
			if fn == None:
					return None

			return fn(ctxt)


if __name__ == "__main__":
	test = DeclarationsResolver()

