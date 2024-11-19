#!/usr/bin/python
# Filename: Errors.py
# Description: Generic implementation of a tree data structure

from enum import Enum

class ErrorCode(Enum):			# Win32 Error codes
	ERROR_CONTINUE			= 1246
	ERROR_NO_MORE_ITEMS		= 259
	ERROR_INVALID_LEVEL		= 124
	ERROR_FILE_NOT_FOUND	= 2
	ERROR_PATH_NOT_FOUND	= 3

	ERROR_HANDLE_EOF       	= 38
	ERROR_HANDLE_DISK_FULL 	= 39
	ERROR_NOT_SUPPORTED    	= 50
	ERROR_DUP_NAME         	= 52
	ERROR_DEV_NOT_EXIST    	= 55
	ERROR_NETWORK_BUSY     	= 54
	ERROR_INVALID_PARAMETER	= 87
	ERROR_INVALID_PASSWORD 	= 86
	ERROR_FILE_EXISTS      	= 80
	ERROR_ALREADY_EXISTS   	= 183
	ERROR_SERVICE_EXISTS   	= 1073

	E_NOTIMPL         		= 0x80004001
	E_UNEXPECTED      		= 0x8000FFFF
	E_OUTOFMEMORY     		= 0x8007000E
	E_INVALIDARG      		= 0x80070057
	E_HANDLE          		= 0x80070006
	E_ABORT           		= 0x80004004
	E_POINTER         		= 0x80004003
	E_NOINTERFACE     		= 0x80004002
	E_FAIL            		= 0x80000008
	E_ACCESSDENIED    		= 0x80000009
	E_PENDING         		= 0x8000000A


	NOERROR             	= 0x00000000
	S_FALSE					= 0x00000001
	S_TRUE					= 0x00000000
	S_OK					= 0x00000000

	# Runtime exception types
	ERROR_EXCEPTION_IN_SERVICE       = 0x00001064
	EVENT_E_INTERNALEXCEPTION        = 0x80040205
	EVENT_E_USER_EXCEPTION           = 0x80040208
	DISP_E_EXCEPTION                 = 0x80020009

if __name__ == "__main__":
	t = ErrorCode()



