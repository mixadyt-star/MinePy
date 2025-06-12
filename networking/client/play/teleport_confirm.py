import asyncio

from ....common_types import *
from ..packet import Packet

class _TeleportConfirm:
    def __init__(self, tp_id: int):
        self.tp_id = tp_id

class TeleportConfirm:
    @staticmethod
    async def create(reader: asyncio.StreamReader) -> _TeleportConfirm:
        return await Packet.create(
            reader=reader,
            data_class=_TeleportConfirm,
            tp_id=VarInt,
        )
