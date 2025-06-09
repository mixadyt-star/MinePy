from typing import Tuple

from networking.server.packet import Packet
from common_types.varint import VarInt
from common_types.float import Float
from common_types.byte import Byte

class PlayerAbilities:
    @staticmethod
    async def create(flags: int,
                     flying_speed: float,
                     field_view: float) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x2c),
            await Byte.encode(flags),
            await Float.encode(flying_speed),
            await Float.encode(field_view),
        )
