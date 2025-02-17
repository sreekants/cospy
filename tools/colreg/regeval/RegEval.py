#!/usr/bin/python
# Filename: RegEval.py
# Description: Implementation of the singleton Regeval application

from cos.model.rule.Automata import Automata

import os, sys, fnmatch

class RegEval:
	def __init__(self, path='.'):
		self.path	= path
		self.file	= 'Rule*'
		# self.file	= 'debug.legata'
		return

	def run(self, args, appinfo):
		if len(args) > 0:
			if self.configure(args, appinfo) == False:
				return -1

		return self.execute()

	def execute(self):
		try:
			files	= self.load()
			count	= 0
			for f in files:
				path	= f[0]
				file	= f[1]

				# Match files if necessary
				if self.file is not None:
					if fnmatch.fnmatch(file, self.file) == False:
						continue

				count	= count+1
				print( f'===== Processing ({count}): {file} =====')
				self.compile(path)

		except Exception as e:
			print( e )
			return -1
			
		return 0

	def configure(self, args, appinfo):
		next	= 0

		while True:
			if next >= len(args):
				break

			method = args[next]
			if method[0] != '-':
				next = next+1
				continue

			method	= method[1:]

			if hasattr(self, method) and callable(func:=getattr(self, method)):
				try:
					nargs 	= args[next+1:]
					if len(nargs) == 0:
						nargs	= None

					result	= func( nargs )
					if result != None:
						print( result )
						
				except Exception as e:
					print(e)
					return False
				
			next	= next+1
				
		return True

	def evaluate(self):
		print( f"Processing directory: {self.path} ..." )
		return
		
	def dir( self, args ):
		self.path	= args[0]
		return

	def load( self ):
		files	= []
		for root, dirs, filenames in os.walk(self.path):
			for filename in filenames:
				path = os.path.join(root, filename)
				files.append( (path, filename) )
		return files

	def compile( self, path ):
		lagata	= Automata(None)

		# Load and compiled legata file
		lagata.load( path )
		lagata.dump()

		return lagata


if __name__ == "__main__":
    test = RegEval('E:\\users\\ntnu\\cospy\\config\\maritime\\regulation\\colreg')
    test.execute()


