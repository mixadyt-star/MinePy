import asyncio

from ....common_types import *
from ..packet import Packet

class _LoginStart:
    def __init__(self, username: str):
        self.username = username

class LoginStart:
    @staticmethod
    async def create(reader: asyncio.StreamReader):
        return await Packet.create(
            reader=reader,
            data_class=_LoginStart,
            username=String,
        )
