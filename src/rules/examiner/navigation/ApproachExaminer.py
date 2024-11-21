#!/usr/bin/python
# Filename: ApproachExaminer.py
# Description: Implementation of the ApproachExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer

class ApproachExaminer(NavigationExaminer):
	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
		return

		

if __name__ == "__main__":
	test = ApproachExaminer()

