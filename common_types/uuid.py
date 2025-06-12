import asyncio
import uuid

from . import CommonType, multi_pop

class UUID(CommonType):
    @staticmethod
    async def encode(data: str) -> bytes:
        return uuid.UUID(data).bytes
    
    @staticmethod
    async def _decode(data: bytearray) -> str:
        return str(uuid.UUID(bytes=multi_pop(data, 16)))
    
    @staticmethod
    async def decode(reader: asyncio.StreamReader) -> str:
        return await UUID._decode(bytearray(await reader.read(16)))