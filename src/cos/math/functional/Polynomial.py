#!/usr/bin/python
# Filename: Polynomial.py
# Description: Polynomial functor

import numpy as np

class Polynomial:
	def __init__(self, coeff):
		if coeff is None:
			self.coeff		= []
		else:
			self.coeff		= coeff
		return

	def differential(self):
		c 	= []
		n	= len(self.coeff)
		if n == 0:
			return Polynomial()

		degree	= 0

		for i in range(n):
			if degree == 0:
				degree = degree + 1
				continue

			c[degree-1]	= self.coeff[i]*float(degree)
			degree 		= degree + 1

		return Polynomial(c)

	def __str__(self):
		s		= []
		prefix	= ''
		epsilon	= np.finfo(float).eps
		for i in range(len(self.coeff)):
			a	=self.coeff[i]
			if abs(a) < epsilon:
				continue

			if i == 0:
				s.append(str(a))
				prefix	= '+'
			elif i == 1:
				s.append(f'{prefix}{a}x')
				prefix	= '+'
			else:
				s.append(f'{prefix}{a}x^{i}')
				prefix	= '+'

		return ''.join(s)

	def __call__(self, x):
		n		= len(self.coeff)

		# A polynomial is defined by the function
		#		f(x) = a0 + a1 x + a2 x^2 + .... + an x^n

		if n == 0:
			return 0
		elif n == 1:
			return self.coeff[0]
		
		r		= 0.0
		x_pow_n	= 1.0
		
		for i in range(n):
			a	= self.coeff[i]

			if i == 0:
				result	= a
			else:
				result	= result+x_pow_n * a

			x_pow_n		= x_pow_n*x
		
		return result

		

if __name__ == "__main__":
	test = Polynomial()

