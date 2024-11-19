#!/usr/bin/python
# Filename: Dispatcher.py
# Description: Implementation of the Dispatcher class

class Dispatcher:
	def __init__(self, world):
		""" Constructor
		Arguments
			world -- Reference ot the simulation world
		"""
		self.world		= world
		self.callbacks	= {}
		return

	def subscribe(self, method, handler):
		""" Register a handler on the dispatcher
		Arguments
			method -- Method name
			handler -- Handler for the method
		"""
		self.callbacks[method]	= handler
		return

	def notify(self, evt):
		""" Notifies an event on the dispatcher
		Arguments
			evt -- Event data
		"""
		for frame in evt.d:
			method	= frame["m"]
			args 	= frame["d"]
			if method in self.callbacks:
				for arg in args:
					self.callbacks[method](arg)

		return


if __name__ == "__main__":
	test = Dispatcher()


