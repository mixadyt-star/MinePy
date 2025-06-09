from .byte import Byte

class Angle:
    @staticmethod
    async def encode(data: int) -> bytes:
        return await Byte.encode(data)
    
    @staticmethod
    async def decode(data: bytearray) -> int:
        return await Byte.decode(data)