#!/usr/bin/python
# Filename: Rule30.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Anchored Vessels and Vessels aground
(a) A vessel at anchor shall exhibit where it can best be seen:
(i) in the fore part, an all-round white light or one ball;
(ii) at or near the stern and at a lower level than the light prescribed in subparagraph (i), an all-round white light
(b) A vessel of less than 50 metres in length may exhibit an all-round white light
where it can best be seen instead of the lights prescribed in paragraph (a) of this
COLREG.
(c) A vessel at anchor may, and a vessel of 100 metres and more in length shall, also
use the available working or equivalent lights to illuminate her decks.
(d) A vessel aground shall exhibit the lights prescribed in paragraph (a) or (b) of this
Rule and in addition, where they can best be seen:
(i) two all-round red lights in a vertical line;
(ii) three balls in a vertical line.
(e) A vessel of less than 7 metres in length, when at anchor, not in or near a narrow
channel, fairway or anchorage, or where other vessels normally navigate, shall not be
required to exhibit the lights or shape prescribed in paragraphs (a), (b) of this COLREG.
(f) A vessel of less than 12 metres in length, when aground, shall not be required to
exhibit the lights or shapes prescribed in sub-paragraphs (d)(i) and (ii) of this COLREG.
'''

class Rule30(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule30()


