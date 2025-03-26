from random import choice


class Player:
    """Base class for players."""

    def __init__(self, symbol: str, parent):
        self.symbol = symbol
        self.parent = parent


    def turn(self):
        """To be implemented by subclasses"""
        return None


class HumanPlayer(Player):
    """Handles the human player."""

    def turn(self) -> None:
        """
        Handles human player move by getting user's input

        # :param board; A Board object
        :returns: A string containing the move cell index
        """
        # self.parent.unlock_board_buttons()


class AiPlayer(Player):
    """Handles the computer player."""

    def turn(self):
        """
        Handles ai player move by choosing a random cell index from available

        # :param board; A Board object
        :returns: A string containing the move cell index
        """
        # self.parent.lock_board_buttons()
        self.make_move()

    def make_move(self):
        move = choice(self.parent.board.get_possible_moves())
        self.parent.make_move(move)
