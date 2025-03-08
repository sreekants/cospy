#!/usr/bin/python
# Filename: Absolute.py
# Description: Absolute value functor

class Absolute:
	def __init__(self):
		return

	def __call__(self, x):
		return abs(x)
		

if __name__ == "__main__":
	test = Absolute()

