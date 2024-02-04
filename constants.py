from enum import Enum


class PlayerStatus(Enum):
    PLAYING = ("Playing",)
    WON = ("Won",)
    STUNNED = ("Stunned",)
    LOST = ("Lost",)
    BLOCKED = "Blocked"


class SpecialChars(Enum):
    Snake = ("Snake",)
    Ladder = ("Ladder",)
    Crocodile = ("Crocodile",)
    Mine = "Mine"
