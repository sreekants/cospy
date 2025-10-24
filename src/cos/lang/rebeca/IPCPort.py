#!/usr/bin/python
# Filename: Port.py
# Description: Implementation of the Port class

from compiler.lang.objects.Port import Interface
from cos.core.kernel.Context import Context

class IPCPort(Interface):
    def __init__(self, ctxt:Context = None):
        Interface.__init__(self)
        self.ctxt       = ctxt
        self.fds        = {}
        self.next_fd    = 4096
        return

    def send(self, fd, msg, options=None):
        self.ctxt.ipc.push( self.fds[fd], msg )
        return

    def receive(self, fd, options=None):
        return self.ctxt.ipc.pop( self.fds[fd] )

    def is_pending(self, fd):
        return self.ctxt.empty( self.fds[fd] ) == False

    def is_open(self, fd):
        return self.fds.get(fd, None) is not None

    def setopt(self, fd, option, value):
        print(f"Setting option {option} to {value}")
        return True

    def getopt(self, fd, option):
        print(f"Getting option {option}")
        return None

    def connect(self, fd, address:str):
        if self.fds.has(fd):
            return False
        
        self.fds[fd]    = address
        return True

    def open(self, type:str):
        self.next_fd    += 1
        return self.next_fd

    def close(self, fd):
        print(f"Closing port {fd}")
        if self.fds.has(fd) == False:
            return False
        
        del self.fds[fd]
        return True

		

if __name__ == "__main__":
	test = IPCPort()

