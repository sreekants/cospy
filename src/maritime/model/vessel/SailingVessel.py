#!/usr/bin/python
# Filename: SailingVessel.py
# Description: Implementation of a simulation object for a saling vessel

from maritime.model.vessel.Vessel import Vessel, Type

class SailingVessel(Vessel):
	def __init__( self, ctxt, id=None, config=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Vessel.__init__( self, ctxt, Type.SAILING, config )
		return



if __name__ == "__main__":
	test = SailingVessel()


