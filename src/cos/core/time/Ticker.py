#!/usr/bin/python
# Filename: Ticker.py
# Description: Implementation of the Ticker class

import time

class Ticker:
	def __init__(self, timeout, clock=None):
		""" Constructor
		Arguments
			timeout -- Timeout for the ticker, in seconds
			clock -- Simulated clock to count in; None counts host seconds
		"""
		self.clock			= clock
		self.timeout		= timeout
		self.last_tick		= self.now()
		return

	def now(self):
		""" Returns the current time in the ticker's seconds
		"""
		if self.clock is None:
			return time.time()
		return self.clock.seconds

	def signaled(self):
		""" Checks if the ticker is signaled.
		"""
		if self.timeout < 0:
			return

		tick		= self.now()
		elapsed		= tick-self.last_tick

		if self.clock is None:
			elapsed	= int(elapsed)
			fired	= elapsed > self.timeout
		else:
			fired	= elapsed >= self.timeout

		if (elapsed< 0) or fired:
			self.last_tick	= tick
			return True

		return False



if __name__ == "__main__":
	test = Ticker()


