#!/usr/bin/python
# Filename: Rule20.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Application
(a) Rules in this Part shall be complied with in all weathers.
(b) The Rules concerning lights shall be complied with from sunset to sunrise, and
during such times no other lights shall be exhibited, except such lights as cannot be
mistaken for the lights specified in these Rules or do not impair their visibility or
distinctive character, or interfere with the keeping of a proper look-out.
(c) The lights prescribed by these Rules shall, if carried, also be exhibited from sunrise
to sunset in restricted visibility and may be exhibited in all other circumstances when
it is deemed necessary.
(d) The Rules concerning shapes shall be complied with by day.
(e) The lights and shapes specified in these Rules shall comply with the pcosisions of
Annex I to these Regulations.
'''
class Rule20(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule20()

