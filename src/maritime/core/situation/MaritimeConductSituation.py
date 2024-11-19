#!/usr/bin/python
# Filename: MaritimeConductSituation.py
# Description: Enumerations and states of encounter situations that occur in shipping

from maritime.core.situation.MaritimeSituation import MaritimeSituation
from cos.model.situation.EncounterSituation import *


class MaritimeConductSituation(MaritimeSituation):
	def __init__(self):
		""" Constructor
		"""
		MaritimeSituation.__init__(self, 'Conduct')
		return


if __name__ == "__main__":
	test = MaritimeConductSituation()


