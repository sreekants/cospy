#!/usr/bin/python
# Filename: ZoneViolationExaminer.py
# Description: Implementation of the ZoneViolationExaminer class

from cos.model.examiner.ConcernExaminer import ConcernExaminer

class ZoneViolationExaminer(ConcernExaminer):
	def __init__(self):
		""" Constructor
		"""
		ConcernExaminer.__init__(self, 'Customs')
		return

		

if __name__ == "__main__":
	test = ZoneViolationExaminer()

