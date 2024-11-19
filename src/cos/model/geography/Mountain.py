#!/usr/bin/python
# Filename: Mountain.py
# Description: Implementation of the mountain class

from cos.model.geography.Land import Land, Type
from cos.core.kernel.Context import Context

class Mountain(Land):
	def __init__( self, ctxt, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Land.__init__( self, ctxt, Type.MOUNTAIN, id, config )
		return



if __name__ == "__main__":
	test = Mountain()


