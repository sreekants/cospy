#!/usr/bin/python
# Filename: ArgList.py
# Description: Implementation of a name value argument list class

class ArgList:
	def __init__(self, args=None, vsep='=', sep=' '):
		""" Constructor
		Arguments
			args -- List of arguments
		"""
		if args is None or len(args)==0:
			self.arglist 	= dict()
		else:
			self.arglist 	= dict( item.split(vsep) for item in args.split(sep) )
		return

	def IsTrue(self, key:str):
		""" Checks if an argument is true
		Arguments
			key -- Key identifier
		"""
		value	= self.arglist.get(key, 'false')
		if value.lower()=='true' or value=='1':
			return True

		return False

	def IsFalse(self, key:str):
		""" Checks if an argument is false
		Arguments
			key -- Key identifier
		"""
		value	= self.arglist.get(key, 'true')
		if value.lower()=='false' or value=='0':
			return True

		return False

	def ToFloat(self, key:str, default=0.0):
		""" Checks if an argument is false
		Arguments
			key -- Key identifier
		"""
		value	= self.arglist.get(key, None)
		if value is None:
			return default

		return float(value)

	def __len__(self):
		""" Returns number of items in the clas
		"""
		return len(self.arglist)

	def __getitem__(self, key:str):
		""" Returns an item with a key name in the list
		Arguments
			key -- Name of the key to search for
		"""
		return self.arglist.get(key, None)

	def __contains__(self, key):
		""" Check if a key is in the arglist """
		return key in self.arglist

if __name__ == "__main__":
	test = ArgList("Name1=Value1 Name2=False Name3=True Name4=0 Name5=1")
	print(test["Name2"])
	if "Name1" in test:
		print( 'has Name1')

	print( test.IsTrue('Name2') )
	print( test.IsTrue('Name3') )
	print( test.IsTrue('Name4') )
	print( test.IsTrue('Name5') )
	print( test.IsTrue('Undefined') )

	print( test.IsFalse('Name2') )
	print( test.IsFalse('Name3') )
	print( test.IsFalse('Name4') )
	print( test.IsFalse('Name5') )
	print( test.IsTrue('Undefined') )

