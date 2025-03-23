#!/usr/bin/env python3

"""
    OXO 2: Object-oriented
    Loner edition written following
    the object-oriented programming paradigm
    uses some more advanced techniques
"""

from board import Board
from ui import Ui
from players import HumanPlayer, AiPlayer, Player
from app import App


class Game:
    """Handles game logic and main game loop"""

    def __init__(self):
        self.result = None
        self.board = Board()

        Ui.display_greeting_message()

    def main_menu(self):
        """
        Handles the main menu and returns the players that should be in the game

        :returns: A pair of Player objects with appropriate subclasses, where first one is the starting one
        """
        self.result = None
        self.board = Board()
        starting_player, human_player = Ui.main_menu()

        players = ['X', 'O']
        players.remove(starting_player)
        second_player = players[0]

        if human_player and human_player == starting_player:
            player_1 = HumanPlayer(starting_player)
            player_2 = AiPlayer(second_player)

        elif human_player:
            player_1 = AiPlayer(starting_player)
            player_2 = HumanPlayer(second_player)

        else:
            player_1 = HumanPlayer(starting_player)
            player_2 = HumanPlayer(second_player)

        return player_1, player_2

    def turn(self, player: Player) -> None:
        """
        Handles the turn of one player

        :param player: The player instance for current player
        """
        self.board.update(player.make_move(self.board), player.symbol)
        Ui.clear_console()
        print(self.board)
        self.result =  self.board.get_result()

    def end_game(self) -> bool | None:
        """
        Handles the end of the game and asks the user to play again.

        :returns: True if the  user wants to quit, None otherwise
        """
        Ui.display_result_message(self.result)

        continue_playing = Ui.get_user_input(('1', '2'), 'Would you like to play again?\n'
                                          ' [1] play again\n'
                                          ' [2] quit')

        if continue_playing != '1':
            Ui.display_goodbye_message()
            return True

    def play(self) -> None:
        """Handles the main program loop"""
        while True:
            player_1, player_2 = self.main_menu()
            print(self.board)

            while True:
                self.turn(player_1)
                if self.result: break

                self.turn(player_2)
                if self.result: break

            if self.end_game(): break


if __name__ == '__main__':
    app = App()
    app.mainloop()