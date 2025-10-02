#!/usr/bin/python
# Filename: Condition.py
# Description: Base class for an decision conditions

from cos.model.logic.Expression import Expression

class Condition:
	def __init__(self, expression:Expression):
		""" Constructor
		Arguments
			expression -- condition expression
		"""
		self.expression	= expression
		return

	def evaluate(self, ctxt):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
		"""
		return self.expression.evaluate(ctxt)



if __name__ == "__main__":
	test = Condition()


