#!/usr/bin/python
# Filename: Ticker.py
# Description: Implementation of the Ticker class

import time

class Ticker:
	def __init__(self, timeout):
		""" Constructor
		Arguments
			timeout -- Timeout for the ticker
		"""
		self.last_tick		= time.time()
		self.timeout		= timeout
		return

	def signaled(self):
		""" Checks if the ticker is signaled.
		"""
		if self.timeout < 0:
			return

		tick		= time.time()
		elapsed		= int(tick-self.last_tick)

		if (elapsed< 0) or (elapsed > self.timeout):
			self.last_tick	= tick
			return True

		return False



if __name__ == "__main__":
	test = Ticker()


