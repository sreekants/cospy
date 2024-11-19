#!/usr/bin/python
# Filename: Clock.py
# Description: Implementation of the Clock class

import datetime, time

class Clock:
	def __init__(self):
		""" Constructor
		"""
		return

	@property
	def utc(self):
		""" Returns the UTC time
		"""
		return int(datetime.datetime.utcnow().timestamp())

	@property
	def tickcount(self):
		""" Returns the tick count
		"""
		return int(time.time())

if __name__ == "__main__":
	test = Clock()


