#!/usr/bin/python
# Filename: Behavior.py
# Description: Implementation of the Behavior class

from enum import Enum

class ActorBehavior(Enum):
	"""Enum for the behavior classes for an actor."""
	# These are for simulation behaviors for simulation actors
	MOTION				= 1001
	DYNAMICS			= 1002
	SENSOR				= 1003

	# These are for control behaviors for simulation actors
	CONTROL_MOTION		= 2001
	CONTROL_DYNAMICS	= 2002
	CONTROL_SENSOR		= 2003

class Behavior:
	def __init__(self, type:ActorBehavior):
		""" Constructor
		Arguments
			type -- Type of the behavior
		"""
		self.type	= type
		return

		
	def intialize(self, actor, vehicle, config:dict):
		""" Initialize the behavior for the actor
		Arguments
			actor -- Actor to initialize the behavior for
			vehicle -- Vehicle object to create the actor for
			config -- Configuration attributes
		"""
		return

	def runnable(self, ctxt, config):
		""" Checks if the behavior is runnable
		Arguments
			ctxt -- Simulation context
			config -- Config information
		"""
		return True

	def notify(self, ctxt, method:str, arg:dict):
		""" Triggers a method
		Arguments
			ctxt -- Simulation context
			method -- Method name
			arg -- Message argumnt
		"""
		return
	
if __name__ == "__main__":
	test = Behavior()

