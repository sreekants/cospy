#!/usr/bin/python
# Filename: FileSystem.py
# Description: Implementation of the FileSystem class

class FileSystem:
	def __init__(self):
		""" Constructor
		"""
		return

	def mount(self):
		""" Mounts the file system
		"""
		return

	def umount(self):
		""" Unmounts the file system
		"""
		return

	def open(self, path:str, mode:str):
		""" Opens a file and returns a stream
		Arguments
			path -- Path of the file
			mode -- Open mode
		"""
		return open(path, mode)

	def close(self, fp):
		""" Closes a file stream
		Arguments
			fp -- File stream
		"""
		if fp is None:
			return 0

		return fp.close()

	def write_file(self, path:str, text:str):
		""" Dumps text into a file
		Arguments
			path -- Path of the file
			text -- Text to dump
		"""
		with open(path, 'w+t') as f:
			f.write(text)
		return

	def read_file(self, path:str):
		""" Returns the content of a file as text
		Arguments
			path -- Path of the file
		"""
		with open(path, 'rt') as f:
			return f.read()

	def read_file_as_bytes(self, path:str):
		""" Returns the content of a file as bytes
        Arguments
            path -- Path of the file
        """
		with open(path, 'rb') as f:
			return f.read()

if __name__ == "__main__":
	test = FileSystem()


