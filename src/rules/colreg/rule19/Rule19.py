#!/usr/bin/python
# Filename: Rule19.py
# Description: Implementation of COLREG Rule

from maritime.model.rule.COLREG import COLREG
from maritime.model.rule.EncounterWatch import EncounterWatch
from maritime.regulation.colreg.Classification import bearing
from cos.model.rule.Situation import Situation
from cos.core.kernel.Context import Context
from cos.core.utilities.ArgList import ArgList

import numpy as np

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

METRES_PER_NM	= 1852.0

class Rule19(COLREG):
	RANGE	= 4000.0	# Metres within which an onset is recorded (evaluator.yaml r_colregs_2_max)
	DCPA	= 500.0		# Metres of predicted passing distance that is a risk of collision

	def __init__(self):
		""" Constructor
		"""
		COLREG.__init__(self)

		self.visibility	= None		# Scenario visibility in nautical miles, read from the resolver each pass

		# Every encounter at risk (19(e)), with own ship's speed and the target's bearing at onset
		self.watch	= EncounterWatch( None, self.DCPA, self.RANGE, snapshot=self.snapshot )
		return

	def setup(self, ctxt:Context, config:ArgList):
		""" Sets up the rule and its encounter thresholds
		Arguments
			ctxt -- Simulation context
			config -- Configuration attributes
		"""
		COLREG.setup( self, ctxt, config )

		self.watch.dcpa		= float( config['encounter.dcpa'] or self.DCPA )
		self.watch.range	= float( config['encounter.range'] or self.RANGE )
		return

	def feed(self, ctxt:Context, rule_ctxt):
		""" Adds every vessel under test alone (19(b)), and encounters at risk once past their closest approach (19(e))
		Arguments
			ctxt -- Simulation context
			rule_ctxt -- Rule context
		"""
		target			= rule_ctxt.resolver.get( 'target' ) if rule_ctxt.resolver is not None else None
		self.visibility	= getattr( target, 'visibility', None )

		vessels		= rule_ctxt.vessels or []
		for own in getattr( rule_ctxt, 'subjects', None ) or vessels:
			self.add_situation( Situation(own, None) )

		self.watch.observe( ctxt, rule_ctxt, self )
		return

	def snapshot(self, own, target)->dict:
		""" Own ship's speed, and whether the target was forward of her beam and in sight, at the onset of an encounter
		Arguments
			own -- Own ship
			target -- Target ship
		"""
		d		= (np.asarray( target.location, dtype=float ) - np.asarray( own.location, dtype=float ))[:2]
		sight	= None if self.visibility is None else bool( np.linalg.norm(d) <= self.visibility*METRES_PER_NM )
		return { 'speed':	float( np.linalg.norm(np.asarray(own.velocity, dtype=float)[:2]) ),
				 'forward':	abs( bearing(own, target) ) < 90.0,
				 'in_sight':	sight }

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


