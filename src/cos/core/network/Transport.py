#!/usr/bin/python
# Filename: WebSocketTransport.py
# Description: Implementation of the Transport class


class Transport:
	def __init__(self, sim, broker, args:dict):
		""" Constructor
		Arguments
			sim -- Reference ot the simulation
			broker -- Broker name
			args -- List of arguments
		"""

		self.sim		= sim
		self.broker		= broker
		return

	def __enter__(self):
		""" Called when locked
		"""
		self.create()
		return self

	def __exit__(self, exception_type, exception_value, exception_traceback):
		""" Called when exception occurs
		Arguments
			exception_type -- Type of exception
			exception_value -- Valie of the exception
			exception_traceback -- Exception stack
		"""
		self.close()
		return


		

if __name__ == "__main__":
	test = Transport()

