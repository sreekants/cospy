#!/usr/bin/python
# Filename: Request.py
# Description: Implementation of the Request class

from cos.core.utilities.ArgList import ArgList
import json

class Request:
	def __init__(self):
		self.instance 	= None
		self.method 	= None
		self.args 		= None
		return

	def parse(self, body:str):
		""" Convert a string to a request object
		Arguments
			body -- String representation of the request
		"""

		# Unmarshall the argument
		if body.startswith('{') and body.endswith('}'):
			bodyinfo	= json.loads( body )
			items		= bodyinfo.items()
		else:
			bodyinfo	= ArgList(body, '=', ',')
			items		= bodyinfo.arglist.items()

		self.instance	= bodyinfo['o']
		self.method 	= bodyinfo['m']
		self.args		= dict()

		for k, v in items:
			if k not in ['o', 'm']:
				self.args[k]	= v

		return


if __name__ == "__main__":
	test = Request()

