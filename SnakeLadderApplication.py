import json
import argparse
import sys
from Controller.GameController import GameController
from constants import SpecialChars


class SnakeLadderApp:
    def __init__(self, mode):
        self.game_controller = GameController(mode)

    def set_game_details(self, file_name):
        try:
            with open(file_name) as file:
                game_config = json.load(file)
        except Exception as E:
            raise E

        self.game_controller.add_board(game_config["Board Size"])
        self.game_controller.add_dice(game_config["Number of Dies"])
        self.game_controller.add_strategy(game_config["Movement Strategy"])

        # Add Snakes
        snakes = game_config["Snakes Positions"]
        for snake_pos in snakes:
            self.game_controller.add_special_object(SpecialChars.Snake, snake_pos)

        # Add Ladders
        ladders = game_config["Ladder Positions"]
        for ladder_pos in ladders:
            self.game_controller.add_special_object(SpecialChars.Ladder, ladder_pos)

        # Add Mines
        mines = game_config["Mine Positions"]
        self.game_controller.set_mine_stun_duration(game_config["Mine Duration"])
        for mine_pos in mines:
            self.game_controller.add_special_object(SpecialChars.Mine, mine_pos)

        # Add Crocodiles
        crocodile = game_config["Crocodile Positions"]
        self.game_controller.set_crocodile_length(game_config["Crocodile Length"])
        for crocodile_pos in crocodile:
            self.game_controller.add_special_object(
                SpecialChars.Crocodile, crocodile_pos
            )

        # Add Players
        if self.game_controller.mode == "Manual":
            num_of_players = input("Enter the num of players to play: ")
            player_names = []
            for i in range(int(num_of_players)):
                name, pos = input("Enter Player Name and Pos: ").split(" ")
                player_names.append([name, int(pos)])
            self.game_controller.add_players(num_of_players, player_names)
        else:
            self.game_controller.add_players(
                game_config["Number of players"], game_config["Player Names"]
            )

    def start_game(self):

        self.game_controller.start_game()
        return "Success"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse Mode and File Name")
    parser.add_argument("--mode", type=str, default="Automatic")
    parser.add_argument("--file_name", type=str, default="input.json")
    args = parser.parse_args()
    app = SnakeLadderApp(args.mode)
    app.set_game_details(args.file_name)
    app.start_game()
