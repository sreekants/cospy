#!/usr/bin/python
# Filename: Hold.py
# Description: Hold operator

import numpy as np

class Hold:
	def __init__(self, default=np.nan):
		self.last	= default
		return
	
	def __call__(self, x):
		if np.isnan(x) == False:
			self.last	= x

		return self.last


		

if __name__ == "__main__":
	test = Hold(10)
	print( test(np.nan) )
	print( test(1) )
	print( test(2) )
	print( test(np.nan) )
	print( test(5) )

