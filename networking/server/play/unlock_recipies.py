from typing import List

from networking.server.packet import Packet
from common_types.boolean import Boolean
from common_types.varint import VarInt

class UnlockRecepies:
    @staticmethod
    async def create(action: int,
                     craft_book_open: bool,
                     filtering_craftable: bool,
                     array1_size: int,
                     array1: List[int],
                     array2_size: int,
                     array2: List[int]) -> bytes:
        
        array1_payload = b''
        for id in array1:
            array1_payload += await VarInt.encode(id)

        array2_payload = b''
        for id in array2:
            array2_payload += await VarInt.encode(id)

        return await Packet.create(
            await VarInt.encode(0x31),
            await VarInt.encode(action),
            await Boolean.encode(craft_book_open),
            await Boolean.encode(filtering_craftable),
            await VarInt.encode(array1_size),
            array1_payload,
            await VarInt.encode(array2_size),
            array2_payload,
        )
