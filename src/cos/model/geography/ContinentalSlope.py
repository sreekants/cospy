#!/usr/bin/python
# Filename: ContinentalSlope.py
# Description: Implementation of the continental_slope class

from cos.model.geography.Sea import Sea, Type
from cos.core.kernel.Context import Context

class ContinentalSlope(Sea):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Sea.__init__( self, ctxt, Type.CONTINENTAL_SLOPE, id, config )
		return



if __name__ == "__main__":
	test = ContinentalSlope()


