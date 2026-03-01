#!/usr/bin/python
# Filename: Cumulative.py
# Description: Implementation of the Cumulative class

from Score import Score

class Cumulative(Score):
	def __init__(self):
		super().__init__()
		return

	def update( self, counter, duration ):
		self.counter 	= self.counter + counter
		return
		

if __name__ == "__main__":
	test = Cumulative()
	test.update( 0.0, 1.0 )
	print( test.evaluate() )
	test.update( 5.0, 2.0 )
	print( test.evaluate() )
	test.update( 1.0, 3.0 )
	print( test.evaluate() )
	test.update( 0.0, 4.0 )
	print( test.evaluate() )
