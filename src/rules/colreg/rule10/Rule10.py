#!/usr/bin/python
# Filename: Rule10.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from cos.core.kernel.Context import Context

'''
Traffic Separation Schemes
(a) This Rule Applies to traffic separation schemes adopted by the Organization and does not relieve
any vessel of her obligation under any other rule.
(b) A vessel using a traffic separation scheme shall:
(i) proceed in the appropriate traffic lane in the general direction of traffic flow for that
lane;
(ii) so far as practicable keep clear of a traffic separation line or separation zone;
(iii) normally join or leave a traffic lane at the termination of the lane, but when joining or
leaving from either side shall do so at as small an angle to the general direction of traffic
flow as practicable.
(c) A vessel shall so far as practicable avoid crossing traffic lanes, but if obliged to do so shall cross on
a heading as nearly as practicable at right angles to the general direction of traffic flow.
(d)
(i) A vessel shall not use an inshore traffic zone when she can safely use the appropriate
traffic lane within the adjacent traffic separation scheme. However, vessels of less than 20
meters in length, sailing vessels and vessels engaged in fishing may use the inshore traffic
zone.
(ii) Notwithstanding subparagraph (d) (i), a vessel may use an inshore traffic zone when en
route to or from a port, offshore installation or structure, pilot station or any other place
situated within the inshore traffic zone, or to avoid immediate danger.
(e) A vessel, other than a crossing vessel, or a vessel joining or leaving a lane shall not normally enter
a separation zone or cross a separation line except:
(i) in cases of emergency to avoid immediate danger;
(ii) to engage in fishing within a separation zone.
(f) A vessel navigating in areas near the terminations of traffic separation schemes shall do so with
particular caution.
(g) A vessel shall so far as practicable avoid anchoring in a traffic separation scheme or in areas near
its terminations.
(h) A vessel not using a traffic separation scheme shall avoid it by as wide a margin as is practicable.
(i) A vessel engaged in fishing shall not impede the passage of any vessel following a traffic lane.
(j) A vessel of less than 20 meters in length or a sailing vessel shall not impede the safe passage of a
power-driven vessel following a traffic lane.
(k) A vessel restricted in her ability to manoeuvre when engaged in an operation for the maintenance
of safety of navigation in a traffic separation scheme is exempted from complying with this Rule to
the extent necessary to carry out the operation.
(l) A vessel restricted in her ability to manoeuvre when engaged in an operation for the laying,
servicing or picking up of a submarine cable, within a traffic separation scheme, is exempted from
complying with this Rule to the extent necessary to carry out the operation.
'''

class Rule10(COLREG):
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
	test = Rule10()


