#!/usr/bin/python
# Filename: BootImage.py
# Description: Implementation of the BootImage class

import tarfile, io
import os.path, sys

class FileSystem:
	def __init__(self, file):
		""" Constructor
		Arguments
			file -- Path of the image file
		"""
		self.name	= file
		self.tar	= None
		return

	def mount(self):
		""" TODO: mount
		""" 
		if self.tar is not None:
			return False

		self.tar	= tarfile.open(self.name)
		return True

	def umount(self):
		""" TODO: umount
		""" 
		if self.tar is None:
			return False

		self.tar.close()
		self.tar	= None
		return True

	def create(self, source):
		""" Adds a directory to the image
		Arguments
			source -- Source directory path
		"""
		with tarfile.open(self.name, "w") as tar:
			tar.add(source, arcname=os.path.basename("$FS"))
		return

	def open(self, path:str, mode:str):
		""" Dummy function for compatibility - Opens a file
		Arguments
			path -- Path of the file in the image
			mode -- Open mode
		"""
		return 1

	def close(self, fp):
		""" Closes a file stream
		Arguments
			fp -- Unused handle
		"""
		return 0

	def exists(self, path:str):
		""" Checks if a file exists in an image
		Arguments
			path -- Path of the file in the image
		"""
		if self.tar is None:
			return False

		if path not in self.tar.getnames():
			return False
		return True

	def read_file(self, path:str):
		""" Returns the content of a file as text
		Arguments
			path -- Path of the file in the image
		"""
		if path.startswith("$FS") == False:
			with open(path, 'rt') as f:
				return f.read()

		if self.tar is None:
			return None

		with self.tar.extractfile(path) as extracted:
			with io.TextIOWrapper(extracted) as txtextracted:
				return txtextracted.read()

	def read_file_as_bytes(self, path:str):
		""" Returns the content of a file as bytes
        Arguments
            path -- Path of the file in the image
        """
		if path.startswith("$FS") == False:
			with open(path, 'rb') as f:
				return f.read()

		if self.tar is None:
			return None

		with self.tar.extractfile(path) as extracted:
			return extracted.read()

if __name__ == "__main__":
	test = FileSystem( 'boot.image')
	test.create( '..\\..\\..\\..\\config' )
	sys.exit(0)

	test.mount()
	for file in ['cos.ini', 'trip/trip1.csv']:
		print( test.read_file(file) )

