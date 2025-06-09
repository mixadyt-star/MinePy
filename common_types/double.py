import struct

class Double:
    @staticmethod
    async def encode(data: float) -> bytes:
        return struct.pack('>d', data)
    
    @staticmethod
    async def decode(data: bytearray) -> float:
        return struct.unpack('>d', data)