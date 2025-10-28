#!/usr/bin/python
# Filename: CargoExaminer.py
# Description: Implementation of the CargoExaminer class

from cos.model.examiner.ConcernExaminer import ConcernExaminer
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

class CargoExaminer(ConcernExaminer):
	def __init__(self):
		""" Constructor
		"""
		ConcernExaminer.__init__(self, 'Environmental')
		return

	def evaluate(self, ctxt:Context, situation):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			situation -- Situation reference
		"""
		return

	def score(self, ctxt:Context, situation, event:str):
		""" Scores the rule
		Arguments
			ctxt -- Simulation context
			situation -- Situation reference
		"""
		# print( f'score {self.scope}' )
		return
		

if __name__ == "__main__":
	test = CargoExaminer()

