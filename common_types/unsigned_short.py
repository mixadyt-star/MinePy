import asyncio

from . import CommonType, multi_pop

class UnsignedShort(CommonType):
    @staticmethod
    async def encode(data: int) -> bytes:
        return (data & 0xFFFF).to_bytes(2, "big")
    
    @staticmethod
    async def _decode(data: bytearray) -> int:
        return int.from_bytes(multi_pop(data, 2))
    
    @staticmethod
    async def decode(reader: asyncio.StreamReader) -> int:
        return await UnsignedShort._decode(bytearray(await reader.read(2)))