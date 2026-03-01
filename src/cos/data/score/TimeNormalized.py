#!/usr/bin/python
# Filename: TimeNormalized.py
# Description: Implementation of the TimeNormalized class

from Score import Score

class TimeNormalized(Score):
	def __init__(self):
		super().__init__()
		return

	def update( self, counter, duration ):
		self.counter 	= self.counter + counter
		self.duration	= duration
		return

	def evaluate( self ):
		return self.counter/self.duration if self.duration > 0.0 else 0.0


if __name__ == "__main__":
	test = TimeNormalized()
	test.update( 0.0, 1.0 )
	print( test.evaluate() )
	test.update( 5.0, 2.0 )
	print( test.evaluate() )
	test.update( 1.0, 3.0 )
	print( test.evaluate() )
	test.update( 0.0, 4.0 )
	print( test.evaluate() )

