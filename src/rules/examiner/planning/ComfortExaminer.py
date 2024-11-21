#!/usr/bin/python
# Filename: ComfortExaminer.py
# Description: Implementation of the ComfortExaminer class

from cos.model.examiner.ConcernExaminer import ConcernExaminer

class ComfortExaminer(ConcernExaminer):
	def __init__(self):
		""" Constructor
		"""
		ConcernExaminer.__init__(self, 'Planning')
		return

		

if __name__ == "__main__":
	test = ComfortExaminer()

