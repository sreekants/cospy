#!/usr/bin/python
# Filename: Topic.py
# Description: A message topic on the message queue

import queue, fnmatch

class Topic:
	def __init__(self):
		""" Constructor
		"""
		self.queue			= queue.Queue()
		self.subscribers	= []
		self.throttle_rate	= 100000
		return


if __name__ == "__main__":
	test = Topic()


