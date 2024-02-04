from Models.AbstractMove import AbstractMove

class Mine(AbstractMove):
    def __init__(self, pos, stun_duration):
        self.pos = pos
        self.stun_duration = stun_duration

    def make_move(self):
        print(f"\t Stunned by Mine for next {self.stun_duration} moves.")
        return self.pos
