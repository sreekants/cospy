#!/usr/bin/python
# Filename: Mapping.py
# Description: TODO

class Interpolator:
	def __init__(self, rfrom, rto):
		self.rfrom  = rfrom
		self.rto    = rto
		return
	
	def __call__(self, v):
		return self.rto[0]+ (self.rto[1]-self.rto[0])*(v-self.rfrom[0])/(self.rfrom[1]-self.rfrom[0])

		

if __name__ == "__main__":
	test = Mapping()

