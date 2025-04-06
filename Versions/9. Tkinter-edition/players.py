from random import choice
from MiniMaxNode import MiniMaxNode


class Player:
    """Base class for players."""

    def __init__(self, symbol: str, board_symbol: str, color:str, parent, image):
        self.symbol = symbol
        self.board_symbol = board_symbol
        self.color = color
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


class MiniMaxPlayer(Player):
    def turn(self):
        root_node = MiniMaxNode(self.parent.board)
        root_node.expand((self.board_symbol, f'{'A' if self.board_symbol == 'B' else 'B'}'))
        root_node.evaluate_minimax_score((max, min),f'{'A' if self.board_symbol == 'B' else 'B'}', self.board_symbol)
        print(root_node)
        best_node = max(root_node.children)

        self.parent.handle_move(best_node.preceding_move)