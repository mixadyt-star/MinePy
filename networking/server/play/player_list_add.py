from typing import List, Tuple

from networking.server.packet import Packet
from common_types.unsigned_byte import UnsignedByte
from common_types.integer import Integer
from common_types.boolean import Boolean
from common_types.varint import VarInt
from common_types.string import String
from common_types.uuid import UUID

class PlayerListAdd:
    @staticmethod
    async def create(number_of_players: int,
                     players: List[Tuple[str, str, int, List[Tuple[str, str, bool, str | None]] | None, int, int, bool, str | None]]) -> bytes:

        players_payload = b''
        for uuid, username, num_of_props, props, gamemode, ping, has_disp_name, disp_name in players:
            players_payload += await UUID.encode(uuid)
            players_payload += await String.encode(username)
            players_payload += await VarInt.encode(num_of_props)
            props_payload = b''
            if (num_of_props > 0):
                for name, value, is_signed, signed in props:
                    props_payload += await String.encode(name)
                    props_payload += await String.encode(value)
                    props_payload += await Boolean.encode(is_signed)
                    if (is_signed):
                        props_payload += await String.encode(signed)
            players_payload += props_payload
            players_payload += await VarInt.encode(gamemode)
            players_payload += await VarInt.encode(ping)
            players_payload += await Boolean.encode(has_disp_name)
            if (has_disp_name):
                players_payload += await String.encode(disp_name)

        return await Packet.create(
            await VarInt.encode(0x2e),
            await VarInt.encode(0x0),
            await VarInt.encode(number_of_players),
            players_payload,
        )
