#!/usr/bin/python
# Filename: RuleDefinition.py
# Description: Definitions used by the rules

from cos.model.logic.DecisionTree import DecisionTree
from cos.model.logic.Decision import Decision
from cos.core.utilities.Tree import Tree

class Definition(DecisionTree):
	def __init__(self):
		""" Constructor
		""" 
		DecisionTree.__init__(self, Decision())
		return


if __name__ == "__main__":
	test = Definition()


