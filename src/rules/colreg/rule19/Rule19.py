#!/usr/bin/python
# Filename: Rule19.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from cos.core.kernel.Context import Context

'''
Conduct of Vessels in Restricted Visibility
(a) This Rule applies to vessels not in sight of one another when navigating in or near an area of
restricted visibility.
(b) Every vessel shall proceed at a safe speed adapted to the prevailing circumstances and conditions
of restricted visibility. A power-driven vessel shall have engines ready for immediate manoeuvre.
(c) Every vessel shall have due regard to the prevailing circumstances and conditions of restricted
visibility when complying with the Rules of Section I of this Part.
(d) A vessel which detects by radar alone the presence of another vessel shall determine if a closequarters situation is developing and/or risk of collision exists. If so, she shall take avoiding action in
ample time, pcosided that when such action consists of an alteration of course, so far as possible the
following shall be avoided:
(i) an alteration of course to port for a vessel forward of the beam, other than for a vessel
being overtaken;
(ii) an alteration of course towards a vessel abeam or abaft the beam.
(e) Except where it has been determined that a risk of collision does not exist, every vessel which
hears apparently forward of her beam the fog signal of another vessel, or which cannot avoid a close
quarters situation with another vessel forward of her beam, shall reduce her speed to the minimum
at which she can be kept on her course. She shall if necessary take all her way off and in any event
navigate with extreme caution until danger of collision is over.
'''

class Rule19(COLREG):
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

		self.subscribe("vessel.overtaken", self.on_overtaken)
		return

	def on_overtaken(self, ctxt:Context, evt):
		""" Event handler for overtaken
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		vessel	= evt[1]
		print( f'{self.__class__.__name__}.overtaken:{vessel.config["name"]}' )
		return


if __name__ == "__main__":
	test = Rule19()


