from ....common_types import *

class _TeleportConfirm:
    def __init__(self, tp_id: int):
        self.tp_id = tp_id

class TeleportConfirm:
    @staticmethod
    async def create(data: bytearray) -> _TeleportConfirm:
        return _TeleportConfirm(
            tp_id=await VarInt.decode(data),
        )
