#!/usr/bin/python
# Filename: LaneDisciplineExaminer.py
# Description: Implementation of the LaneDisciplineExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer

class LaneDisciplineExaminer(NavigationExaminer):
	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
		return

		

if __name__ == "__main__":
	test = LaneDisciplineExaminer()

