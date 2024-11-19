#!/usr/bin/python
# Filename: Rule9.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from cos.core.kernel.Context import Context

'''
Narrow Channels
(a) A vessel proceeding along the course of a narrow channel or fairway shall keep as near to the
outer limit of the channel or fairway which lies on her starboard side as is safe and practicable.
(b) A vessel of less than 20 metres in length or a sailing vessel shall not impede the passage of a
vessel which can safely navigate only within a narrow channel or fairway.
(c) A vessel engaged in fishing shall not impede the passage of any other vessel navigating within a
narrow channel or fairway.
(d) A vessel shall not cross a narrow channel or fairway if such crossing impedes the passage of a
vessel which can safely navigate only within such channel or fairway. The latter vessel may use the
sound signal prescribed in Rule 34(d) if in doubt as to the intention of the crossing vessel.
(e)
(i) In a narrow channel or fairway when overtaking can take place only if the vessel to be
overtaken has to take action to permit safe passing, the vessel intending to overtake
shall indicate her intention by sounding the appropriate signal prescribed in Rule
34(c)(i). The vessel to be overtaken shall, if in agreement, sound the appropriate signal
prescribed in Rule 34(c)(ii) and take steps to permit safe passing. If in doubt she may
sound the signals prescribed in Rule 34(d).
(ii) This Rule does not relieve the overtaking vessel of her obligation under Rule 13.
(f) A vessel nearing a bend or an area of a narrow channel or fairway where other vessels
may be obscured by an intervening obstruction shall navigate with particular alertness
and caution and shall sound the appropriate signal prescribed in Rule 34(e).
(g) Any vessel shall, if the circumstances of the case admit, avoid anchoring in a narrow channel.
'''

class Rule9(COLREG):
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
		self.subscribe("vessel.overtaking", self.on_overtaking)
		self.subscribe("vessel.crossing", self.on_crossing)
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

	def on_overtaking(self, ctxt:Context, evt):
		""" Event handler for overtaking
		Arguments
			ctxt -- Simulation context
			evt -- Event data
		"""
		vessel	= evt[1]
		print( f'{self.__class__.__name__}.overtaking:{vessel.config["name"]}' )
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
	test = Rule9()


