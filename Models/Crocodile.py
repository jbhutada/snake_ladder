from Models.AbstractMove import AbstractMove


class Crocodile(AbstractMove):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def make_move(self):
        print(f"\t Eaten by crocodile from {self.start} to {self.end}")
        return self.end
