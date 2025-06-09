from ...storing import *

async def generate_eid(cache: Cache):
    o = cache.eid
    cache.eid += 1
    
    return o

async def generate_tp_id(cache: Cache):
    o = cache.tp_id
    cache.tp_id += 1

    return o