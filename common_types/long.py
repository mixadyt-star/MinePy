import asyncio

from . import CommonType, multi_pop

class Long(CommonType):
    @staticmethod
    async def encode(data: int) -> bytes:
        return (data & 0xFFFFFFFFFFFFFFFF).to_bytes(8, "big")
    
    @staticmethod 
    async def _decode(data: bytearray) -> int:
        return int.from_bytes(multi_pop(data, 8), signed=True)

    @staticmethod
    async def decode(reader: asyncio.StreamReader) -> int:
        return await Long._decode(bytearray(await reader.read(8)))