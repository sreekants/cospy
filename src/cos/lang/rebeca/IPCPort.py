#!/usr/bin/python
# Filename: Port.py
# Description: Implementation of the Port class

from compiler.lang.objects.Port import Interface
from cos.core.kernel.Context import Context
from cos.core.kernel.Object import Object
from cos.core.kernel.Request import Request

class IPCChannel:
    def __init__(self, ctxt, address):
        self.ctxt       = ctxt
        self.address    = address
        return
    
    def send(self, msg):
        self.ctxt.ipc.push( self.address, msg )
        return

    def receive(self):
        return self.ctxt.ipc.pop( self.address )
    
    def is_pending(self):
        return self.ctxt.ipc.is_pending( self.address )

class RPCChannel:
    def __init__(self, ctxt, address):
        self.object     = ctxt.sim.objects.get(address)
        self.ctxt       = ctxt
        return
    
    def send(self, msg):
        # Unmarshall the request call
        req = Request()
        req.parse(msg)

        if req.method is None:
            self.ctxt.log.error(f"Service {self.name} received a request with no instance.")
            return

        # Invoke the method on the actor
        self.object.notify(self, req.method, req.args)
        return

    def receive(self):
        return None
    
    def is_pending(self):
        return False

class IPCPort(Interface):
    def __init__(self, ctxt:Context = None):
        Interface.__init__(self)
        self.ctxt       = ctxt
        self.fds        = {}
        self.next_fd    = 4096
        return

    def __getfd(self, fd):
        type, port    = self.fds.get(fd, (None, None))
        if port is None:
            raise Exception(f"Port {fd} not found")
        
        return port
    
    def send(self, fd, msg, options=None):
        self.__getfd(fd).send( msg )
        return

    def receive(self, fd, options=None):
        return self.__getfd(fd).receive()

    def is_pending(self, fd):
        return self.__getfd(fd).is_pending()

    def is_open(self, fd):
        return self.fds.get(fd, None) is not None

    def setopt(self, fd, option, value):
        print(f"Setting option {option} to {value}")
        return True

    def getopt(self, fd, option):
        print(f"Getting option {option}")
        return None

    def connect(self, fd, address:str):
        if self.fds.get(fd, None) is not None:
            return False
        
        if address.startswith("ipc://") == True:
            type    = "ipc"
            port    = IPCChannel(self.ctxt, address[5:])
        elif address.startswith("rpc://") == True:
            type    = "rpc"
            port    = RPCChannel(self.ctxt, address[5:])
        else:
            raise Exception(f"Unknown address type {address}")

        self.fds[fd]    = (type, port)
        return True

    def open(self, type:str):
        self.next_fd    += 1
        if type.find('//'):
            self.connect( self.next_fd, type )
        return self.next_fd

    def close(self, fd):
        print(f"Closing port {fd}")
        if self.fds.has(fd) == False:
            return False
        
        del self.fds[fd]
        return True

		

if __name__ == "__main__":
	test = IPCPort()

