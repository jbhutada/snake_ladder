import random


class Dice:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def roll(self):
        return random.choice(list(range(self.min, self.max + 1)))
