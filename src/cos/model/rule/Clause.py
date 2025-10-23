#!/usr/bin/python
# Filename: Clause.py
# Description: A rule clause decision

from cos.lang.logic.Decision import Decision, DecisionType

class Clause(Decision):
	def __init__(self, name:str=None, parent=None, type=DecisionType.TYPE_NULL_OBJECT, ref=None):
		""" Constructor
		Arguments
			name -- Name of the object
			parent -- #TODO
			type -- Type of the object
			ref -- #TODO
		"""
		Decision.__init__(self, str, parent, type, ref)
		return


if __name__ == "__main__":
	test = Clause()


