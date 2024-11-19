#!/usr/bin/python
# Filename: AbyssalPlain.py
# Description: Implementation of the abyssal plain class

from cos.model.geography.Sea import Sea, Type

class AbyssalPlain(Sea):
	def __init__( self, id=None, config=None ):
		""" Constructor
		Arguments
			id -- Unique identifier
			config -- Configuration attributes
		"""
		Sea.__init__( self, Type.ABYSSAL_PLAIN, id, config )
		return



if __name__ == "__main__":
	test = AbyssalPlain()


