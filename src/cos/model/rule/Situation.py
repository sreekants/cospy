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
		return



if __name__ == "__main__":
	test = Situation()


