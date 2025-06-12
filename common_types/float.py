import asyncio
import struct

from . import CommonType, multi_pop

class Float(CommonType):
    @staticmethod
    async def encode(data: float) -> bytes:
        return struct.pack('>f', data)
    
    @staticmethod
    async def _decode(data: bytearray) -> float:
        return struct.unpack('>f', multi_pop(data, 4))

    @staticmethod
    async def decode(reader: asyncio.StreamReader) -> float:
        return await Float._decode(bytearray(await reader.read(4)))