import json
import math

blocks = json.load(open("static/blocks.minepy"))

bits_per_block = 0
for identifier, block in blocks.items():
    bits_per_block += len(block) - 1
bits_per_block = math.ceil(math.log2(bits_per_block))

class Block:
    def __init__(self, id: int, data: int, light: int, sky_light: int):
        self.id = id
        self.data = data
        self.lignt = light
        self.sky_light = sky_light

async def get_block(identifier: str, block: str) -> Block:
    global blocks

    return Block(blocks[identifier]["id"], blocks[identifier][block], 0, 15)