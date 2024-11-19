#!/usr/bin/python
# Filename: TrafficSeparationScheme.py
# Description: Implementation of the marine_valley class

from cos.model.geography.Sea import Sea, Type
from cos.model.geography.MaritimeZone import MaritimeZone
from cos.core.kernel.Context import Context


class AreaToAvoid(MaritimeZone):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		MaritimeZone.__init__( self, ctxt, Type.AREA_TO_AVOID, id, config )
		return



if __name__ == "__main__":
	test = AreaToAvoid()


