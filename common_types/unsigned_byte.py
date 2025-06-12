import asyncio

from . import CommonType, multi_pop

class UnsignedByte(CommonType):
    @staticmethod
    async def encode(data: int) -> bytes:
        return (data & 0xFF).to_bytes(1, "big")
    
    @staticmethod
    async def _decode(data: bytearray) -> int:
        return int.from_bytes(multi_pop(data, 1))
    
    @staticmethod
    async def decode(reader: asyncio.StreamReader) -> int:
        return await UnsignedByte._decode(bytearray(await reader.read(1)))