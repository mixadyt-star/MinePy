from typing import List

from ...common_types import *
from .generation  import *
from .blocks import *

class _ChunkSection:
    def __init__(self, data: List[Block], is_empty: bool):
        self.data = data
        self.is_empty = is_empty

class ChunkSection:
    @staticmethod
    async def generate(chunk_x: int, chunk_z: int, section_y: int) -> _ChunkSection:
        data: List[Block] = []

        is_empty = True

        for y in range(16):
            for z in range(16):
                for x in range(16):
                    block = await gen_block(
                        chunk_x * 16 + x,
                        section_y * 16 + y,
                        chunk_z * 16 + z
                    )

                    if (block.id != 0):
                        is_empty = False

                    data.append(block)

        return _ChunkSection(data, is_empty)
    
    @staticmethod
    async def pack(chunk_section: _ChunkSection) -> bytes:
        packed = b''

        packed += await UnsignedByte.encode(bits_per_block)
        packed += await VarInt.encode(0)

        counter = 0
        packed_block_states = b''
        binary_block_states = ''
        packed_block_lights = b''
        binary_block_lights = ''
        packed_sky_lights = b''
        binary_sky_lights = ''
        for block in chunk_section.data:
            binary_block_states = bin(block.id)[2:].zfill(bits_per_block - 4) + \
                bin(block.data)[2:].zfill(4) + binary_block_states
            binary_block_lights = bin(block.lignt)[2:].zfill(4) + binary_block_lights
            binary_sky_lights = bin(block.sky_light)[2:].zfill(4) + binary_sky_lights
            
            if (len(binary_block_states) >= 64):
                counter += 1
                packed_block_states += await Long.encode(int(binary_block_states[-64:], 2))
                binary_block_states = binary_block_states[:-64]

            if (len(binary_block_lights) >= 8):
                packed_block_lights += await Byte.encode(int(binary_block_lights[-8:], 2))
                binary_block_lights = binary_block_lights[:-8]

            if (len(binary_sky_lights) >= 8):
                packed_sky_lights += await Byte.encode(int(binary_sky_lights[-8:], 2))
                binary_sky_lights = binary_sky_lights[:-8]

        packed += await VarInt.encode(counter)
        packed += packed_block_states
        packed += packed_block_lights
        packed += packed_sky_lights

        return packed

class _Chunk:
    def __init__(self, x: int, z: int, chunk_sections: List[_ChunkSection], biomes: List[int]):
        self.chunk_sections = chunk_sections
        self.biomes = biomes
        self.block_entities = []
        self.x = x
        self.z = z

class Chunk:
    @staticmethod
    async def generate(chunk_x: int, chunk_z: int) -> _Chunk:
        chunk_sections: List[_ChunkSection] = []
        biomes: List[int] = []
        
        for section_y in range(16):
            chunk_sections.append(await ChunkSection.generate(
                chunk_x,
                chunk_z,
                section_y,
            ))

        for z in range(16):
            for x in range(16):
                biomes.append(await gen_biome(x, z))

        return _Chunk(
            chunk_x,
            chunk_z,
            chunk_sections,
            biomes
        )
    
    @staticmethod
    async def pack(chunk: _Chunk) -> bytes:
        packed = b''

        packed += await Integer.encode(chunk.x)
        packed += await Integer.encode(chunk.z)
        packed += await Boolean.encode(True)
        
        chunk_section_mask = 0
        data = b''
        is_last_empty = False
        for i, chunk_section in enumerate(chunk.chunk_sections):
            if (not chunk_section.is_empty or not is_last_empty):
                chunk_section_mask |= 1 << i
                data += await ChunkSection.pack(chunk_section)
            is_last_empty = chunk_section.is_empty

        packed += await VarInt.encode(chunk_section_mask)

        for biome in chunk.biomes:
            data += await Byte.encode(biome)

        packed += await VarInt.encode(len(data))
        packed += data
        packed += await VarInt.encode(len(chunk.block_entities))
        for block_entity in chunk.block_entities:
            raise NotImplementedError
        
        return packed