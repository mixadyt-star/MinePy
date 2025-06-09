from networking.server.packet import Packet
from common_types.unsigned_byte import UnsignedByte
from common_types.integer import Integer
from common_types.boolean import Boolean
from common_types.varint import VarInt
from common_types.string import String

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
