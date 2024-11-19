#!/usr/bin/python
# Filename: GrowthFunction.py
# Description: Implementation of the DecayFunctions class

import math

# Reference: https://en.wikipedia.org/wiki/Exponential_growth
class ExponentialGrowth:
	def __init__(self, a, b, tau):
		""" Constructor
		Arguments
				a -- growth rate
			tau -- time for the growth
		"""
		self.a	= float(a)
		self.τ	= float(tau)
		return

	def doubling_time(self):
		""" Doubling time for the growth
		"""
		return math.log(2.0)*self.τ

	def folding_time(self, scale):
		""" Folding time for the growth
		Arguments
			scale -- Scale of the growth
		"""
		return math.log(scale)*self.τ

	def growth_constant(self, scale):
		""" Growth constant
		Arguments
			scale -- Scale of the growth
		"""
		return 1.0/self.τ

	def __call__(self, x0, t):
		""" Calculate the value of the function at an epoch
		Arguments
			x0 -- initial value
			t -- Time duration or distance from initial value
		"""
		return x0 * math.exp(t/self.τ)

if __name__ == "__main__":
	test = ExponentialDecay()


