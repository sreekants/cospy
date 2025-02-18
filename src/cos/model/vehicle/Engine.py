#!/usr/bin/python
# Filename: Engine.py
# Description: Implement the engine collection

from cos.model.vehicle.ValueSet import ValueSet

class State(ValueSet):
	def __init__(self):
		ValueSet.__init__(self)
		return

class Engine:
	def __init__(self):
		self.state	= State()
		return

if __name__ == "__main__":
	test = Engine()

