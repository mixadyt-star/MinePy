from ....common_types import *
from ..packet import Packet

class LoginSuccess:
    @staticmethod
    async def create(uuid: str, name: str) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x2),
            await String.encode(uuid),
            await String.encode(name),
        )
