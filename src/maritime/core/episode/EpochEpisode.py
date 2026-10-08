#!/usr/bin/python
# Filename: EpochEpisode.py
# Description: Implementation of the EpochEpisode class

from cos.model.rule.Episode import Episode
from cos.core.utilities.EventId import EventId


class EpochEpisode(Episode):
	def __init__(self, ticks:int):
		""" Constructor
		Arguments
			ticks -- Length of the timeslice, in ticks
		"""
		Episode.__init__( self )
		if int( ticks ) < 1:
			raise ValueError( f'EpochEpisode: a timeslice is at least one tick, not {ticks}' )

		self.ticks		= int( ticks )
		self.id			= None		# Episode id while one is open
		self.began		= None		# Tick the open timeslice began at
		self.situations	= []		# Situations active at any tick of the timeslice
		self.context	= None		# Rule context of the pass that ended the timeslice
		return

	@property
	def open(self)->bool:
		""" Whether a timeslice is in progress
		"""
		return self.id is not None

	def start(self, tick:int)->bool:
		""" Whether a timeslice starts this tick: one starts whenever none is open
		Arguments
			tick -- Current tick
		"""
		if self.open:
			return False

		self.id			= EventId.next()
		self.began		= tick
		self.situations	= []
		return True

	def observe(self, situations):
		""" Adds the situations active this tick to the timeslice
		Arguments
			situations -- Active situations, e.g. a vessel's situations
		"""
		if self.open == False:
			return

		for s in situations:
			if s not in self.situations:
				self.situations.append( s )
		return

	def end(self, tick:int)->bool:
		""" Whether the open timeslice ends this tick: it has lasted its configured ticks
		Arguments
			tick -- Current tick
		"""
		if (self.open == False) or (tick - self.began < self.ticks):
			return False

		self.id			= None
		return True



if __name__ == "__main__":
	test = EpochEpisode( 10 )
