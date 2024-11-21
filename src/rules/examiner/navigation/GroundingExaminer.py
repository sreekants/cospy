#!/usr/bin/python
# Filename: GroundingExaminer.py
# Description: Implementation of COLREG Rule

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer

class GroundingExaminer(NavigationExaminer):
	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
		return



if __name__ == "__main__":
	test = GroundingExaminer()


