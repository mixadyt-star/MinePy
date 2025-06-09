from ..static import *
from ..static import *
from .. import config

class Player:
    def __init__(self, username: str, uuid: str):
        self.username = username
        self.uuid = uuid
        self.eid = None
        self.display_name = None
        self.gamemode = SURVIVAL
        self.dimension = OVERWORLD
        self.online = False
        self.invulnerable = False
        self.flying = False
        self.allow_flying = False
        self.instant_crash = False
        self.slot = 0
        self.locale = None
        self.view_distance = None
        self.chat_mode = None
        self.chat_colors = None
        self.displayed_skin_parts = None
        self.main_hand = None
        self.position = (0, config.SEA_LEVEL + 2, 0)
        self.rotation = (0, 0)