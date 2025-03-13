from random import choice
from time import sleep

from board import Board
from ui import Ui


class Player:
    """Base class for players."""

    def __init__(self, symbol: str):
        self.symbol = symbol


    def make_move(self, board: Board):
        """To be implemented by subclasses"""
        return None


class HumanPlayer(Player):
    """Handles the human player."""

    def make_move(self, board: Board) -> str:
        """
        Handles human player move by getting user's input

        :param board; A Board object
        :returns: A string containing the move cell index
        """
        return Ui.get_user_input(board.get_possible_moves(), f'Player {self.symbol}, make your move!')


class AiPlayer(Player):
    """Handles the computer player."""

    def make_move(self, board: Board) -> list[str]:
        """
        Handles ai player move by choosing a random cell index from available

        :param board; A Board object
        :returns: A string containing the move cell index
        """
        move = choice(board.get_possible_moves())
        Ui.display_ai_move_message(self.symbol, move)
        sleep(1)
        return move