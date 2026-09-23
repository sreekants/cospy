#!/usr/bin/python
# Filename: CustomsExaminer.py
# Description: Implementation of the CustomsExaminer class

from cos.model.examiner.Examiner import Examiner
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

class TestInspector(Examiner):
	def __init__(self, type):
		""" Constructor
		Arguments
			type -- Type of the object
		"""
		Examiner.__init__( self, type )
		return
		

if __name__ == "__main__":
	test = TestInspector()

