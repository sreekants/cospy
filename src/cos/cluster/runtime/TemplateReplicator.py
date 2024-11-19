#!/usr/bin/python
# Filename: TemplateReplicator.py
# Description: Helper class to generate code from a meta-programming template

import os, shutil

class Declarations:
	def __init__(self, defaults=None):
		""" Constructor
		"""
		self.values	= {}

		if defaults != None:
			for k, v in defaults.items():
				self.set(k, v)
		return

	def replace_text( self, text ):
		""" Replace all meta tags in a text and returns the processed text
		Arguments
			text -- text to process
		"""
		for k, v in self.values.items():
			text	= text.replace( k, v )
			text	= self.__do_replace_text( text, k, k.upper(), v )
			text	= self.__do_replace_text( text, k, k.lower(), v )

		return text


	def set( self, key, value ):
		""" Sets a meta tag value
		Arguments
			key -- Name of meta-tag
			value -- value of the meta-tag
		"""
		if key == 'model':
			self.values['$$original_model$$']	= value

		self.values['$${}$$'.format(key)]	= value
		return

	def has_tag( self, key ):
		""" Sets a meta tag value
		Arguments
			key -- Name of meta-tag
		"""
		return self.values.has_key('$${}$$'.format(key))

	def __setitem__( self, key, value ):
		""" Sets a meta tag value
		Arguments
			key -- Name of meta-tag
			value -- value of the meta-tag
		"""
		self.set( key, value )
		return

	# Private functions
	def __do_replace_text( self, text:str, origkey:str, key:str, value:str ):
		""" Internal function to replace all tags
		Arguments
			text -- text to process replacement for
			origkey -- Original meta-tag key
			key -- Name of the meta-tag
			value -- value of the meta-tag
		"""
		if origkey != key:
			text	= text.replace( key, value )
		return text

class TemplateReplicator:
	def __init__(self, decls, overwrite=False):
		""" Constructor
		Arguments
			decls -- Variable declarations for the generation
			overwrite	-- Flag to enable overwriting existing file
		"""
		self.declarations	= decls
		self.overwrite		= overwrite
		return


	def replicate( self, templatedir:str, outputdir:str ):
		""" Repliate a template to an output directory from a template directory
		Arguments
			templatedir -- template directory
			outputdir -- Generated output directory
		"""
		for root, dirs, filenames in os.walk(templatedir):
			# Evalute the target directory and create it
			# if it does not exist
			outroot	= os.path.join(outputdir, root[len(templatedir):])
			if os.path.isdir(outroot) == False:
				os.makedirs( outroot )

			for filename in filenames:
				if filename == 'confirm.inf':
					continue

				src		= os.path.join(root, filename)
				dest	= os.path.join(outroot, filename)
				dest	= self.declarations.replace_text( dest )

				if os.path.isfile(dest) == True:
					if self.overwrite == True:
						os.remove(dest)
					else:
						continue

				if self.is_text_file(src) == False:
					self.__copy_file(src, dest, True)
				else:
					self.__compile_file( src, dest )
		return

	def is_text_file(self, path:str)->bool:
		""" Checks if a file extension represents a valid text file
		Arguments
			path -- Path of the file
		"""
		ext = TemplateReplicator.find_extension(path)
		if ext in [
				# Proprietary tools
				"mki",		# Creates a single source file from a codebase

				# Automake project files.
				"am", "ac", "in",

				# Unix configuration files
				"conf",

				# Visual Studio project files.
				"dsp", "dsw", "sln", "vcxproj", "filters", "user", "def",

				# Embedded project files
				"ino",		# Arduino

				# Windows specific files.
				"reg",			# Registry files
				"manifest",		# Manifest files
				"wix",			# Manifest files

				# Code::Blocks project files.
				"cbp", "layout",

				"txt", "java", "h", "c++","cs",
				"cfg", "ini","json","yaml","spec",
				"sql", "dmp", "rc",
				"asm","h","h++", "cpp", "dsp", "dsw", "mak", "hpp", "hxx", "cxx",
				"html", "htm",
				"css", "xsl", "svg", "txt",
				"cfg", "ini", "idl", "wsidl", "prj", "yaml",
				"wsdl", "disco", "soap",
				"tsv", "csv",
				"bat", "sh",
				"js", "vbs", "pl", "py", "rb", "lua", "nut", "erl",
				"scm","ss","tcl","prolog"
			]:
			return True

		return False

	@staticmethod
	def find_extension( path:str ):
		""" Extracts  the file extension from the path
		Arguments
			path -- Path of the file
		"""
		ndx = path.rfind('.')
		if ndx == -1:
			return ""
		return path[ndx+1:]

	# Private function
	def __compile_file( self, src:str, dest:str ):
		""" Compiles a template file and generates an output
		Arguments
			src -- Path to the source file
			dest -- Path to the destination file
		"""

		template	= TemplateReplicator.__read_from_file( src )
		output		= self.declarations.replace_text( template )

		with open(dest, 'w+t') as f:
			f.write(output)

		return

	def __copy_file( self, src:str, dest:str, overwrite=False ):
		""" Copies a file to a new location
		Arguments
			src -- Path of the file
			dest -- Path of the location to copy
			overwrite=False -- Flag to indicate overwriting, if the file already exists
		"""
		if os.path.isfile(dest):
			if overwrite == False:
				return

		return shutil.copyfile( src, dest )

	@staticmethod
	def __read_from_file(path:str):
		""" Reads the text content of a file
		Arguments
			path -- Path of the file
		"""
		if os.path.isfile(path):
			with open(path, 'rt') as f:
				return f.read()

		return ''



if __name__ == "__main__":
	decl = Declarations()
	decl['location']	= 'alesund'

	rep = TemplateReplicator( decl )
	rep.replicate( 'E:\\users\\ntnu\\modcolreg\\config', 'test' )


