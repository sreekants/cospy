#!/usr/bin/python
# Filename: Pipeline.py
# Description: Pipeline of functions

class Pipeline(list):
	def __init__(self, plant=None):
		self.e		= None
		self.plant	= plant
		return

	def feed(self, e):
		self.e	= e
		return

	def __call__(self, x):
		# Handle the error feedback
		if self.e is not None:
			x	= x + self.e

		for fn in self:
			x	= fn(x)

		# If the tail end of the pipeline has a plant as in a 
		# PID controller, we use it to calculate the error
		if self.plant is not None:
			x 		= self.plant(x)
			self.e	= x

		return x
		

if __name__ == "__main__":
	test = Pipeline()

