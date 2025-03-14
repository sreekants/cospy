#!/usr/bin/python
# Filename: Rule18.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Responsibilities between Vessels
(The new paragraph (f) shall enter into force on 29 November 2003, as
amended by Resolution A.919(22))
Except where Rules 9, 10 and 13 otherwise require:
(a) A power-driven vessel underway shall keep out of the way of:
(i) a vessel not under command;
(ii) a vessel restricted in her ability to manoeuvre;
(iii) a vessel engaged in fishing;
(iv) a sailing vessel.
(b) A sailing vessel underway shall keep out of the way of:
(i) a vessel not under command;
(ii) a vessel restricted in her ability to manoeuvre;
(iii) a vessel engaged in fishing.
(c) A vessel engaged in fishing when underway shall, so far as possible, keep out of the way
of:
(i) a vessel not under command;
(ii) a vessel restricted in her ability to manoeuvre.
(d)
(i) Any vessel other than a vessel not under command or a vessel restricted in her ability to
manoeuvre shall, if the circumstances of the case admit, avoid impeding the safe
passage of a vessel constrained by her draught, exhibiting the signals in Rule 28.
(ii) A vessel constrained by her draught shall navigate with particular caution having full
regard to her special condition.
(e) A seaplane on the water shall, in general, keep well clear of all vessels and avoid impeding their
navigation. In circumstances, however, where risk of collision exists, she shall comply with the Rules
of this Part.
(f)
(i) A WIG craft shall, when taking off, landing and in flight near the surface, keep well clear of
all other vessels and avoid impeding their navigation;
(ii) a WIG craft operating on the water surface shall comply with the Rules of this Part as a
power-driven vessel.
'''

class Rule18(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule18()


