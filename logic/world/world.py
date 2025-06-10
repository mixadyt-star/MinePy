from ...logger import *
from ... import config
set_verbosity_level(config.VERBOSITY_LEVEL)

import os

from .chunk import Chunk, _Chunk
from ...storing import *

class World:
    @staticmethod
    async def generate():
        for x in range(-18, 19):
            for z in range(-18, 19):
                if (not file_exists(f"data\\world\\overworld_{x}_{z}.minepy")):
                    chunk = await World.get_packed_chunk(x, z)
                    del chunk

                log(f"Generating world... {round(((x + 18) * 37 + (z + 18)) / 13.69, 1)}%", end="\r")
        
        log('Generating world... 100%   ')
    
    @staticmethod
    async def get_packed_chunk(x: int, z: int) -> bytes:
        chunk = load_bytes(f"data\\world\\overworld_{x}_{z}.minepy")
        if (chunk is not None):
            return chunk
        else:
            chunk = await Chunk.pack(await Chunk.generate(x, z))
            await World.store_chunk(chunk, x, z)
            return chunk

    @staticmethod
    async def store_chunk(chunk: bytes, x: int, z: int):
        store_bytes(f"data\\world\\overworld_{x}_{z}.minepy", chunk)

    @staticmethod
    async def is_world_generated() -> bool:
        for x in range(-18, 19):
            for z in range(-18, 19):
                if (not file_exists(f"data\\world\\overworld_{x}_{z}.minepy")):
                    return False
                
        return True