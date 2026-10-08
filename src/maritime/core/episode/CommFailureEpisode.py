#!/usr/bin/python
# Filename: CommFailureEpisode.py
# Description: Implementation of the CommFailureEpisode class

from cos.model.rule.Episode import Episode


class CommFailureEpisode(Episode):
	def __init__(self):
		""" Constructor
		"""
		Episode.__init__( self )
		return

		

if __name__ == "__main__":
	test = CommFailureEpisode()

