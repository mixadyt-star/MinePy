from typing import Tuple

from networking.server.packet import Packet
from common_types.varint import VarInt
from common_types.byte import Byte

class HeldItemChange:
    @staticmethod
    async def create(slot: int) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x3a),
            await Byte.encode(slot),
        )
