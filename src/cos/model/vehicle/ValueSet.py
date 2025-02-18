#!/usr/bin/python
# Filename: ValueSet.py
# Description: Implement the ValueSet collection

from cos.core.utilities.PropertySet import StringSet

class ValueSet(StringSet):
	def __init__(self):
		StringSet.__init__(self)
		return

	def set(self, value):
		return self.add(value)

	def reset(self, value):
		return self.delete(value)

	# Legata operators
	def SET(self, value):
		return self.set(value)

	def UNSET(self, value):
		return self.reset(value)

	def CLEAR(self, value):
		return self.clear()

	def ADD(self, value):
		return self.set(value)
		
	def DEL(self, value):
		return self.reset(value)

	def HAS(self, value):
		return self.has(value)
	
	def IN(self, values):
		return self.contains(values)

	def NOT_IN(self, values):
		return False if self.contains(values) else True

	def IS(self, values):
		return self.matches(values)

if __name__ == "__main__":
	test = ValueSet()

