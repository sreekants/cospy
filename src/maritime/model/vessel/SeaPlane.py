#!/usr/bin/python
# Filename: SeaPlane.py
# Description: Implementation of a simulation object for a sea plane

from maritime.model.vessel.Vessel import Vessel, Type

class SeaPlane(Vessel):
	def __init__( self, ctxt, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Vessel.__init__( self, ctxt, Type.SEAPLANE, id, config )
		return



if __name__ == "__main__":
	test = SeaPlane()


