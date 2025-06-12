import asyncio

from ....common_types import *
from ..packet import Packet

class _StatusPingRequest:
    def __init__(self, payload: int):
        self.payload = payload

class StatusPingRequest:
    @staticmethod
    async def create(reader: asyncio.StreamReader) -> _StatusPingRequest:
        return await Packet.create(
            reader=reader,
            data_class=_StatusPingRequest,
            payload=Long,
        )
