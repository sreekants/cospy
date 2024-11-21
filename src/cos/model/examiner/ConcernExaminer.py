#!/usr/bin/python
# Filename: Concern.py
# Description: Base class for all rules

from cos.model.examiner.Examiner import Examiner
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

class ConcernExaminer(Examiner):
	def __init__(self, type):
		""" Constructor
		Arguments
			type -- Type of the object
		"""
		Examiner.__init__( self, type )
		return



if __name__ == "__main__":
	test = ConcernExaminer()


