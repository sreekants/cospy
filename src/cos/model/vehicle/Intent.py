#!/usr/bin/python
# Filename: Intent.py
# Description: Implement the intent collection

from cos.model.vehicle.ValueSet import ValueSet

class Intent(ValueSet):
	def __init__(self):
		ValueSet.__init__(self)
		return


if __name__ == "__main__":
	test = Intent()

