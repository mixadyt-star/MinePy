from ....common_types import *
from ..packet import Packet

class KeepAlive:
    @staticmethod
    async def create(keep_alive_id) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x1f),
            await Long.encode(keep_alive_id),
        )
