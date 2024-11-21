#!/usr/bin/python
# Filename: EconomicExaminer.py
# Description: Implementation of the EconomicExaminer class

from cos.model.examiner.ConcernExaminer import ConcernExaminer

class EconomicExaminer(ConcernExaminer):
	def __init__(self):
		""" Constructor
		"""
		ConcernExaminer.__init__(self, 'Planning')
		return

		

if __name__ == "__main__":
	test = EconomicExaminer()

