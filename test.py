import unittest

from SnakeLadderApplication import SnakeLadderApp
from Models.Snake import Snake
from constants import SpecialChars


class TestCases(unittest.TestCase):

    def initialize_board(self):
        self.app = SnakeLadderApp("Automatic")
        self.app.set_game_details("input.json")

    def test_initialize_board(self):
        self.initialize_board()

    def test_invalid_snake(self):
        self.initialize_board()
        snake_pos = [10, 11]
        with self.assertRaises(Exception) as context:
            self.app.game_controller.add_special_object(SpecialChars.Snake, snake_pos)
        self.assertEqual(str(context.exception), "Invalid Snake : {}".format(snake_pos))

    def test_invalid_ladder(self):
        self.initialize_board()
        ladder_pos = [11, 10]
        with self.assertRaises(Exception) as context:
            self.app.game_controller.add_special_object(SpecialChars.Ladder, ladder_pos)
        self.assertEqual(
            str(context.exception), "Invalid Ladder : {}".format(ladder_pos)
        )

    def test_normal_move(self):
        self.initialize_board()
        player = list(self.app.game_controller.player_to_position.keys())[0]
        self.app.game_controller.make_move(player, 3)
        self.assertEqual(player.pos, 4)

    def test_ladder_move(self):
        self.initialize_board()
        player = list(self.app.game_controller.player_to_position.keys())[0]
        self.app.game_controller.make_move(player, 1)
        self.assertEqual(player.pos, 37)


if __name__ == "__main__":
    unittest.main()
