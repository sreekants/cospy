#!/usr/bin/python
# Filename: Fleet.py
# Description: Implementation of a fleet controller: a meta vessel that flies its members, not a vessel at sea

from maritime.model.vessel.Vessel import Vessel, Type

class Fleet(Vessel):
	def __init__( self, ctxt, id=None, config:dict=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Vessel.__init__( self, ctxt, Type.FLEET, id, config )
		return



if __name__ == "__main__":
	test = Fleet()


