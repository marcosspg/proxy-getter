class Proxy:
    type = "";
    address = "";
    port = "";

    def __init__(self,type,address, port): 
          self.type = type
          self.address = address
          self.port = port

    def __str__(self):
        return "type: "+self.type+", address: "+self.address+", port: "+self.port;