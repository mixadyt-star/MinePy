import asyncio

from . import CommonType, multi_pop

class Integer(CommonType):
    @staticmethod
    async def encode(data: int) -> bytes:
        return (data & 0xFFFFFFFF).to_bytes(4, "big")
    
    @staticmethod
    async def _decode(data: bytearray) -> int:
        return int.from_bytes(multi_pop(data, 4), signed=True) 
    
    @staticmethod
    async def decode(reader: asyncio.StreamReader) -> int:
        return await Integer._decode(bytearray(await reader.read(4)))