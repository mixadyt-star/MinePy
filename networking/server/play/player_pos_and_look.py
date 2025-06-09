from ....common_types import *
from ..packet import Packet

class PlayerPosAndLook:
    @staticmethod
    async def create(x: float,
                     y: float,
                     z: float,
                     yaw: float,
                     pitch: float,
                     flags: int,
                     tp_id: int) -> bytes:
        return await Packet.create(
            await VarInt.encode(0x2f),
            await Double.encode(x),
            await Double.encode(y),
            await Double.encode(z),
            await Float.encode(yaw),
            await Float.encode(pitch),
            await Byte.encode(flags),
            await VarInt.encode(tp_id),
        )
