#!/usr/bin/python
# Filename: NumericRange.py
# Description: A numeric range comparator

class NumericRange:
	def __init__(self, range):
		self.range	= range

	def __contains__(self, item):
		return True if (self.range[0]<=item) and (self.range[1]>=item) else False

		

if __name__ == "__main__":
	test = NumericRange()

