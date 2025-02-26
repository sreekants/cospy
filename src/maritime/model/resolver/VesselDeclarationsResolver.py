#!/usr/bin/python
# Filename: VesselDeclarationsResolver.py
# Description: Implementation of the ZoneResolver class

from maritime.model.resolver.DeclarationsResolver import DeclarationsResolver


class VesselDeclarationsResolver(DeclarationsResolver):
	def __init__(self, resolver=None):
		""" Constructor
		Arguments
			resolver -- Parent composite resolver
			prefix -- Prefix for the resolver
		""" 
		DeclarationsResolver.__init__(self, 'Vessel')
		return


if __name__ == "__main__":
	test = VesselDeclarationsResolver()

