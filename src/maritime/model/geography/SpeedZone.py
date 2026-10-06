#!/usr/bin/python
# Filename: SpeedZone.py
# Description: Implementation of the reach with a local speed limit zone class

from cos.model.geography.Sea import Sea, Type
from cos.model.geography.MaritimeZone import MaritimeTrafficZone
from cos.core.kernel.Context import Context


class SpeedZone(MaritimeTrafficZone):
	def __init__( self, ctxt:Context, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		MaritimeTrafficZone.__init__( self, ctxt, Type.SPEED_ZONE, id, config )
		return




if __name__ == "__main__":
	test = SpeedZone()


