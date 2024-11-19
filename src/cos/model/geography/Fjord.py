#!/usr/bin/python
# Filename: Fjord.py
# Description: Implementation of the fjord class

from cos.model.geography.Sea import Sea, Type
from cos.core.kernel.Context import Context

class Fjord(Sea):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Sea.__init__( self, ctxt, Type.FJORD, id, config )
		return



if __name__ == "__main__":
	test = Fjord()


