#!/usr/bin/python
# Filename: VesselDeclarationsResolver.py
# Description: Resolves Vessel.* declarations and the vessel enums, e.g. Vessel.Type.PowerDriven

from maritime.model.resolver.DeclarationsResolver import DeclarationsResolver
from maritime.model.vessel.Vessel import Type, Status, Operation, Restriction
from cos.core.kernel.Context import Context

import re

ENUMS	= { 'Type': Type, 'Status': Status, 'Operation': Operation, 'Restriction': Restriction }


class VesselDeclarationsResolver(DeclarationsResolver):
	def __init__(self, resolver=None):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
			prefix -- Prefix for the resolver
		"""
		DeclarationsResolver.__init__(self, 'Vessel')
		return

	def resolve(self, ctxt:Context, variable:str):
		""" Resolves a declaration, else a vessel enum member
		Arguments
			ctxt -- Simulation context
			variable -- Term, e.g. Vessel.Status.ANCHORED
		"""
		result	= DeclarationsResolver.resolve( self, ctxt, variable )
		if result is not None:
			return result

		return VesselDeclarationsResolver.member( self.get_key(ctxt, variable) )

	@staticmethod
	def member(key:str):
		""" The enum member a key names, as 'Group.Name' with Name as the member or in CamelCase
		Arguments
			key -- e.g. 'Type.PowerDriven' or 'Status.NOT_UNDER_COMMAND'
		Returns
			The member, or None when the key names none
		"""
		if (key is None) or (key.count('.') != 1):
			return None

		group, name	= key.split('.')
		enum		= ENUMS.get( group )
		if enum is None:
			return None

		name		= name if name.isupper() else re.sub( r'(?<!^)(?=[A-Z])', '_', name ).upper()
		return enum.__members__.get( name )


if __name__ == "__main__":
	test = VesselDeclarationsResolver()
