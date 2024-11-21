#!/usr/bin/python
# Filename: OvertakingExaminer.py
# Description: Implementation of the OvertakingExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer

class OvertakingExaminer(NavigationExaminer):
	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
		return

		

if __name__ == "__main__":
	test = OvertakingExaminer()

