#!/usr/bin/python
# Filename: EncounterEpisode.py
# Description: Implementation of the EncounterEpisode class

from cos.model.rule.Episode import Episode


class EncounterEpisode(Episode):
	def __init__(self):
		""" Constructor
		"""
		Episode.__init__( self )
		return

		

if __name__ == "__main__":
	test = EncounterEpisode()

