#!/usr/bin/python
# Filename: Rule7.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Risk of Collision
(a) Every vessel shall use all available means appropriate to the prevailing circumstances and
conditions to determine if risk of collision exists. If there is any doubt such risk shall be deemed to
exist.
(b) Proper use shall be made of radar equipment if fitted and operational, including long-range
scanning to obtain early warning of risk of collision and radar plotting or equivalent systematic
observation of detected objects.
(c) Assumptions shall not be made on the basis of scanty information, especially scanty radar
information.
(d) In determining if risk of collision exists the following considerations shall be among those taken
into account:
(i) Such risk shall be deemed to exist if the compass bearing of an approaching vessel does
not appreciably change;
(ii) such risk may sometimes exist even when an appreciable bearing change is evident,
particularly when approaching a very large vessel or a tow or when approaching a vessel
at close range.
'''

class Rule7(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule7()


