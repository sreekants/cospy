#!/usr/bin/python
# Filename: Episode.py
# Description: Implementation of the Episode class


from abc import ABC, abstractmethod

class Episode:
	def __init__(self):
		""" Constructor
		"""
		self.at				= None
		self.duration		= None
		self.situations		= list()		# TODO: Should this be a map?
		self.auto_append	= False
		return

	def append(self, situation:object):
		if self.auto_append == False:
			return
		
		if situation is None:
			return
		
		if situation in self.situations:
			return
		
		self.situations.append(situation) 
		return
	
	def evaluate( self, ctxt:object, vehicle:object, situation:object )->bool:
		""" Overridable to check if a context has concluded
		Arguments
			ctxt -- rule context 
			vehicle -- vehicle involved
			situation -- situation being evaluated
		"""
		if self.at is None:
			if self.start(ctxt, vehicle, situation) == False:
				return
			self.start	= ctxt.sim.tickcount()
			return
		else:
			self.append(situation) 

			if self.end(ctxt, vehicle, situation) == False:
				return
			
			self.duration	= ctxt.sim.tickcount()-self.start
			return
		return

	@abstractmethod
	def start( self, ctxt:object, vehicle:object, situation:object )->bool:
		""" Overridable to check if a context has concluded
		Arguments
			ctxt -- rule context 
			vehicle -- vehicle involved
			situation -- situation being evaluated
		"""
		pass

	@abstractmethod
	def end( self, ctxt:object, vehicle:object, situation:object )->bool:
		""" Overridable to check if a context has concluded
		Arguments
			ctxt -- rule context 
			vehicle -- vehicle involved
			situation -- situation being evaluated
		"""
		pass
		

if __name__ == "__main__":
	test = Episode()

