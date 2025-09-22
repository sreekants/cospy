#!/usr/bin/python
# Filename: RegEval.py
# Description: Implementation of the singleton Regeval application

from cos.model.rule.Automata import Automata

import os, sys, fnmatch

class RegEval:
	def __init__(self, path='.'):
		self.path		= path
		self.file		= None
		self.terms		= set()

		self.config 	= {
				'definitions':True,
				'terms':False,
				'verbose':False
			}

		self.stats		= {
				'rules':0
			}
		
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
				self.compile(count, path)

			self.stats["count"]	= count
			self.postproc()

		except Exception as e:
			print( f'Error {e}' )
			return -1
			
		return 0

	def dump_symbols(self):
		print( f"Symbols ({len(self.terms)})" )
		terms = sorted(self.terms)
		for t in terms:
			print( f'  * {t}' )
		return

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

	def verbose( self, args ):
		self.config["verbose"]	= True
		return

	def verbose( self, args ):
		self.config["terms"]	= True
		return

	def dir( self, args ):
		self.path	= args[0]
		return

	def match( self, args ):
		self.file	= args[0]
		return

	def load( self ):
		files	= []
		for root, dirs, filenames in os.walk(self.path):
			for filename in filenames:
				path = os.path.join(root, filename)
				files.append( (path, filename) )
		return files

	def compile( self, count, path ):
		legata	= Automata(None)

		try:

			# Load and compiled legata file
			legata.load( path )
			result = legata.dump(self.config)

			if self.config.get('verbose', False) is True:
				defs	= result['definitions']
				print( f'===== Processing({count}): {path} =====')
				print( '\n'.join(defs) )

			for term in legata.parser.terms:
				self.terms.add(term)

		except Exception as e:
			location = 'file'
			print( f'{location} {str(e)}')

		return legata

	def postproc( self ):
		try:
			self.print_terms()
			self.print_stats()
		except Exception as e:
			print( f'{str(e)}')
		return

	def print_terms( self ):
		if self.config.get('terms', False) == False:
			return
		
		print( f'===== Terms =====')
		termdict	= {}

		for term in self.terms:
			if term.find('.') == -1:
				continue

			parts 	= term.split('.')
			scope	= parts[0]

			if termdict.get(scope, None) is None:
				termdict[scope]	= set()

			termset	= termdict.get(scope)
			term	= '.'.join(parts[1:])
			termset.add( term )

		scopenames	= list(termdict.keys())
		scopenames.sort()

		for k in scopenames:
			for t in termdict[k]:
				print(f'{k}.{t}')
		return

	def print_stats( self ):
		print( f'===== Summary =====')
		print( f'Directory path:   {self.path}')
		print( f'Files processed:  {self.stats["count"]}')
		return

if __name__ == "__main__":
    test = RegEval('E:\\users\\ntnu\\cospy\\config\\maritime\\regulation\\colreg')
    test.execute()


