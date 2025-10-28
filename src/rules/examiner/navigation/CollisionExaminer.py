#!/usr/bin/python
# Filename: CollisionExaminer.py
# Description: Implementation of the CollisionExaminer class

from rules.examiner.navigation.NavigationExaminer import NavigationExaminer
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

class CollisionExaminer(NavigationExaminer):
	def __init__(self):
		""" Constructor
		"""
		NavigationExaminer.__init__(self)
		return

		

if __name__ == "__main__":
	test = CollisionExaminer()

