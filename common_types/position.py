from typing import Tuple

from .long import Long

class Position:
    @staticmethod
    async def encode(data: Tuple[int, int, int]) -> bytes:
        x, y, z = data
        position = ((x & 0x3FFFFFF) << 38) | ((y & 0xFFF) << 26) | (z & 0x3FFFFFF)
        return await Long.encode(position)
    
    @staticmethod
    async def decode(data: bytearray) -> Tuple[int, int, int]:
        position = await Long.decode(data)
        x = position >> 38
        y = (position >> 26) & 0xFFF
        z = position << 38 >> 38

        return x, y, z