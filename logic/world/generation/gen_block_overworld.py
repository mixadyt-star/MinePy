from logic.world.blocks import get_block, Block
import config

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