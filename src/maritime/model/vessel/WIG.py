#!/usr/bin/python
# Filename: WIG.py
# Description: Implementation of a simulation object for a WIG

from maritime.model.vessel.Vessel import Vessel, Type

class WIG:
	def __init__( self, ctxt, id=None, config:dict=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Vessel.__init__( self, ctxt, Type.WIG, id, config )
		return



if __name__ == "__main__":
	test = WIG()


