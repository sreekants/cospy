#!/usr/bin/python
# Filename: Scales.py
# Description: Implementation of the Scales class

from cos.model.environment.Types import DynamicForce

import numpy as np

class Scales:
	def __init__(self):
		""" Constructor
		"""
		unit_vector	= np.ones(3)

		# Scaling vector for maps
		self.map		= unit_vector

		# Scaling vectors for environmental forces
		self.weather	= {
				DynamicForce.WIND_CURRENT: unit_vector,
				DynamicForce.SEA_CURRENT: unit_vector,
				DynamicForce.SEA_WAVE: unit_vector
			}
		return


	def transpose(self, x):
		scale	= self.map
		return (x[0]*scale[0], x[1]*scale[1])


if __name__ == "__main__":
	test = Scales()


