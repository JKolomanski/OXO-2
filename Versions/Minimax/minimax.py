from board import Board
from copy import  deepcopy
from functools import total_ordering


@total_ordering
class MiniMaxNode:
    """
    Represents a node in a decision tree for a tic-tac-toe game.

    Attributes:
        board: Board
            A Board object with its state attribute corresponding to the state that this node represents
        children: list[Node]
            A list of all child nodes (for every possible future game state)
        score: int or None
            The score of the node, can be None if not evaluated yet
    """
    def __init__(self, board: Board):
        self.board = board
        self.children = []
        self.score = None
        self.preceding_move = None

    def __str__(self):
        return (f'Node object\n'
                f'Preceding move: {self.preceding_move}\n'
                f'State: \n{str(self.board)}\n'
                f'Score: {self.score}\n'
                f'Total descendants: {self.count_children()}\n\n'
                f'Children states: \n{f'\n\n'.join(str(child.board) + f'\nScore: {child.score}' + f'\nPreceding_move: {child.preceding_move}' for child in self.children)}\n')

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score

    def count_children(self):
        """Count the number of all descendants of this node (children + children of children...)"""
        count = len(self.children)

        for child in self.children:
            count += child.count_children()
        return count

    def evaluate_score(self, min_player: str, max_player: str) -> int | None:
        """
        Evaluate score for the minimax algorithm based and current board state

        :param min_player: The symbol for the min player
        :param max_player: The symbol for the max player
        :returns: int from -1 to 1 based on result or None if the state isn't terminal
        """
        result = self.board.get_result()
        modifier = 0
        if self.board.state[1][1] == max_player: modifier += 1
        if self.board.state[1][1] == min_player: modifier -= 1

        if result == max_player: return 1 + modifier
        elif result == 'FULL': return 0
        elif result == min_player: return -1 + modifier
        else: return None

    def evaluate_minimax_score(self, functions: list, min_player: str, max_player: str) -> int | None:
        """
        Recursively evaluate the minmax score for this node based on scores of all descendants

        :param functions: a list of two min and max functions in the order in which players take turns
        :param min_player: The symbol for the min player
        :param max_player: The symbol for the max player
        :returns: int with a value of -1, 0 or 1
        """
        self.score = self.evaluate_score(min_player, max_player)
        if self.score is not None: return self.score

        children_scores = []
        for child in self.children:
            children_scores.append(child.evaluate_minimax_score((functions[1], functions[0]), min_player, max_player))

        if not children_scores:
            self.score = 0
        else:
            self.score = functions[0](children_scores)

        return self.score

    def get_move(self, row_index: int, cell_index:int) -> str:
        """
        Get the cell number from list indexes

        :param row_index: The index of the row the cell is in
        :param cell_index: Index of the specific cell in that row
        :returns: The move number corresponding to that cell
        """
        return self.board.template[row_index][cell_index]

    def expand(self, players: tuple[str]) -> None:
        """
        Add all the possible valid future descendants, based on the state inside this Node object,
        to the children attribute recursively
        Basically, generate a decision tree with parent node as this parent node

        :param players: The list of players in the game (in correct order)
        """
        # Stop if terminal state
        if self.board.get_result():
            return

        for i, row in enumerate(self.board.state):
            for j, cell in enumerate(row):
                if cell == ' ':
                    new_state = deepcopy(self.board.state)
                    new_state[i][j] = players[0]
                    new_board = Board(new_state)
                    child_node = MiniMaxNode(new_board)
                    child_node.preceding_move = child_node.get_move(i, j)
                    self.children.append(child_node)

        # Recursively evaluate for each child, while swapping players
        for child in self.children:
            child.expand((players[1], players[0]))