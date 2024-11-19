#!/usr/bin/python
# Filename: self.py
# Description: Log subsysten for the simulation

from cos.core.kernel.Configuration import Configuration
from cos.core.utilities.ActiveRecord import ActiveRecord
import os, datetime, colorama, time

# Error codes match Win32 error log codes
EVENTLOG_ERROR_TYPE				= 0x0001	# Log and exit
EVENTLOG_WARNING_TYPE			= 0x0002	# Log errorcode, no exit
EVENTLOG_INFORMATION_TYPE		= 0x0004	# Informational Log, no exit
EVENTLOG_SYSTEM_ERROR			= 0x1001	# Log errorcode & exit
EVENTLOG_ABNORMAL_TERMINATION	= 0x2001	# Log errorcode, core dump & exit

class LogFile:
	def __init__(self, dbpath, table='system', utcmode=False):
		""" Constructor
		Arguments
			dbpath -- Database repository to add logs to
			table -- Table to save to.
			utcmode -- Time log mode (local vs. UTC)
		"""

		if dbpath is None:
			self.model	= None
			return

		#If the content database does not exist, create it
		if os.path.isfile(dbpath) == True:
			self.model	= ActiveRecord.create(table, dbpath, table)
		else:
			self.model	= ActiveRecord.create(table, dbpath, table)
			self.model.execute_sql( f'CREATE TABLE [{table}] ('\
				'[id] INTEGER NULL, [creation_time] TIMESTAMP NULL,'\
				'[module] VARCHAR(64) NULL, [log_type] INTEGER NULL,'\
				'[description] VARCHAR(128) NULL, [category] VARCHAR(32) NULL,'\
				'[computer] VARCHAR(64) NULL, [user] VARCHAR(64) NULL,'\
				'[source] VARCHAR(64) NULL)' )
		self.utcmode	= utcmode
		self.path		= dbpath
		return

	def log(self, module, log_type, text):
		""" Adds a log entry
		Arguments
			module -- Module to log for
			log_type -- Type of the log
			text -- Text of the log
		"""
		if self.model is None:
			return

		if self.utcmode == False:
			logtime = datetime.datetime.now()
		else:
			logtime	= datetime.datetime.utcnow()

		print(text)

		values = {
			'creation_time':logtime,
			'module':module,
			'log_type': log_type,
			'description': text,
			'category': 'SYSTEM',
			'computer': '127.0.0.1' }
		self.model.add( values )
		return

	def flush(self):
		""" Flushes the log.
		"""
		return

	def error(self, module, text):
		""" Logs an error
		Arguments
			module -- Module to log for
			text -- Text of the log
		"""
		self.log( module, EVENTLOG_ERROR_TYPE, text )
		return

	def warning(self, module, text):
		""" Logs a warning
		Arguments
				module -- Module to log for
			text -- Text of the log
		"""
		self.log( module, EVENTLOG_WARNING_TYPE, text )
		return

	def info(self, module, text):
		""" Logs an information
		Arguments
				module -- Module to log for
			text -- Text of the log
		"""
		self.log( module, EVENTLOG_INFORMATION_TYPE, text )
		return

class LoggerSettings:
	def __init__(self, config:Configuration=None):
		""" Constructor
		Arguments
			"""
		if config is None:
			return

		path = config.get_file('SystemUtilities.Logger', 'LogFile')

		if path is None:
			self.file	= None
		else:
			self.file	= LogFile( path )

		self.disabled_modules	= []
		self.silentmode 		= False
		return

	def disable_module(self, name):
		""" Disables module from logging
		Arguments
			name -- Module name
		"""
		self.disabled_modules.append(name)
		return

	def is_module_enabled(self, module):
		""" Check if a module can be logged
		Arguments
				module -- Module name
		"""
		return module not in self.disabled_modules

	@property
	def silent(self):
		""" Checks if operation is in silent mode
		"""
		return self.silentmode

