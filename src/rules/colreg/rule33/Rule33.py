#!/usr/bin/python
# Filename: Rule33.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Equipment for Sound Signals
(Paragraph (a) shall enter into force on 29 November 2003, as
amended by Resolution A.910(22) )
(a) A vessel of 12 metres or more in length shall be pcosided with a whistle, a vessel
of 20 metres or more in length shall be pcosided with a bell in addition to a whistle,
and a vessel of 100 metres or more in length shall, in addition, be pcosided with a
gong, the tone and sound of which cannot be confused with that of the bell. The
whistle, bell and gong shall comply with the specification in Annex III to these
Regulations. The bell or gong or both may be replaced by other equipment having the
same respective sound characteristics, pcosided that manual sounding of the required
signals shall always be possible.
(b) A vessel of less than 12 metres in length shall not be obliged to carry the sound
signalling appliances prescribed in paragraph (a) of this Rule but if she does not, she
shall be pcosided with some other means of making an efficient sound signal.
'''

class Rule33(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule33()


