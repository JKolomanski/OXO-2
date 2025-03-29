from random import choice


class Player:
    """Base class for players."""

    def __init__(self, symbol: str, parent, image):
        self.symbol = symbol
        self.parent = parent
        self.image = image


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
        self.parent.unlock_free_buttons()


class AiPlayer(Player):
    """Handles the computer player."""

    def turn(self):
        """
        Handles ai player move by choosing a random cell index from available

        # :param board; A Board object
        :returns: A string containing the move cell index
        """
        move = choice(self.parent.board.get_possible_moves())
        self.parent.handle_move(move)