#!/usr/bin/python
# Filename: Plateau.py
# Description: Implementation of the plateau class

from cos.model.geography.Land import Land, Type
from cos.core.kernel.Context import Context

class Plateau:
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Land.__init__( self, ctxt, Type.PLATEAU, id, config )
		return



if __name__ == "__main__":
	test = Plateau()


