import asyncio

from . import CommonType, multi_pop

class Boolean(CommonType):
    @staticmethod
    async def encode(data: bool) -> bytes:
        return int(data).to_bytes(1, "big")
    
    @staticmethod
    async def _decode(data: bytearray) -> bool:
        return bool(multi_pop(data, 1))
    
    @staticmethod
    async def decode(reader: asyncio.StreamReader) -> bool:
        return await Boolean._decode(bytearray(await reader.read(1)))