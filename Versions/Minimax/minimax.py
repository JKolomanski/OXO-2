from board import Board
from copy import  deepcopy


class Node:
    """
    Represents a node in a decision tree for a tic-tac-toe game.

    Attributes:
        board: Board
            A Board object with its state attribute corresponding to the state that node represents
        children: list[Node]
            A list of all child nodes (for every possible future game state)
        score: int or None
            The score of the node, can be None if not evaluated yet
    """
    def __init__(self, board: Board):
        self.board = board
        self.children = []
        self.score = None

    def __str__(self):
        return (f'Node object\n'
                f'State: \n{str(self.board)}\n'
                f'Score: {self.score}\n'
                f'Total descendants: {self.count_children()}\n\n'
                f'Children states: \n{f'\n\n'.join(str(child.board) + f'\nScore: {child.score}' for child in self.children)}\n')

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

        if result == max_player: return 1
        elif result == 'FULL': return 0
        elif result == min_player: return -1
        else: return None

    def evaluate_minimax_score(self, functions: list, min_player, max_player):
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

    def get_possible_states(self, players: tuple[str]) -> None:
        """
        Get all the possible valid future stated of a game based on the state inside this Node object.
        Basically, generate a decision tree with node as the parent node

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
                    child_node = Node(new_board)
                    self.children.append(child_node)

        # Recursively evaluate for each child, while swapping players
        for child in self.children:
            child.get_possible_states((players[1], players[0]))


# Just for testing
temp_board = Board(([' ', ' ', ' '],
[' ', ' ', ' '],
[' ', ' ', ' ']))
root = Node(temp_board)
root.get_possible_states(('X', 'O'))

print(root.evaluate_minimax_score((max, min), 'O', 'X'))
print('rooooooot')
print(root)