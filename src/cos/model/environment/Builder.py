#!/usr/bin/python
# Filename: Builder.py
# Description: Base class for all environment builders

from cos.core.simulation.Builder import Builder as BuilderBaseClass
from cos.core.kernel.Context import Context
from cos.core.kernel.BootLoader import BootLoader
from cos.core.utilities.ActiveRecord import ActiveRecord

class Builder(BuilderBaseClass):
	def __init__(self, category, type, model, table, prototypes):
		""" Constructor
		Arguments
			category -- Category of the object
			type -- Type of the object
			model -- #TODO
			table -- #TODO
			prototypes -- #TODO
		"""
		BuilderBaseClass.__init__(self, category, type, model, table, prototypes)
		return


if __name__ == "__main__":
	test = Builder()


