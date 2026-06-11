#!/usr/bin/python
# Filename: Score.py
# Description: Implementation of the Score class

class Score:
	def __init__(self, counter=0.0):
		self.counter 	= counter
		self.duration	= 0.0
		return

	def reset(self, counter=0.0):
		self.counter 	= counter
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

