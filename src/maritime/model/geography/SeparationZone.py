#!/usr/bin/python
# Filename: MaritimeTrafficZones.py
# Description: Implementation of the maritme traffic zone classes

from cos.model.geography.Sea import Sea, Type
from cos.model.geography.MaritimeZone import MaritimeTrafficZone
from cos.core.kernel.Context import Context


class SeparationZone(MaritimeTrafficZone):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		MaritimeTrafficZone.__init__( self, ctxt, Type.SEPARATION_ZONE, id, config )
		return



if __name__ == "__main__":
	test = SeparationZone()

