from .... import config
from ..blocks import *

async def gen_block(x: int, y: int, z: int) -> Block:
    if (y < config.SEA_LEVEL):
        stone = await get_block("minecraft:stone", "stone")
        return stone
    elif (y == config.SEA_LEVEL):
        stone = await get_block("minecraft:stone", "stone")
        stone.lignt = 15
        return stone
    
    air = await get_block("minecraft:air", "air")
    return air