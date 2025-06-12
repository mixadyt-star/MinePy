from typing import Dict
import asyncio

from ...common_types import *

class Packet:
    @staticmethod
    async def create(reader: asyncio.StreamReader, data_class: object, **kwargs: Dict[str, CommonType]):
        types: Dict[str, CommonType] = kwargs
        return data_class(**{key: await common_type.decode(reader) for key, common_type in types.items()})