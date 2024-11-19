#!/usr/bin/python
# Filename: ContinentalShelfPlain.py
# Description: Implementation of the continental_shelf_plain class

from cos.model.geography.Sea import Sea, Type
from cos.core.kernel.Context import Context

class ContinentalShelfPlain(Sea):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Sea.__init__( self, ctxt, Type.CONTINENTAL_SHELF_PLAIN, id, config )
		return



if __name__ == "__main__":
	test = ContinentalShelfPlain()


