#!/usr/bin/python
# Filename: Situation.py
# Description: Enumerations and states of encounter situations that occur in shipping

from cos.core.kernel.Faculty import Faculty

class Situation(Faculty):
	def __init__(self, category, type):
		""" Constructor
		Arguments
			category -- Category of the object
			type -- Type of the object
		"""
		Faculty.__init__( self, category, type )
		self.listen( f'/{category}/{type}/{self.__class__.__name__}' )
		return



if __name__ == "__main__":
	test = Situation()


