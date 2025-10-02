#!/usr/bin/python
# Filename: Assurance.py
# Description: Base class for an decision assurance 

from cos.lang.logic.Expression import Expression
from cos.core.utilities.Errors import ErrorCode

from abc import ABC, abstractmethod

class Assurance(ABC):
	def __init__(self, expression):
		""" Constructor
		Arguments
			expression -- #TODO
		"""
		self.expession	= expression
		return

	@abstractmethod
	def apply(self, ctxt):
		""" #TODO: apply
		Arguments
			ctxt -- Simulation context
		"""
		pass



if __name__ == "__main__":
	test = Assurance()


