#!/usr/bin/python
# Filename: Exception.py
# Description: Base class for an decision exception

from cos.model.logic.Expression import Expression

class Exception:
	def __init__(self, expression:Expression):
		""" Constructor
		Arguments
			expression -- #TODO
		"""
		self.expression	= expression
		return

	def evaluate(self, ctxt):
		""" Evaluates an expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.expression.evaluate(ctxt)



if __name__ == "__main__":
	test = Exception()


