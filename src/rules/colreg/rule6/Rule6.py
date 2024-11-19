#!/usr/bin/python
# Filename: Rule6.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG

'''
Safe Speed
Every vessel shall at all times proceed at a safe speed so that she can take proper and effective action
to avoid collision and be stopped within a distance appropriate to the prevailing circumstances and
conditions. In determining a safe speed the following factors shall be among those taken into
account:
(a) By all vessels:
(i) the state of visibility;
(ii) the traffic density including concentrations of fishing vessels or any other vessels;
(iii) the manoeuvrability of the vessel with special reference to stopping distance and turning
ability in the prevailing conditions;
(iv) at night the presence of background light such as from shore lights or from back scatter
of her own lights;
(v) the state of wind, sea and current, and the proximity of navigational hazards;
(vi) the draught in relation to the available depth of water.
(b) Additionally, by vessels with operational radar:
(i) the characteristics, efficiency and limitations of the radar equipment;
(ii) any constraints imposed by the radar range scale in use;
(iii) the effect on radar detection of the sea state, weather and other sources of interference;
(iv) the possibility that small vessels, ice and other floating objects may not be detected by
radar at an adequate range;
(v) the number, location and movement of vessels detected by radar;
(vi) the more exact assessment of the visibility that may be possible when radar is used to
determine the range of vessels or other objects in the vicinity.
'''

class Rule6(COLREG):
	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)
		return



if __name__ == "__main__":
	test = Rule6()


