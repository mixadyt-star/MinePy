import json
import math
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(os.path.dirname(os.path.dirname(current_dir)), "static\\blocks.minepy")
blocks = json.load(open(file_path))

bits_per_block = 0
for identifier, block in blocks.items():
    bits_per_block += len(block) - 1
bits_per_block = 13 # math.ceil(math.log2(bits_per_block))

class Block:
    def __init__(self, id: int, data: int, light: int, sky_light: int):
        self.id = id
        self.data = data
        self.lignt = light
        self.sky_light = sky_light

async def get_block(identifier: str, block: str) -> Block:
    global blocks

    return Block(blocks[identifier]["id"], blocks[identifier][block], 0, 15)