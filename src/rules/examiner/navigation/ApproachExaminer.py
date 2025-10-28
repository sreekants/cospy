#!/usr/bin/python
# Filename: ApproachExaminer.py
# Description: Implementation of the ApproachExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

class ApproachExaminer(NavigationExaminer):
	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
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
	test = ApproachExaminer()

