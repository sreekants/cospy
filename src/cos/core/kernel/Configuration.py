#!/usr/bin/python
# Filename: Configuration.py
# Description: Master configuration file for the simulation

from cos.core.kernel.BootImage import FileSystem

import configparser
import os
import re

class Configuration:
	def __init__(self, configfile='cos.ini', configpath='COS_CONFIG', imagefile=None):
		""" Constructor:
		Arguments
			configfile='cos.ini' -- File name of the configuration file
			configpath=None -- Environment variable for the configuration path
			imagefile=None -- Boot image file
		"""
		self.appconfig		= configpath
		self.approot		= 'COS_CONFIG'
		self.inifile		= configfile
		self.config			= None
		self.bootimage		= None

		# Loads the configuration
		self.__load_config( imagefile )

		if self.approot in os.environ.keys():
			self.workspace	= os.environ[self.approot]
		else:
			self.workspace	= '.'

		return

	def __load_config(self, imagefile):
		""" Loads the configuration settings
		Arguments
			imagefile=None -- Boot image file
			variables=None -- Variables to load into the environment
		"""

		if imagefile is not None:
			self.bootimage	= FileSystem( imagefile )
			self.bootimage.mount()

			cfgtxt		= self.bootimage.read_file( f'$FS/{self.inifile}' )
			self.parser = configparser.ConfigParser()
			self.parser.read_string(cfgtxt)
			self.config	= "$FS"
		else:
			# Find the config file in the path if
			# one is not in the current directory
			if self.exists(self.inifile) == False:
				self.inifile = self.find_config_file()

			self.parser = configparser.ConfigParser()
			self.parser.read(self.inifile)

			# Configure the root folder
			self.config	= self.__expand_root_path('Folders','CONFIG')

		self.env	= {}

		self.root	= self.__expand_root_path('Folders','ROOT')
		self.db		= self.__expand_root_path('Folders','DB')
	
		section		= 'EnvironmentVariables'
		variables	= self.get_keys(section)
		for k in variables:
			k = k.upper()
			if k in ['DB', 'ROOT', 'CONFIG']:
				continue

			self.env[k]	= self.resolve(self.__expand_root_path(section, k))
		return

	def exists(self, path):
		""" TODO: exists
		Arguments
			path -- TODO
		""" 
		if self.bootimage is None:
			return os.path.exists(path)

		return self.bootimage.exists(path)

	def get_root_folder(self):
		""" Returns the root folder
		Arguments
			"""
		return self.root

	def get_keys(self, type):
		""" Returns the keys of a type
		Arguments
			type -- Section that defines the type
		"""
		return self.parser[type]

	def get_folder(self,type,key):
		""" Returns a resolved directory path
		Arguments
			type -- Section that defines the type
			key -- Key name
		"""
		return self.__get_expanded_path(type, key)

	def get_file(self, type:str, key:str):
		""" Returns an file path
		Arguments
			type -- Section that defines the type
			key -- Key name
		"""
		return self.__get_expanded_path(type, key)

	def __normalize(self, path:str):
		""" Internal function to normalize a path to local pathname
		Arguments
			path -- Path to normalize
		"""
		if path is None:
			return path

		return path.replace( '/', os.sep )


	def __expand_root_path(self,type,key):
		""" Internal function expands a root path
		Arguments
			type -- Type of the object
			key -- Key identifier
		"""
		value	= self.get_value(type,key)
		if value == None:
			return value

		for k, v in os.environ.items():
			if value.find(f'$({k})') != -1:
				value	= value.replace(f'$({k})', v)
				break

		return self.__normalize( value )

	def __get_expanded_path(self,type,key):
		""" Internal function expands a path
		Arguments
			type -- Section that defines the type
			key -- Key name
		"""
		return self.resolve( self.get_value(type,key) )

	def resolve_argv(self, args):
		matches	= re.findall( r'\$\([A-Z_]*\)', args )
		for p in matches:
			key	= str(p)
			if args.find(key) == -1:
				 continue
			
			value	= self.resolve(key)
			args	= args.replace(key, value)
		return args

	def resolve(self, value):
		""" Resolves a value with configuration variables
		Arguments
			value -- Path to resolve
		"""
		if value.find(f'$({self.approot})') != -1:
			return self.__normalize( value.replace(f'$({self.approot})', self.workspace) )

		if value.find('$(ROOT)') != -1:
			value	= value.replace('$(ROOT)', self.root)

		if value.find('$(DB)') != -1:
			value	= value.replace('$(DB)', self.db)

		if value.find('$(CONFIG)') != -1:
			value = value.replace('$(CONFIG)', self.config)

		for k, v in self.env.items():
			if value.find(f'$({k})') != -1:
				value	= value.replace(f'$({k})', v)

		# Configuration paths loaded from the boot image file are not normalized.
		if self.bootimage is not None:
			return value
		
		return self.__normalize(value)

	def get_value(self,type,key):
		""" Returns a string value
		Arguments
			type -- Section that defines the type
			key -- Key name
		"""
		value 	= self.parser.get(type,key)

		# Support inline comments
		comment	= value.find(';')
		if comment != -1:
			value	= value[:comment].rstrip()
		return value

	def get_bool(self,type,key):
		""" Returns a boolean value
		Arguments
			type -- Section that defines the type
			key -- Key name
		"""
		return self.parser.get(type,key).lower() == 'true'

	def get_int(self,type,key):
		""" Returns an integer value
		Arguments
			type -- Section that defines the type
			key -- Key name
		"""
		return int(float(self.parser.get(type,key)))

	def find_config_file(self):
		""" Finds the confituration file in the path
		Arguments
			"""
		filepath = self.inifile
		if filepath is None:
			return None

		if self.appconfig is not None:
			self.config = os.environ[self.appconfig]
			filepath = os.path.join( self.config, self.inifile)

		if self.exists(filepath) == True:
			return filepath

		self.config = '.'
		return None

	@staticmethod
	def resolve_path( value:str, sep=None ):
		""" Resolves a path
		Arguments
			value -- Path name
			sep=None -- Separator for the path
		"""
		value = Configuration.replace_separators( value, sep )
		for k, v in os.environ.items():
			if value.find(f'$({k})') != -1:
				return value.replace(f'$({k})', v)

		return value

	@staticmethod
	def replace_separators( path:str, sep=None ):
		""" Replaces the separators in a generic unix path with the native path separtor
		Arguments
			path -- Path to parse
			sep=None -- Separator for the path
		"""
		sep = Configuration.__get_separator(sep)
		return path.replace( '/', sep )

	@staticmethod
	def __get_separator( sep=None ):
		""" Helper function to return the separator
		Arguments
			sep=None -- Separator for the path
		"""
		if sep == None:
			return os.sep

		return sep


if __name__ == "__main__":
	test = Configuration()


