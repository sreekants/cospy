#!/usr/bin/python
# Filename: Event.py
# Description: A class for an IPC Event in the simulation environment

class Event:
	def __init__(self, ctxt, msg, arg):
		""" Constructor
		Arguments
			ctxt -- Simulation context
			msg -- Message of the event
			arg -- Additional processign arguments for the event
		"""
		self.ctxt	= ctxt
		self.msg	= msg
		self.arg	= arg
		return



if __name__ == "__main__":
	test = Event()


