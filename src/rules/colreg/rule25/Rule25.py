#!/usr/bin/python
# Filename: Rule25.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Sailing Vessels underway and Vessels under Oars
(a) A sailing vessel underway shall exhibit:
(i) sidelights;
(ii) a sternlight.
(b) In a sailing vessel of less than 20 metres in length the lights prescribed in
paragraph (a) of this Rule may be combined in one lantern carried at or near the top
of the mast where it can best be seen.
(c) A sailing vessel underway may, in addition to the lights prescribed in paragraph
(a) of this Rule, exhibit at or near the top of the mast, where they can best be seen,
two all-round lights in a vertical line, the upper being red and the lower green, but
these lights shall not be exhibited in conjunction with the combined lantern permitted
by paragraph (b) of this COLREG.
(d)
(i) A sailing vessel of less than 7 metres in length shall, if practicable, exhibit the
lights prescribed in paragraph (a) or (b) of this Rule, but if she does not, she
shall have ready at hand an electric torch or lighted lantern showing a white
light which shall be exhibited in sufficient time to prevent collision.
(ii) A vessel under oars may exhibit the lights prescribed in this Rule for sailing
vessels, but if she does not, she shall have ready at hand an electric torch or
lighted lantern showing a white light which shall be exhibited in sufficient time
to prevent collision.
(e) A vessel proceeding under sail when also being propelled by machinery shall
exhibit forward where it can best be seen a conical shape, apex down wards.
'''

class Rule25(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule25()


