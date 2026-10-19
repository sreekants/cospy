#!/usr/bin/python
# Filename: BerthingExaminer.py
# Description: Implementation of the BerthingExaminer class

from rules.examiner.navigation.GroundingExaminer import GroundingExaminer
from cos.model.examiner.Examination import ExaminationType
from cos.core.kernel.Context import Context

# REQUIREMENT:
# Berthing: seabed contact while berthing, i.e. at or below berthing_speed
# within berthing_distance of land (config/examiner/zones.yaml), in any zone.
# Every other contact is a grounding (COS.049).
#
# The arithmetic is identical to GroundingExaminer's, so this subclasses it and
# changes only which situation it answers for and which events it scores.



class BerthingExaminer(GroundingExaminer):
	EXAMINES	= ExaminationType.BERTHING
	TOPIC		= '/Faculty/Concern/Berthing'
	MESSAGE		= 'vessel.berthing'
	ZONES		= 'berthing_zones'
	MARGIN		= 'berthing_margin'
	CONTACT		= 'berthing.contact'
	NEAR_MISS	= 'berthing.margin'
	BERTHING	= True

	def __init__(self):
		""" Constructor
		"""
		GroundingExaminer.__init__(self)
		return

	# No method overrides are needed: the inherited scorer reads the names above.


if __name__ == "__main__":
	test = BerthingExaminer()
