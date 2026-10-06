#!/usr/bin/python
# Filename: NatureReserve.py
# Description: Implementation of the protected marine area zone class

from cos.model.geography.Sea import Sea, Type
from cos.model.geography.MaritimeZone import MaritimeTrafficZone
from cos.core.kernel.Context import Context


class NatureReserve(MaritimeTrafficZone):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		MaritimeTrafficZone.__init__( self, ctxt, Type.NATURE_RESERVE, id, config )
		return




if __name__ == "__main__":
	test = NatureReserve()


