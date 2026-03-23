#!/usr/bin/python
# Filename: Clock.py
# Description: Implementation of the Clock class

import datetime, time

class Clock:
	def __init__(self):
		""" Constructor
		"""
		self.starttime	= time.time()
		return

	@property
	def utc(self):
		""" Returns the UTC time
		"""
		return datetime.datetime.now()

	@property
	def tickcount(self):
		""" Returns the tick count
		"""
		return round(time.time() - self.starttime, 4)

if __name__ == "__main__":
	test = Clock()


