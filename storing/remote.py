from ..static import *

class Remote:
    def __init__(self, address: str, port: int):
        self.address = address
        self.port = port
        self.username = None
        self.compression_enabled = False

    def __eq__(self, other):
        return (self.address, self.port) == (other.address, other.port)
    
    def __hash__(self):
        return hash((self.address, self.port))