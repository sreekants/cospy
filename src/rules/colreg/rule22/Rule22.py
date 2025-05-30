#!/usr/bin/python
# Filename: Rule22.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Visibility of Lights
The lights prescribed in these Rules shall have an intensity as specified in Section 8
Annex I to these Regulation so as to be visible at the following minimum ranges:
(a) In vessels of 50 metres or more in length:
- a masthead light, 6 miles;
- a sidelight, 3 miles;
- a sternlight, 3 miles;
- a towing light, 3 miles;
- a white, red, green or yellow all-round light, 3 miles.
(b) In vessels of 12 metres or more in length but less than 50 m in length:
- a masthead light, 5 miles; except that where the length of the vessel is less than
20 meters, 3 miles;
- a sidelight, 2 miles;
- a sternlight, 2 miles;
- a towing light, 2 miles;
- a white, red, green or yellow all-round light, 2 miles.
(c) In vessels of less than 12 metres in length:
- a masthead light, 2 miles,
- a sidelight, 1 mile,
- a sternlight, 2 miles,
- a towing light, 2 miles;
- a white, red, green or yellow all-round light, 2 miles.
(d) In inconspicuous, partly submerged vessels or objects being towed; a white allround light, 3 miles.
'''

class Rule22(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule22()


