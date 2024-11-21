#!/usr/bin/python
# Filename: BerthingExaminer.py
# Description: Implementation of the BerthingExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer

class BerthingExaminer(NavigationExaminer):
	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
		return

		

if __name__ == "__main__":
	test = BerthingExaminer()

