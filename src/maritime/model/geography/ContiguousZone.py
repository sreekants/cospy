#!/usr/bin/python
# Filename: ContiguousZone.py
# Description: Implementation of the marine_valley class

from cos.model.geography.Sea import Sea, Type
from cos.model.geography.MaritimeZone import MaritimeZone
from cos.core.kernel.Context import Context

class ContiguousZone(MaritimeZone):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		MaritimeZone.__init__( self, ctxt, Type.CONTIGUOUS_ZONE, id, config )
		return



if __name__ == "__main__":
	test = ContiguousZone()


