import zlib

from ...common_types import *
from ... import config

class Packet:
    @staticmethod
    async def create(*args, is_compressed: bool = True) -> bytes:
        payload = b''
        
        for data in args:
            payload += data

        if (is_compressed):
            if (len(payload) >= config.COMPRESSION_THRESHOLD):
                compressed = zlib.compress(payload)
                return (await VarInt.encode(len(compressed))) + (await VarInt.encode(len(payload))) + compressed
            else:
                return (await VarInt.encode(len(payload) + 1)) + (await VarInt.encode(0)) + payload
        else:
            return (await VarInt.encode(len(payload))) + payload