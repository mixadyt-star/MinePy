import json

from ....common_types import *
from ..packet import Packet

class StatusResponse:
    @staticmethod
    async def create(version_name: str,
                     version_protocol: int,
                     max_players: int,
                     players_online: int,
                     server_description: str,
                     server_icon: str):
        
        data = json.dumps({
            "version": {
                "name": version_name,
                "protocol": version_protocol,
            },
            "players": {
                "max": max_players,
                "online": players_online,
            },
            "description": {
                "text": server_description,
            },
            "favicon": server_icon,
            "enforcesSecureChat": False,
        })

        return await Packet.create(
            await VarInt.encode(0x0),
            await String.encode(data),
            is_compressed=False,
        )
