#!/usr/bin/python
# Filename: MaritimeExclusionZone.py
# Description: Implementation of the maritime exclusion class

from cos.model.geography.Sea import Sea, Type
from cos.model.geography.MaritimeZone import MaritimeZone
from cos.core.kernel.Context import Context

class MaritimeExclusionZone(MaritimeZone):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		MaritimeZone.__init__( self, ctxt, Type.MARITIME_EXCLUSION_ZONE, id, config )
		return



if __name__ == "__main__":
	test = MaritimeExclusionZone()