class Logger:
	def __init__(self, config:Configuration=None):
		""" Constructor
		Arguments
			config -- Configuration attributes
		"""
		self.settings	= LoggerSettings(config)
		return


	def set_silent(self, is_silent:bool=True):
		""" Sets the tracing to silent mode (no dump on the console)
		Arguments
			is_silent -- Sets the silent mode
		"""
		self.settings.silentmode	= is_silent


	def error(self, module:str, text:str, log_to_file:bool=False):
		""" Dumps an error
		Arguments
			module -- Module information
			text -- Log text
			log_to_file -- Flag to enable logging
		"""
		self.__print_error(module, text)

		if log_to_file == True:
			self.settings.file.error(module, text)
		return


	def warning(self, module:str, text:str, log_to_file:bool=False):
		""" Dumps a warning
		Arguments
			module -- Module information
			text -- Log text
			log_to_file -- Flag to enable logging
		"""
		self.__print_warning(module, text)

		if log_to_file == True:
			self.settings.file.warning(module, text)
		return


	def info(self, module:str, text:str, log_to_file:bool=False):
		""" Dumps a log information
		Arguments
			module -- Module information
			text -- Log text
			log_to_file -- Flag to enable logging
		"""
		self.__print_information(module, text)

		if log_to_file == True:
			self.settings.file.info(module, text)
		return


	def debug(self, module:str, text:str):
		""" Prints a debug message
		Arguments
			module -- Module name
			text -- Log text
		"""
		self.__print_debug(module, text)
		return


	def trace(self, module:str, text:str, log_to_file:bool=False, log_to_file_only:bool=False):
		""" Traces a message
		Arguments
			module -- module Name
			text -- text to print or write to file
			log_to_file -- true if 'text' is to be written to log file
			log_to_file_only -- true if 'text' is not to be printed but to be written to log file
		"""
		ctxt = self.settings

		if self.is_log_enabled(module):
			if (log_to_file_only == False) and (ctxt.silent == False):
				print( f'   {text}' )
			if log_to_file == True:
				ctxt.file.__print_information(module, text)
		return


	def __print_error(self, module:str, text:str):
		""" Internal function to print an error
		Arguments
			module -- Module information
			text -- Log text
		"""
		# Warnings are always printed
		if self.is_log_enabled(module):
			self.print_console( colorama.Fore.RED + colorama.Style.BRIGHT , module, self.format_text("ERR", module, text) )
		return


	def __print_warning(self, module,text):
		""" Internal function to print an warning
		Arguments
			module -- Module information
			text -- Log text
		"""
		# Warnings are always printed
		if self.is_log_enabled(module):
			self.print_console( colorama.Fore.YELLOW + colorama.Style.BRIGHT, module, self.format_text("WARN", module, text) )
		return



	def __print_information(self, module,text):
		""" Prints an information text
		Arguments
			module -- Module information
			text -- Text to print
		"""
		if self.is_log_enabled(module):
			self.print_console( colorama.Fore.GREEN+colorama.Style.BRIGHT, module, self.format_text(None, module, text) )
		return


	def __print_debug(self, module,text):
		""" Prints a debug text
		Arguments
			module -- Module information
			text -- Text to print
		"""
		if self.is_log_enabled(module):
			self.print_console( colorama.Style.NORMAL, module, text )
		return


	def print_generic(self, color, module, text):
		""" Prints an generic text
		Arguments
			color -- Text color
			module -- Module information
			text -- Text to print
		"""
		if self.settings.silent == True:
			return

		print( color + text + colorama.Style.RESET_ALL )
		return


	def print_console(self, color, module, text):
		""" Prints text to console
		Arguments
			color -- Text color
			module -- Module information
			text -- Text to print
		"""
		if self.settings.silent == True:
			return

		print( color + self.get_timestamp()+ ' ' + text + colorama.Style.RESET_ALL )
		return


	def format_text(self, prefix, module, text):
		""" Formats a text
		Arguments
			prefix -- Text prefix
			module -- Module name
			text -- Log text
		"""
		if (prefix==None) or len(prefix):
			return f'({module}) {text}'

		return f'{prefix}({module}) {text}'


	def is_log_enabled(self, module):
		""" Checks if a module is enabled for logging
		Arguments
			module -- Module information
		"""

		return self.settings.is_module_enabled(module)


	def get_timestamp(self):
		""" Generates a time stamp for the log
		"""
		return time.strftime('%d/%m/%y %H:%M:%S')

if __name__ == "__main__":
	test = LogFile("test.s3db")
	test.error("COLREG.Rule1", "Failed on ship 1")


