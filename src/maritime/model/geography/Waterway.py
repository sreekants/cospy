#!/usr/bin/python
# Filename: Waterway.py
# Description: Implementation of the waterway class

from cos.model.geography.Sea import Sea, Type
from cos.model.geography.TrafficZone import TrafficZone
from cos.core.kernel.Context import Context

class Waterway(TrafficZone):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		TrafficZone.__init__( self, ctxt, Type.WATERWAY, id, config )
		return


		

if __name__ == "__main__":
	test = Waterway()

