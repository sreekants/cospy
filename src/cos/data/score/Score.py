#!/usr/bin/python
# Filename: Score.py
# Description: Implementation of the Score class

class Score:
	def __init__(self):
		self.counter 	= 0.0
		self.duration	= 0.0
		return

	def reset(self):
		self.counter 	= 0.0
		self.duration	= 0.0
		return
	
	def update( self, counter, duration ):
		self.counter 	= counter
		self.duration	= duration
		return
	
	def evaluate( self ):
		return self.counter
		

if __name__ == "__main__":
	test = Score()

