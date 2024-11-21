#!/usr/bin/python
# Filename: PlanExaminer.py
# Description: Implementation of the PlanExaminer class

from cos.model.examiner.ConcernExaminer import ConcernExaminer

class PlanExaminer(ConcernExaminer):
	def __init__(self):
		""" Constructor
		"""
		ConcernExaminer.__init__(self, 'Planning')
		return

		

if __name__ == "__main__":
	test = PlanExaminer()

