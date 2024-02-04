from Models.AbstractMove import AbstractMove


class Snake(AbstractMove):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def make_move(self):
        print(f"\t Bitten the snake from {self.start} to {self.end}")
        return self.end
