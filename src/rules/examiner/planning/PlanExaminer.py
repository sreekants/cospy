#!/usr/bin/python
# Filename: PlanExaminer.py
# Description: Implementation of the PlanExaminer class

from cos.model.examiner.ConcernExaminer import ConcernExaminer
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

class PlanExaminer(ConcernExaminer):
	def __init__(self):
		""" Constructor
		"""
		ConcernExaminer.__init__(self, 'Planning')
		return

	def evaluate(self, ctxt:Context, situation):
		""" Evaluates the expression
		Arguments
			ctxt -- Simulation context
			situation -- Situation reference
		"""
		# print( f'evaluate {self.scope}/{self.id}' )
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
	test = PlanExaminer()

