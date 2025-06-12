import asyncio

from ....common_types import *
from ..packet import Packet

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
    async def create(reader: asyncio.StreamReader) -> _ClientSettings:
        return await Packet.create(
            reader=reader,
            data_class=_ClientSettings,
            locale=String,
            view_distance=Byte,
            chat_mode=VarInt,
            chat_colors=Boolean,
            displayed_skin_parts=UnsignedByte,
            main_hand=VarInt,
        )