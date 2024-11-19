#!/usr/bin/python
# Filename: Rule35.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Sound Signals in restricted Visibility
(A new paragraph (i) shall enter into force on 29 November 2003,
as amended by Resolution A.919(22))
In or near an area of restricted visibility, whether by day or night, the signals
prescribed in this Rule shall be used as follows:
(a) A power-driven vessel making way through the water shall sound at intervals of
not more than 2 minutes one prolonged blast.
(b) A power-driven vessel underway but stopped and making no way through the
water shall sound at intervals of not more than 2 minutes two prolonged blasts in
succession with an interval of about 2 seconds between them.
(c) A vessel not under command, a vessel restricted in her ability to manoeuvre, a
vessel constrained by her draught, a sailing vessel, a vessel engaged in fishing and a
vessel engaged in towing or pushing another vessel shall, instead of the signals
prescribed in paragraphs (a) or (b) of this Rule sound at intervals of not more than 2
minutes three blasts in succession, namely one prolonged followed by two short
blasts.
(d) A vessel engaged in fishing, when at anchor, and a vessel restricted in her ability
to manoeuvre when carrying out her work at anchor, shall instead of the signals
prescribed in paragraph (g) of this Rule sound the signal prescribed in paragraph (c)
of this COLREG.
(e) A vessel towed or if more than one vessel is towed the last vessel of the tow, if
manned, shall at intervals of not more than 2 minutes sound four blasts in succession,
namely one prolonged followed by three short blasts. When practicable, this signal
shall be made immediately after the signal made by the towing vessel.
(f) When a pushing vessel and a vessel being pushed ahead are rigidly connected in a
composite unit they shall be regarded as a power-driven vessel and shall give the
signals prescribed in paragraphs (a) or (b) of this COLREG.
(g) A vessel at anchor shall at intervals of not more than one minute ring the bell
rapidly for about 5 seconds. In a vessel of 100 metres or more in length the bell shall
be sounded in the forepart of the vessel and immediately after the ringing of the bell
the gong shall be sounded rapidly for about 5 seconds in the after part of the vessel. A
vessel at anchor may in addition sound three blasts in succession, namely one short,
one prolonged and one short blast, to give warning of her position and of the
possibility of collision to an approaching vessel.
(h) A vessel aground shall give the bell signal and if required the gone signal
prescribed in paragraph (g) of this Rule and shall, in addition, give three separate and
distinct strokes on the bell immediately before and after the rapid ringing of the bell. A
vessel aground may in addition sound an appropriate whistle signal.
(i) A vessel of 12 metres or more but less than 20 metres in length shall not be
obliged to give the bell signals prescribed in paragraphs (g) and (h) of this COLREG.
However, if she does not, she shall make some other efficient sound signal at intervals
of not more than 2 minutes.
(j) A vessel of less than 12 metres in length shall not be obliged to give the abovementioned signals but, if she does not, shall make some other efficient sound signal at
intervals of not more than 2 minutes.
(k) A pilot vessel when engaged on pilotage duty may in addition to the signals
prescribed in paragraphs (a), (b) or (g) of this Rule sound an identity signal consisting
of four short blasts.
'''

class Rule35(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule35()


