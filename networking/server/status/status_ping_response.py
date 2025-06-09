from ....common_types import *
from ..packet import Packet

class StatusPingResponse:
    @staticmethod
    async def create(payload: int) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x1),
            await Long.encode(payload),
            is_compressed=False,
        )
