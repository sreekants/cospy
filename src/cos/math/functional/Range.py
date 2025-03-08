#!/usr/bin/python
# Filename: Range.py
# Description: TODO

class Range:
	def __init__(self, bound):
		if bound[0] > bound[1]:
			self.bound	= (bound[1], bound[0])
		else:
			self.bound	= bound
		return

	def __call__(self, x):
		if x < self.bound[0]:
			return self.bound[0]
		
		if x > self.bound[1]:
			return self.bound[1]
		
		return x

		

if __name__ == "__main__":
	test = Range((5, 10))

	print( test(0) )		#  5
	print( test(8) )		#  8
	print( test(10) )		# 10
	print( test(11) )		# 10
