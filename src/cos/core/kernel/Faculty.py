#!/usr/bin/python
# Filename: Faculty.py
# Description: Base class for all faculties

from cos.core.kernel.Object import Object

class Faculty(Object):
	def __init__(self, category, type, name=None):
		""" Constructor
		Arguments
			category -- Category of the object
			type -- Type of the object
			name -- Name of the object
		"""
		if (category is not None) and (type is not None):
			self.bind( category, type, name )

		return
	
	def bind(self, category, type, name):
		""" bind
		Arguments
			category -- Category of the object
			type -- Type of the object
			name -- Name of the object
		"""
		if name is None:
			name	= self.__class__.__name__

		self.scope	= f'Faculty/{category}/{type}'
		Object.__init__( self, self.scope, name )

		self.listen( f'/{self.scope}/{name}' )
		return

	def on_timer(self, ctxt, sim):
		""" Callback handling timer events
		Arguments
			ctxt -- Context of the event
			sim -- Reference ot the simulation
		"""
		return


if __name__ == "__main__":
	test = Faculty()


