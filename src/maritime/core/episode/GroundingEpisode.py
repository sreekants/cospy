#!/usr/bin/python
# Filename: GroundingEpisode.py
# Description: Implementation of the GroundingEpisode class

from cos.model.rule.Episode import Episode
from cos.core.utilities.EventId import EventId


class GroundingEpisode(Episode):
	def __init__(self, approach:float, retreat:float):
		""" Constructor
		Arguments
			approach -- Metres from the nearest land at which a closing vessel starts an episode
			retreat -- Metres the vessel must open from its closest distance to end the episode
		"""
		Episode.__init__( self )
		self.approach	= float( approach )
		self.retreat	= float( retreat )
		self.id			= None		# Episode id while one is open
		self.previous	= None		# Distance to land at the last tick
		self.closest	= None		# Smallest distance to land in the open episode
		return

	@property
	def open(self)->bool:
		""" Whether an episode is in progress
		"""
		return self.id is not None

	def start(self, distance:float)->bool:
		""" Whether an episode starts this tick: within approach of land and closing on it
		Arguments
			distance -- Distance from the vessel to the nearest land, e.g. (OwnShip,Map.Land).Distance
		"""
		previous		= self.previous
		self.previous	= distance

		if self.open or (distance is None) or (previous is None):
			return False

		if (distance <= self.approach) and (distance < previous):
			self.id			= EventId.next()
			self.closest	= distance
			return True
		return False

	def end(self, distance:float)->bool:
		""" Whether the open episode ends this tick: the vessel has opened retreat from its closest distance
		Arguments
			distance -- Distance from the vessel to the nearest land
		"""
		if (self.open == False) or (distance is None):
			return False

		self.closest	= min( self.closest, distance )
		if distance - self.closest < self.retreat:
			return False

		self.id			= None
		self.closest	= None
		return True



if __name__ == "__main__":
	test = GroundingEpisode( 500.0, 100.0 )
