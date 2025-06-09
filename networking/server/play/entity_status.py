from typing import Tuple

from networking.server.packet import Packet
from common_types.integer import Integer
from common_types.varint import VarInt
from common_types.byte import Byte

class EntityStatus:
    @staticmethod
    async def create(eid: int, entity_status: int) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x1b),
            await Integer.encode(eid),
            await Byte.encode(entity_status),
        )
