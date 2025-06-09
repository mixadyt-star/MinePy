from asyncio import sleep
import time

from ..storing import *

cache: Cache = None

async def run():
    global cache

    while (True):
        now = time.time()
        await tick(cache)
        end = time.time()
        if (0.05 - end + now > 0):
            await sleep(0.05 - end + now)

async def tick(cache: Cache):
    cache.world_ticks += 1