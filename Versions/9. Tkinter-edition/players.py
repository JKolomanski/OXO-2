from random import choice
from MiniMaxNode import MiniMaxNode
import time



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

    def get_enemy_symbol(self):
        """Get the symbol of the opposite player"""
        return 'A' if self.board_symbol == 'B' else 'B'


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
    """Handles the random computer player."""

    def turn(self):
        """Handles AI player move by choosing a random cell index from available"""
        move = choice(self.parent.board.get_possible_moves())
        self.parent.handle_move(move)


class MiniMaxPlayer(Player):
    """Handles a computer player making choices with the minimax algorithm"""
    def turn(self):
        """Handles the turn for a minimax player"""
        enemy_symbol = self.get_enemy_symbol()
        root_node = MiniMaxNode(self.parent.board)
        start_time = time.perf_counter()
        root_node.expand((self.board_symbol, enemy_symbol))
        end_time = time.perf_counter()
        print(f'time to expand: {end_time - start_time:3f} seconds')
        start_time = time.perf_counter()
        root_node.evaluate_minimax_score((max, min), enemy_symbol, self.board_symbol)
        end_time = time.perf_counter()
        print(f'time to evaluate: {end_time - start_time:3f} seconds')
        all_best_nodes = [node for node in root_node.children if node.score == max(root_node.children).score]
        chosen_node = choice(all_best_nodes)

        self.parent.handle_move(chosen_node.preceding_move)