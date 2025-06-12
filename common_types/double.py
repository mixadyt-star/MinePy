import asyncio
import struct

from . import CommonType, multi_pop

class Double(CommonType):
    @staticmethod
    async def encode(data: float) -> bytes:
        return struct.pack('>d', data)
    
    @staticmethod
    async def _decode(data: bytearray) -> float:
        return struct.unpack('>d', multi_pop(data, 8))
    
    @staticmethod
    async def decode(reader: asyncio.StreamReader) -> float:
        return await Double._decode(bytearray(await reader.read(8)))