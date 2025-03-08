#!/usr/bin/python
# Filename: Interpolate.py
# Description: Interpolator function

class Interpolate:
	def __init__(self, rfrom, rto):
		self.rfrom  = rfrom
		self.rto    = rto
		return
	
	def __call__(self, x):
		return self.rto[0]+ (self.rto[1]-self.rto[0])*(x-self.rfrom[0])/(self.rfrom[1]-self.rfrom[0])

		

if __name__ == "__main__":
	test = Interpolate( (-40,0), (-40,32) )
	# Celcius to Farenheit convertor
	print( test(0) )		#  32F
	print( test(-40) )		# -40F
	print( test(80) )		# 176F

