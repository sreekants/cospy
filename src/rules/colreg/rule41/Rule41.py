#!/usr/bin/python
# Filename: Rule41.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Verification of compliance
(a) Every Contracting Party shall be subject to periodic audits by the Organization in
accordance with the audit standard to verify compliance with and implementation of
the present Convention.
(b) The Secretary-General of the Organization shall have responsibility for
administering the Audit Scheme, based on the guidelines developed by the
Organization*.
(c) Every Contracting Party shall have responsibility for facilitating the conduct of the
audit and implementation of a programme of actions to address the findings, based on
the guidelines developed by the Organization*.
(d) Audit of all Contracting Parties shall be:
(i) based on an overall schedule developed by the Secretary-General of the
Organization, taking into account the guidelines developed by the Organization*;
and
(ii) conducted at periodic intervals, taking into account the guidelines developed by
the Organization*.
* Refer to the Framework and Procedures for the IMO Member State Audit Scheme,
adopted by the Organization by resolution A.1067(28).
'''

class Rule41(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule41()

