#!/usr/bin/python
# Filename: SpeedExaminer.py
# Description: Implementation of the SpeedExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer

class SpeedExaminer(NavigationExaminer):
	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
		return

		

if __name__ == "__main__":
	test = SpeedExaminer()

