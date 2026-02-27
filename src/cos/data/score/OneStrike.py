#!/usr/bin/python
# Filename: OneStrike.py
# Description: Implementation of the OneStrike class

from Score import Score

class OneStrike(Score):
	def __init__(self):
		super().__init__()
		return

	def update( self, counter, duration ):
		if self.counter == 0.0 and counter > 0.0:
			self.counter = counter
		return

if __name__ == "__main__":
	test = OneStrike()
	test.update( 0.0, 1.0 )
	print( test.evaluate() )
	test.update( 5.0, 2.0 )
	print( test.evaluate() )
	test.update( 1.0, 3.0 )
	print( test.evaluate() )
	test.update( 0.0, 4.0 )
	print( test.evaluate() )

