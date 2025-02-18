#!/usr/bin/python
# Filename: PropertySet.py
# Description: A collection of propeerties

import fnmatch

class PropertySet(list):
	def __init__(self):
		list.__init__(self)
		return

	def add(self, value):
		if value not in self:
			self.append(value)
		return
		
	def remove(self, value):
		if value in self:
			self.remove(value)
		return

	def has(self, value):
		return True if value in self else False
	
	def contains(self, values):
		for v in values:
			if v in self:
				return True
			
		return False

	def matches(self, values):
		for v in values:
			if v not in self:
				return False
			
		return True


class StringSet(list):
	def __init__(self):
		list.__init__(self)
		return

	def add(self, value):
		if value not in self:
			self.append(value)
		return
		
	def delete(self, value):
		if value in self:
			self.remove(value)
		return

	def has(self, value):
		return True if value in self else False
	
	def contains(self, values):
		for v in values:
			if self.find(v) == True:
				return True
			
		return False

	def matches(self, values):
		for v in values:
			if self.find(v) == False:
				return False
			
		return True


	def find(self, spec):
		for v in self:
			if fnmatch.fnmatch(v, spec):
				return True
			
		return False

if __name__ == "__main__":
	test = PropertySet()

