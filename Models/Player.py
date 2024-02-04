from constants import PlayerStatus


class Player:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.status = PlayerStatus.PLAYING
        self.stun_duration = 0
