#!/usr/bin/python
# Filename: Binary.py
# Description: Implementation of the Binary class

from Score import Score

class Binary(Score):
	def __init__(self):
		super().__init__()
		return

	def update( self, counter, duration ):
		if self.counter == 0.0 and counter > 0.0:
			self.counter = 1.0
		return

if __name__ == "__main__":
	test = Binary()
	test.update( 0.0, 1.0 )
	print( test.evaluate() )
	test.update( 1.0, 2.0 )
	print( test.evaluate() )
	test.update( 5.0, 3.0 )
	print( test.evaluate() )
	test.update( 0.0, 4.0 )
	print( test.evaluate() )

