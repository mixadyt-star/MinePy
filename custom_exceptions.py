class PlayerAlreadyOnline(Exception):
    def __init__(self):
        super().__init__("Player already online")

class ServerIsFull(Exception):
    def __init__(self):
        super().__init__("Server is full")