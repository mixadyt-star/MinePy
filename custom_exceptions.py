class PlayerAlreadyOnline(Exception):
    def __init__(self):
        super().__init__("Player already online")