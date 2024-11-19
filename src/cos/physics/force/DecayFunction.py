#!/usr/bin/python
# Filename: DecayFunction.py
# Description: Implementation of the DecayFunctions class

import math

# Reference: https://en.wikipedia.org/wiki/Exponential_decay
class ExponentialDecay:
	def __init__(self, rate):
		""" Constructor
		Arguments
				rate -- Decay rate
		"""
		self.λ	= float(rate)
		return

	def mean(self):
		""" Mean of the decay function
		"""
		return 1.0/self.λ

	def halflife(self):
		""" Halflife to decay
		"""
		return math.log(2.0)/self.λ

	def __call__(self, N0, t):
		""" Calculate the value of the function at an epoch
		Arguments
			N0 -- initial value
			t -- Time duration or distance from initial value
		"""
		return N0 * math.exp(-self.λ*t)

if __name__ == "__main__":
	test = ExponentialDecay()


