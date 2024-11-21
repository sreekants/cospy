#!/usr/bin/python
# Filename: SignalExaminer.py
# Description: Implementation of the SignalExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer

class SignalExaminer(NavigationExaminer):
	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
		return

		

if __name__ == "__main__":
	test = SignalExaminer()

