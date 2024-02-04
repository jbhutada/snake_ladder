from abc import ABC, abstractmethod


class DiceStrategy(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_dice_value(self, dice_throws):
        pass

    @abstractmethod
    def get_min_dice_possible(self):
        pass
