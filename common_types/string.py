import asyncio

from . import CommonType, multi_pop
from .varint import VarInt

class String(CommonType):
    @staticmethod
    async def encode(data: str) -> bytes:
        temp = await VarInt.encode(len(data))
        encoded = temp + data.encode()

        return encoded

    @staticmethod
    async def _decode(data: bytearray) -> str:
        length = await VarInt._decode(data)

        return multi_pop(data, length).decode()
    
    @staticmethod
    async def decode(reader: asyncio.StreamReader) -> str:
        return (await reader.read(await VarInt.decode(reader))).decode()