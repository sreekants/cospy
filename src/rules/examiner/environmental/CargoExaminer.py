#!/usr/bin/python
# Filename: CargoExaminer.py
# Description: Implementation of the CargoExaminer class

from cos.model.examiner.ConcernExaminer import ConcernExaminer

class CargoExaminer(ConcernExaminer):
	def __init__(self):
		""" Constructor
		"""
		ConcernExaminer.__init__(self, 'Environmental')
		return

		

if __name__ == "__main__":
	test = CargoExaminer()

