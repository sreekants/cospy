#!/usr/bin/python
# Filename: NightTimeExaminer.py
# Description: Implementation of the NightTimeExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer

class NightTimeExaminer(NavigationExaminer):
	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
		return

		

if __name__ == "__main__":
	test = NightTimeExaminer()

