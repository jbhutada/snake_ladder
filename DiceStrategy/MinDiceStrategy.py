from DiceStrategy.AbstractDiceStrategy import DiceStrategy


class MinDiceStrategy(DiceStrategy):
    def __init__(self, dice, num_of_dices):
        self.dice = dice
        self.num_of_dices = num_of_dices

    def get_dice_value(self, dice_throws):
        return min(dice_throws)

    def get_min_dice_possible(self):
        return self.dice.min
