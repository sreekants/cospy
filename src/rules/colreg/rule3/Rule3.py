#!/usr/bin/python
# Filename: Rule3.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from cos.core.kernel.Context import Context
from maritime.conduct.grounding.Grounding import Event

'''
General Definitions
(A amended paragraph (a) and a new paragraph (m) shall enter into
force on 29 November 2003, as amended by Resolution A.919(22))
For the purpose of these Rules, except where the context otherwise requires:
(a) The word 'vessel includes every description of water craft, including nondisplacement craft, WIG craft and seaplanes, used or capable of being used as a
means of transportation on water'.
(b) The term 'power-driven vessel' means any vessel propelled by machinery.
(c) The term 'sailing vessel' means any vessel under sail pcosided that propelling
machinery, if fitted, is not being used.
(d) The term 'vessel engaged in fishing' means any vessel fishing with nets, lines,
trawls or other fishing apparatus which restrict manoeuvrability, but does not include
a vessel fishing with trolling lines or other fishing apparatus which do not restrict
manoeuvrability.
(e) The word 'seaplane' includes any aircraft designed to manoeuvre on the water.
(f) The term 'vessel not under command' means a vessel which through some
exceptional circumstance is unable to manoeuvre as required by these Rules and is
therefore unable to keep out of the way of another vessel.
(g) The term 'vessel restricted in her ability to manoeuvre' means a vessel which from
the nature of her work is restricted in her ability to manoeuvre as required by these
Rules and therefore is unable to keep out of the way of another vessel.
The term 'vessels restricted in their ability to manoeuvre' shall include but not be
limited to;
(i) a vessel engaged in laying, servicing or picking up a navigation mark,
submarine cable or pipeline;
(ii) a vessel engaged in dredging, surveying or underwater operations;
(iii) a vessel engaged in replenishment or transferring persons, pcosisions or
cargo while underway;
(iv) a vessel engaged in the launching or recovery of aircraft;
(v) a vessel engaged in mineclearance operations;
(vi) a vessel engaged in a towing operation such as severely restricts the towing
vessel and her tow in their ability to deviate from their course.
(h) The term 'vessel constrained by her draught' means a power-driven vessel which
because of her draught in relation to the available depth and width of navigable water,
is severely restricted in her ability to deviate from the course she is following.
(i) The word 'underway' means that a vessel is not at anchor, or made fast to the
shore, or aground.
(j) The words 'length' and 'breadth' of a vessel mean her length overall and greatest
breadth.
(k) Vessels shall be deemed to be in sight of one another only when one can be
observed visually from the other.
(l) The term 'restricted visibility' means any condition in which visibility is restricted by
fog, mist, falling snow, heavy rainstorms, sandstorms or any other similar causes.
(m) The term 'Wing-In-Ground (WIG) craft' means a multimodal craft which, in its
main operational mode, flies in close proximity to the surface by utilizing surfaceeffect action.
'''

class Rule3(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return

	def on_start(self, ctxt:Context, config):
		""" Callback for simulation startup
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		COLREG.on_start(self, ctxt, config)

		self.subscribe("vessel.aground", self.on_aground)
		return

	def on_aground(self, ctxt:Context, evt:Event):
		""" Event handler for aground
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		print( f'{self.__class__.__name__}.aground:{evt.vessel.config["name"]} at {evt.seabed.config["name"]} ' )
		return


if __name__ == "__main__":
	test = Rule3()


