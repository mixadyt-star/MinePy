from ....common_types import *
from ..packet import Packet

class JoinGame:
    @staticmethod
    async def create(eid: int,
                     gamemode: int,
                     dimension: int,
                     difficulty: int,
                     max_players: int,
                     level_type: str,
                     reduced_debug_info: bool) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x23),
            await Integer.encode(eid),
            await UnsignedByte.encode(gamemode),
            await Integer.encode(dimension),
            await UnsignedByte.encode(difficulty),
            await UnsignedByte.encode(max_players),
            await String.encode(level_type),
            await Boolean.encode(reduced_debug_info),
        )
