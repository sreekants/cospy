#!/usr/bin/python
# Filename: PowerDrivenVessel.py
# Description: Implementation of a simulation object for a power driven vessel

from maritime.model.vessel.Vessel import Vessel, Type

class PowerDrivenVessel(Vessel):
	def __init__( self, ctxt, id=None, config:dict=None ):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Vessel.__init__( self, ctxt, Type.POWER_DRIVEN, id, config )
		return



if __name__ == "__main__":
	test = PowerDrivenVessel()


