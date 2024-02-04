from Controller.AbstractGameController import GameController
from Models.Cell import Cell
from Models.Dice import Dice
from Models.Player import Player
from Models.Crocodile import Crocodile
from Models.Snake import Snake
from Models.Ladder import Ladder
from Models.Mine import Mine
from DiceStrategy.MaxDiceStrategy import MaxDiceStrategy
from DiceStrategy.MinDiceStrategy import MinDiceStrategy
from DiceStrategy.SumDiceStrategy import SumDiceStrategy
from collections import deque
from constants import SpecialChars, PlayerStatus


class GameController(GameController):
    def __init__(self, mode):
        self.mode = mode
        self.board = []
        self.dice_strategy = None
        self.no_of_dices = None
        self.dice = None
        self.player_to_position = {}
        self.playing_queue = deque()
        self.mine_stun_duration = None
        self.crocodile_length = None
        self.winners_sequence = []

    def add_players(self, num_of_players, players):
        for player_name, start_pos in players:
            player = Player(player_name, start_pos)
            self.player_to_position[player] = start_pos

    def add_board(self, size):
        for i in range(0, size * size + 1):
            self.board.append(Cell(i))

    def add_dice(self, no_of_dices, dice_range=[1, 6]):
        self.no_of_dices = no_of_dices
        self.dice = Dice(dice_range[0], dice_range[1])

    def set_mine_stun_duration(self, stun_duration):
        self.mine_stun_duration = stun_duration

    def set_crocodile_length(self, crocodile_length):
        self.crocodile_length = crocodile_length

    def add_strategy(self, strategy):
        match strategy:
            case "SUM":
                self.dice_strategy = SumDiceStrategy(self.dice, self.no_of_dices)
            case "MAX":
                self.dice_strategy = MaxDiceStrategy(self.dice, self.no_of_dices)
            case "MIN":
                self.dice_strategy = MinDiceStrategy(self.dice, self.no_of_dices)

    def add_special_object(self, type, pos):
        match type:
            case SpecialChars.Crocodile:
                self.board[pos].assign_special_object(
                    type, Crocodile(pos, pos - self.crocodile_length)
                )
            case SpecialChars.Snake:
                if pos[0] <= pos[1]:
                    raise Exception(f"Invalid Snake : {pos}")
                self.board[pos[0]].assign_special_object(type, Snake(*pos))
            case SpecialChars.Ladder:
                if pos[0] >= pos[1]:
                    raise Exception(
                        f"Invalid Ladder : {pos}",
                    )
                self.board[pos[0]].assign_special_object(type, Ladder(*pos))
            case SpecialChars.Mine:
                self.board[pos].assign_special_object(
                    type, Mine(pos, self.mine_stun_duration)
                )

    def make_move(self, curr_player, dice_value=None):
        curr_pos = curr_player.pos
        if curr_player.status == PlayerStatus.BLOCKED:
            return
        # Handle Stunned Player
        if curr_player.status == PlayerStatus.STUNNED:
            curr_player.stun_duration -= 1
            if curr_player.stun_duration == 0:
                curr_player.status = PlayerStatus.PLAYING
            return True

        if len(self.board) - 1 - curr_pos < self.dice_strategy.get_min_dice_possible():
            curr_player.status = PlayerStatus.BLOCKED
            print(
                f"{curr_player.name} is at {curr_player.pos} and cant roll a valid dice Throw!!"
            )
            return False

        # Throw Dice
        dice_throws = []
        if self.mode == "Manual":
            dice_throw = (
                input(f"Give inputs of {self.no_of_dices} Throws: ").strip().split(" ")
            )
            dice_throws = list(map(int, dice_throw))
        else:
            for i in range(self.no_of_dices):
                dice_throws.append(self.dice.roll())
        dice_value = (
            self.dice_strategy.get_dice_value(dice_throws)
            if dice_value is None
            else dice_value
        )

        # Handle invalid Move
        if curr_pos + dice_value > len(self.board) - 1:
            print(
                f"{curr_player.name} rolled {dice_value} at {curr_pos} and makes a Invalid Move"
            )
            return True

        # Make Dice Move
        new_pos = curr_pos + dice_value
        print(
            f"{curr_player.name} rolled {dice_value} at {curr_pos} and reached {new_pos}"
        )

        # Make Special Move
        if self.board[new_pos].special_object is not None:
            new_pos = self.board[new_pos].special_object.make_move()
            if self.board[new_pos].special_object_type == SpecialChars.Mine:
                curr_player.status = PlayerStatus.STUNNED
                curr_player.stun_duration = self.mine_stun_duration

        # Check if you knocked up someone

        for player in self.player_to_position:
            if player.pos == new_pos:
                print(
                    f"\t {player.name} got knocked out by {curr_player.name} and reaches to 1."
                )
                player.pos = 1
                player.status = PlayerStatus.PLAYING
        curr_player.pos = new_pos

        return True

    def start_game(self):
        for player in self.player_to_position:
            self.playing_queue.append(player)

        while self.playing_queue:
            curr_player = self.playing_queue.popleft()
            if (
                curr_player.status == PlayerStatus.PLAYING
                or curr_player.status == PlayerStatus.STUNNED
                or curr_player.status == PlayerStatus.BLOCKED
            ):
                self.make_move(curr_player)
                if curr_player.pos == len(self.board) - 1:
                    print(f"{curr_player.name} Completed !")
                    curr_player.pos = -1
                    self.winners_sequence.append(curr_player.name)
                else:
                    self.playing_queue.append(curr_player)

                # check if all blocked
                all_blocked = True
                for player in self.playing_queue:
                    if player.status != PlayerStatus.BLOCKED:
                        all_blocked = False

                if len(self.playing_queue) != 0 and all_blocked:
                    print("All Remaining Players are Blocked !, Game Ends")
                    break

        print("Game Ends !! ")
        print(f"Final Winner Sequence: {self.winners_sequence}")
