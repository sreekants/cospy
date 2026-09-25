#!/usr/bin/python
# Filename: Situation.py
# Description: Implementation of the Rule Situation class

class Situation:
	def __init__(self, OS=None, TS=None):
		""" Constructor
		"""
		self.maneuvers	= {}
		self.approaches	= {}

		# Context attributes
		self.zone		= None
		self.eez		= None
		self.harbour	= None
		self.lane		= None
		self.mez		= None
		self.tss		= None
		self.os			= OS
		self.ts			= TS
		self.fleet		= Situation.fleet_of( OS, TS )	# COS.005
		return

	@staticmethod
	def fleet_of(OS, TS):
		""" The fleet in scope: the target's, else own ship's
		Arguments
			OS -- Own ship
			TS -- Target ship
		"""
		for vessel in (TS, OS):
			fleet	= getattr( vessel, 'fleet', None )
			if fleet is not None:
				return fleet
		return None



if __name__ == "__main__":
	test = Situation()


