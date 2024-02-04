from Models.AbstractMove import AbstractMove


class Ladder(AbstractMove):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def make_move(self):
        print(f"\t Climbed the ladder from {self.start} to {self.end}")
        return self.end
