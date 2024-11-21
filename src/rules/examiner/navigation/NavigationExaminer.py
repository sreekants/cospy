#!/usr/bin/python
# Filename: NavigationExaminer.py
# Description: Implementation of the NavigationExaminer class

from cos.model.examiner.ConcernExaminer import ConcernExaminer

class NavigationExaminer(ConcernExaminer):
	def __init__(self):
		""" Constructor
		"""
		ConcernExaminer.__init__(self, 'Navigation')
		return

		

if __name__ == "__main__":
	test = NavigationExaminer()

