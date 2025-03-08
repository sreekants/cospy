#!/usr/bin/python
# Filename: Fourier.py
# Description: TODO

import numpy as np

class Fourier:
	def __init__(self, a):
		self.a	= a
		return

	def __call__(self, x):
		result	= 0.0
		halfpi	= np.pi/2.0

		for n in range(len(self.a)):
			result	= result + self.a[n]*np.cos( (2.0*n+1.0)*halfpi*x )

		return result

		

if __name__ == "__main__":
	test = Fourier([2.0])
	print(test(1.0))
	print(2.0*np.cos(np.pi/2.0))

