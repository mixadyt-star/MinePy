from ..logger import *
from .. import config
set_verbosity_level(config.VERBOSITY_LEVEL)

from asyncio import sleep
import random
import time

from ..networking.server import *
from ..storing import *

cache: Cache = None

async def run():
    global cache

    while (True):
        now = time.time()
        for writer, last_keep in cache.keep_alive_list.items():
            if (now - last_keep >= 10):
                writer.writer.write(await KeepAlive.create(
                    random.randint(0, 18446744073709551615),
                ))
                log(f"Keep alive to {writer.writer.get_extra_info("peername")[0]}:{writer.writer.get_extra_info("peername")[1]} sent", 2)
                cache.keep_alive_list[writer] = now
                
        await sleep(10)

async def tick(cache: Cache):
    cache.world_ticks += 1