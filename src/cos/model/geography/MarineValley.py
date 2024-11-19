#!/usr/bin/python
# Filename: MarineValley.py
# Description: Implementation of the marine valley class

from cos.model.geography.Sea import Sea, Type
from cos.core.kernel.Context import Context

class MarineValley(Sea):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Sea.__init__( self, ctxt, Type.MARINE_VALLEY, id, config )
		return



if __name__ == "__main__":
	test = MarineValley()


