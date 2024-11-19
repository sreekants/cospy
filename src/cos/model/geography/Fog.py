#!/usr/bin/python
# Filename: Fog.py
# Description: Implementation of the fog weather system class

from cos.model.geography.Sky import Sky, Type
from cos.core.kernel.Context import Context

class Fog(Sky):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Sky.__init__( self, ctxt, Type.FOG, id, config )
		return



if __name__ == "__main__":
	test = Fog()


