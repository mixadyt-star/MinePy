import asyncio

from ....common_types import *
from ..packet import Packet

class _Handshake:
    def __init__(self,
                 version: int,
                 address: str,
                 port: int,
                 intent: int):
        
        self.version = version
        self.address = address,
        self.port = port
        self.intent = intent

class Handshake:
    @staticmethod
    async def create(reader: asyncio.StreamReader) -> _Handshake:
        return await Packet.create(
            reader=reader,
            data_class=_Handshake,
            version=VarInt,
            address=String,
            port=UnsignedShort,
            intent=VarInt,
        )
