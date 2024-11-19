#!/usr/bin/python
# Filename: Cloud.py
# Description: Implementation of the cloud class

from cos.model.geography.Sky import Sky, Type
from cos.core.kernel.Context import Context

class Cloud(Sky):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Sky.__init__( self, ctxt, Type.CLOUD, id, config )
		return



if __name__ == "__main__":
	test = Cloud()


