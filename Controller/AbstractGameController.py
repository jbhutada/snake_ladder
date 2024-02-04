from abc import ABC, abstractmethod


class GameController(ABC):
    @abstractmethod
    def add_players(num_of_players, players):
        pass

    @abstractmethod
    def add_board(size):
        pass

    @abstractmethod
    def add_dice(num_of_dices):
        pass

    @abstractmethod
    def add_strategy(strategy):
        pass

    @abstractmethod
    def add_special_object(start, end, type):
        pass

    # start game
