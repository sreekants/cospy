#!/usr/bin/python
# Filename: EncounterEvent.py
# Description: Types of maritime events 

class Event:
	def __init__(self, subject, distance):
		""" Constructor
		Arguments
			subject -- Subject of th event
			distance -- Distance of th event
		"""
		self.subject	= subject
		self.distance	= distance
		return

class EncounterEvent(Event):
	def __init__(self, situation, OS, TS, distance, α, β):
		""" Constructor
		Arguments
			situation -- Situation type
			OS -- Reference to own ship
			TS -- Reference to target ship
			distance -- Distance of the ship
			α -- Direction of the target ship from own ship
			β -- Direction of the own ship from target
		"""
		Event.__init__(self, OS, distance)

		self.TS			= TS
		self.distance	= distance
		self.α			= α
		self.β			= β
		return

	@property
	def OS(self):
		""" Returns a reference to the own ship
		"""
		return self.subject

if __name__ == "__main__":
	test = Events()


