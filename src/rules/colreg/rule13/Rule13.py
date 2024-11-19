#!/usr/bin/python
# Filename: Rule13.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from cos.core.kernel.Context import Context
from cos.model.rule.Situation import Situation

'''
Overtaking
(a) Notwithstanding anything contained in the Rules of Part B, Sections I and II any vessel overtaking
any other shall keep out of the way of the vessel being overtaken.
(b) A vessel shall be deemed to be overtaking when coming up with another vessel from a direction
more than 22.5 degrees abaft her beam, that is, in such a position with reference to the vessel she is
overtaking, that at night she would be able to see only the sternlight of that vessel but neither of her
sidelights.
(c) When a vessel is in any doubt as to whether she is overtaking another, she shall assume that this
is the case and act accordingly.
(d) Any subsequent alteration of the bearing between the two vessels shall not make the overtaking
vessel a crossing vessel within the meaning of these Rules or relieve her of the duty of keeping clear
of the overtaken vessel until she is finally past and clear.
'''

class Rule13(COLREG):
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

		self.subscribe("vessel.overtaking", self.on_overtaking)
		self.subscribe("vessel.crossing", self.on_crossing)
		self.subscribe("vessel.approach", self.on_close_encounter)
		return

	def on_overtaking(self, ctxt:Context, evt):
		""" Event handler for overtaking
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		OS		= evt[1]
		TS		= evt[2]
		print( f'{self.__class__.__name__}.overtaking:{OS.config["name"]}' )
		return

	def on_crossing(self, ctxt:Context, evt):
		""" Event handler for crossing
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		OS		= evt[1]
		TS		= evt[2]
		print( f'{self.__class__.__name__}.crossing:{OS.config["name"]}' )
		return

	def on_close_encounter(self, ctxt:Context, evt):
		""" Event handler for close encounters
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		OS			= evt[1]
		TS			= evt[2]
		distance	= evt[3]
		self.add_situation( Situation(OS, TS) )
		print( f'{self.__class__.__name__}.close_encounter:{OS.config["name"]}' )
		return

if __name__ == "__main__":
	test = Rule13()


