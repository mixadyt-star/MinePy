from typing import Dict
import asyncio
import pickle
import os

from .remote import Remote
from .player import Player

class StreamWriter:
    def __init__(self, writer: asyncio.StreamWriter):
        self.writer = writer

    def __hash__(self):
        return hash(self.writer.get_extra_info("peername"))
    
    def __eq__(self, other):
        return self.writer.get_extra_info("peername") == other.writer.get_extra_info("peername")

class Cache:
    def __init__(self):
        self.world_ticks = 0
        self.eid = 0
        self.tp_id = 0
        self.online = 0
        self.keep_alive_list: Dict[StreamWriter, int] = {}
        self.remote: Dict[Remote, int] = {}
        self.players: Dict[str, Player] = {}

def load() -> Cache:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(os.path.dirname(current_dir), "cache.minepy")
    return pickle.load(open(file_path, "rb")) if os.path.exists(file_path) else Cache()

def store(cache: Cache):
    cache.online = 0
    cache.tp_id = 0
    cache.remote = {}
    cache.keep_alive_list = {}
    for _, player in cache.players.items():
        player.online = False
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(os.path.dirname(current_dir), "cache.minepy")
    pickle.dump(cache, open(file_path, "wb"), pickle.HIGHEST_PROTOCOL)