from typing import Tuple
import asyncio

from . import CommonType, multi_pop
from .long import Long

class Position(CommonType):
    @staticmethod
    async def encode(data: Tuple[int, int, int]) -> bytes:
        x, y, z = data
        position = ((x & 0x3FFFFFF) << 38) | ((y & 0xFFF) << 26) | (z & 0x3FFFFFF)
        return await Long.encode(position)
    
    @staticmethod
    async def _decode(data: bytearray) -> Tuple[int, int, int]:
        position = await Long._decode(data)
        x = position >> 38
        y = (position >> 26) & 0xFFF
        z = position << 38 >> 38

        return x, y, z
    
    @staticmethod
    async def decode(reader: asyncio.StreamReader) -> Tuple[int, int, int]:
        return await Position._decode(bytearray(await reader.read(8)))