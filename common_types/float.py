import struct

class Float:
    @staticmethod
    async def encode(data: float) -> bytes:
        return struct.pack('f', data)
    
    @staticmethod
    async def decode(data: bytearray) -> float:
        return struct.unpack('f', data)