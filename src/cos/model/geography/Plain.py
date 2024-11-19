#!/usr/bin/python
# Filename: Plain.py
# Description: Implementation of the plain class

from cos.model.geography.Land import Land, Type
from cos.core.kernel.Context import Context

class Plain(Land):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Land.__init__( self, ctxt, Type.PLAIN, id, config )
		return



if __name__ == "__main__":
	test = Plain()


