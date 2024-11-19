#!/usr/bin/python
# Filename: MaritimeZone.py
# Description: Implementation of the base class for maritime zones class

from cos.model.geography.Sea import Sea, Type
from cos.model.geography.TrafficZone import TrafficZone
from cos.core.kernel.Context import Context

class MaritimeZone(Sea):
	def __init__( self, ctxt:Context, type, id, config ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
        	type -- Type of the object
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Sea.__init__( self, ctxt, type, id, config )
		return


class MaritimeTrafficZone(TrafficZone):
	def __init__( self, ctxt:Context, type, id, config ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
        	type -- Type of the object
			id -- Unique identifier
			config -- Configuration attributes
		"""
		TrafficZone.__init__( self, ctxt, type, id, config )
		return


if __name__ == "__main__":
	test = MaritimeZone()


