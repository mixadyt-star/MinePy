import asyncio

from . import CommonType
from .byte import Byte

class Angle(CommonType):
    @staticmethod
    async def encode(data: int) -> bytes:
        return await Byte.encode(data)
    
    @staticmethod
    async def _decode(data: bytearray) -> int:
        return await Byte._decode(data)
    
    @staticmethod
    async def decode(reader: asyncio.StreamReader) -> int:
        return await Angle._decode(bytearray(await reader.read(1)))