#!/usr/bin/python
# Filename: Harbour.py
# Description: Implementation of the marine_valley class

from cos.model.geography.Sea import Sea, Type
from cos.model.geography.TrafficZone import TrafficZone
from cos.core.kernel.Context import Context

class Harbour(TrafficZone):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		TrafficZone.__init__( self, ctxt, Type.HARBOUR, id, config )
		return



if __name__ == "__main__":
	test = Harbour()


