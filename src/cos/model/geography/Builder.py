#!/usr/bin/python
# Filename: Builder.py
# Description: Base class for all geography builders

from cos.core.simulation.Builder import Builder as BuilderBase

class Builder(BuilderBase):
	def __init__(self, category, type, model, table, prototypes):
		""" Constructor
		Arguments
			category -- Category of the object
			type -- Type of the object
			model -- Model name
			table -- Table name
			prototypes -- Prototype definition for types of objects
		"""
		BuilderBase.__init__(self, category, type, model, table, prototypes)
		return



if __name__ == "__main__":
	test = Builder()


