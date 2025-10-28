#!/usr/bin/python
# Filename: DayTimeExaminer.py
# Description: Implementation of the DayTimeExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

class DayTimeExaminer(NavigationExaminer):
	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
		return

		

if __name__ == "__main__":
	test = DayTimeExaminer()

