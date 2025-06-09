from ....common_types import *
from ..packet import Packet

class EntityStatus:
    @staticmethod
    async def create(eid: int, entity_status: int) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x1b),
            await Integer.encode(eid),
            await Byte.encode(entity_status),
        )
