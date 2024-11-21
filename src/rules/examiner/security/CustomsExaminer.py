#!/usr/bin/python
# Filename: CustomsExaminer.py
# Description: Implementation of the CustomsExaminer class

from cos.model.examiner.ConcernExaminer import ConcernExaminer

class CustomsExaminer(ConcernExaminer):
	def __init__(self):
		""" Constructor
		"""
		ConcernExaminer.__init__(self, 'Customs')
		return

		

if __name__ == "__main__":
	test = CustomsExaminer()

