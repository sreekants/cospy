#!/usr/bin/python
# Filename: Rule1.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Application
(a) These Rules shall apply to all vessels upon the high seas and in all waters
connected therewith navigable by seagoing vessels.
(b) Nothing in these Rules shall interfere with the operation of special rules made by
an appropriate authority for roadsteads, harbours, rivers, lakes or inland waterways
connected with the high seas and navigable by seagoing vessels. Such special rules
shall conform as closely as possible to these Rules.
(c) Nothing in these Rules shall interfere with the operation of any special rules made
by the Government of any State with respect to additional station or signal lights,
shapes or whistle signals for ships of war and vessels proceeding under convoy, or
with respect to additional station or signal lights or shapes for fishing vessels engaged
in fishing as a fleet. These additional station or signal lights, shapes or whistle signals
shall, so far as possible, be such that they cannot be mistaken for any light, shapes or
signal authorized elsewhere under these Rules.
(d) Traffic separation schemes may be adopted by the Organization for the purpose of
these Rules.
(e) Whenever the Government concerned shall have determined that a vessel of
special construction or purpose cannot comply fully with the pcosisions of any of these
Rules with respect to the number, position, range or arc of visibility of lights or
shapes, as well as to the disposition and characteristics of sound-signalling appliances,
such vessel shall comply with such other pcosisions in regard to the number, position,
range or arc of visibility of lights or shapes, as well as to the disposition and
characteristics of sound-signalling appliances, as her Government shall have
determined to be the closest possible compliance with these Rules in respect to that
vessel. MSC/Circ.1144
'''

class Rule1(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule1()


