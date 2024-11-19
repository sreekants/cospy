#!/usr/bin/python
# Filename: Rule17.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from cos.core.kernel.Context import Context

'''
Action by Stand-on Vessel
(a)
(i) Where one of two vessels is to keep out of the way the other shall keep her course and
speed.
(ii) The latter vessel may however take action to avoid collision by her manoeuvre alone, as
soon as it becomes apparent to her that the vessel required to keep out of the way is
not taking appropriate action in compliance with these Rules.
(b) When, from any cause, the vessel required to keep her course and speed finds herself so close
that collision cannot be avoided by the action of the give-way vessel alone, she shall take such action
as will best aid to avoid collision.
(c) A power-driven vessel which takes action in a crossing situation in accordance with sub-paragraph
(a)(ii) of this Rule to avoid collision with another power-driven vessel shall, if the circumstances of
the case admit, not alter course to port for a vessel on her own port side.
(d) This Rule does not relieve the give-way vessel of her obligation to keep out of the way
'''

class Rule17(COLREG):
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

		self.subscribe("vessel.giveway", self.on_giveway)
		self.subscribe("vessel.standon", self.on_standon)
		self.subscribe("vessel.crossing", self.on_crossing)
		return

	def on_standon(self, ctxt:Context, evt):
		""" Event handler for standon
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		vessel	= evt[1]
		print( f'{self.__class__.__name__}.standon:{vessel.config["name"]}' )

		# Post an event to the scoring table
		self.data(ctxt, 'call', [300, 0, 0])
		return

	def on_giveway(self, ctxt:Context, evt):
		""" Event handler for giveway
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		vessel	= evt[1]
		print( f'{self.__class__.__name__}.giveway:{vessel.config["name"]}' )

		# Post an event to the scoring table
		self.data(ctxt, 'log', [200, 0, 0])
		return

	def on_crossing(self, ctxt:Context, evt):
		""" Event handler for crossing
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		vessel	= evt[1]
		print( f'{self.__class__.__name__}.crossing:{vessel.config["name"]}' )

		# Post an event to the scoring table
		self.data(ctxt, 'log', [200, 0, 0])
		return

if __name__ == "__main__":
	test = Rule17()


