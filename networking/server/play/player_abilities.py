from ....common_types import *
from ..packet import Packet

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
