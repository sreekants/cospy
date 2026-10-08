#!/usr/bin/python
# Filename: VoyageEpisode.py
# Description: Implementation of the VoyageEpisode class

from cos.model.rule.Episode import Episode


class VoyageEpisode(Episode):
	def __init__(self):
		""" Constructor
		"""
		Episode.__init__( self )
		return

		

if __name__ == "__main__":
	test = VoyageEpisode()

