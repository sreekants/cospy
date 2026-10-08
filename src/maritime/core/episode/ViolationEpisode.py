#!/usr/bin/python
# Filename: ViolationEpisode.py
# Description: Implementation of the ViolationEpisode class

from cos.model.rule.Episode import Episode


class ViolationEpisode(Episode):
	def __init__(self):
		""" Constructor
		"""
		Episode.__init__( self )
		return

		

if __name__ == "__main__":
	test = ViolationEpisode()

