#!/usr/bin/python
# Filename: Rule39.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Definitions
(a) Audit means a systematic, independent and documented process for obtaining
audit evidence and evaluating it objectively to determine the extent to which audit
criteria are fulfilled.
(b) Audit Scheme means the IMO Member State Audit Scheme established by the
Organization and taking into account the guidelines developed by the
Organization*.
* Refer to the Framework and Procedures for the IMO Member State Audit Scheme,
adopted by the Organization by resolution A.1067(28).
(c) Code for Implementation means the IMO Instruments Implementation Code (III
Code) adopted by the Organization by resolution A.1070(28).
(d) Audit Standard means the Code for Implementation.
'''

class Rule39(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule39()


