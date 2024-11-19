#!/usr/bin/python
# Filename: Rule15.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from cos.core.kernel.Context import Context

'''
Crossing Situation
When two power-driven vessels are crossing so as to involve risk of collision, the vessel which has the
other on her own starboard side shall keep out of the way and shall, if the circumstances of the case
admit, avoid crossing ahead of the other vessel.
'''

class Rule15(COLREG):
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

		self.subscribe("vessel.crossing", self.on_crossing)
		return

	def on_crossing(self, ctxt:Context, evt):
		""" Event handler for crossing
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		vessel	= evt[1]
		print( f'{self.__class__.__name__}.crossing:{vessel.config["name"]}' )
		return


if __name__ == "__main__":
	test = Rule15()


