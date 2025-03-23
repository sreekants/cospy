#!/usr/bin/python
# Filename: States.py
# Description: Finite states function

import json

class States:
	def __init__(self):
		self.reset_on_read	= True
		self.is_static		= True
		self.use_data		= False
		self.states			= dict()
		self.default		= None

		self.is_float		= False
		self.is_integer		= False
		return

	def load(self, path):
		with open(path, 'rt') as f:
			data 		= json.loads(f.read())
			for k, v in data['Properties'].items():
				self.states[v['Input']] = {
					'name': k, 
					'output': v['Output']
				}

			self.default	= v.get('Default', None)
		return

	def __call__(self, x):
		outstate	= self.states.get(x, None)
		if outstate is None:
			return self.default
		
		if self.is_float == True:
			return float(outstate['output'])

		if self.is_integer == True:
			return int(outstate['output'])

		return outstate['output']

	

if __name__ == "__main__":
	test = States()
	test.load('device.json')
	print(test('A*'))


