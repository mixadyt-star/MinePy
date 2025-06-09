from ....common_types import *

class _ClientSettings:
    def __init__(self,
                 locale: str,
                 view_distance: int,
                 chat_mode: int,
                 chat_colors: bool,
                 displayed_skin_parts: int,
                 main_hand: int):
        self.locale = locale
        self.view_distance = view_distance
        self.chat_mode = chat_mode
        self.chat_colors = chat_colors
        self.displayed_skin_parts = displayed_skin_parts
        self.main_hand = main_hand

class ClientSettings:
    @staticmethod
    async def create(data: bytearray) -> _ClientSettings:
        return _ClientSettings(
            locale=await String.decode(data),
            view_distance=await Byte.decode(data),
            chat_mode=await VarInt.decode(data),
            chat_colors=await Boolean.decode(data),
            displayed_skin_parts=await UnsignedByte.decode(data),
            main_hand=await VarInt.decode(data),
        )