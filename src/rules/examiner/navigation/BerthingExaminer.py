#!/usr/bin/python
# Filename: BerthingExaminer.py
# Description: Implementation of the BerthingExaminer class

from rules.examiner.navigation.GroundingExaminer import GroundingExaminer
from cos.core.kernel.Context import Context

# REQUIREMENT:
# Berthing: the inland counterpart of grounding. A vessel in internal waters,
# a harbour or a waterway that stands closer to the shore than its draught
# allows has berthed, whether or not it meant to.
#
# The arithmetic is identical to GroundingExaminer's, so this subclasses it and
# changes only which zone types it answers for, which margin it reads, and
# which events it scores - all four of which are names looked up in
# config/examiner/zones.yaml. Sharing the computation keeps the two concerns
# from drifting apart as the depth model improves.



class BerthingExaminer(GroundingExaminer):
	TOPIC		= '/Faculty/Concern/Berthing'
	MESSAGE		= 'vessel.berthing'
	ZONES		= 'berthing_zones'
	MARGIN		= 'berthing_margin'
	CONTACT		= 'berthing.contact'
	NEAR_MISS	= 'berthing.margin'

	def __init__(self):
		""" Constructor
		"""
		GroundingExaminer.__init__(self)
		return

	# No method overrides are needed. The inherited scorer reads self.TOPIC,
	# self.MESSAGE, self.ZONES, self.MARGIN, self.CONTACT and self.NEAR_MISS,
	# so redeclaring those six names above is the whole of the difference
	# between berthing and grounding.


if __name__ == "__main__":
	test = BerthingExaminer()
