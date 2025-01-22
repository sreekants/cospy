

class VTSChannel:
    def __init__(self):
        pass

    def Open(self):
        return

    def Connect(self):
        return
    
    def Send(self, msg):
        return
    
    def Receive(self, msg):
        return

class TrafficAgent:
    def __init__(self):
        self.vts    = None
        return

    def start(self):
        self.vts    = VTSChannel()
        self.vts.Open()
        self.vts.Connect()
        return

    
class TrafficController(TrafficAgent):
    def __init__(self):
        TrafficAgent.__init__(self)
        return


    