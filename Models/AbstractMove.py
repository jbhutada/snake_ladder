from abc import ABC, abstractmethod


class AbstractMove(ABC):

    @abstractmethod
    def make_move(self):
        pass
