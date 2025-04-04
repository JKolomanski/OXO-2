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
        self.score = self.evaluate_score('O', 'X')

    def __str__(self):
        return (f'Node object\n'
                f'State: \n{'\n'.join(str(row) for row in self.board.state)}\n'
                f'Score: {self.score}\n'
                f'Total descendants: {self.count_children()}\n\n'
                f'Children states: \n{f'\n\n'.join(f'\n'.join(str(row) for row in child.board.state) + f'\nScore: {child.score}' for child in self.children)}\n')

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


def get_possible_states(parent_node: Node, players: tuple[str]) -> None:
    """
    Get all the possible valid future stated of a game based on the state given inside a Node object.
    Basically, generate a decision tree inside the parent node given

    :param parent_node: The parent node to be modified
    :param players: The list of players in the game (in correct order)
    """
    # Stop if terminal state
    if parent_node.board.get_result():
        return

    for i, row in enumerate(parent_node.board.state):
        for j, cell in enumerate(row):
            if cell == ' ':
                new_state = deepcopy(parent_node.board.state)
                new_state[i][j] = players[0]
                new_board = Board(new_state)
                child_node = Node(new_board)
                parent_node.children.append(child_node)

    # Recursively evaluate for each child, while swapping players
    for child in parent_node.children:
        get_possible_states(child, (players[1], players[0]))


temp_board = Board(([' ', ' ', ' '],[ ' ', ' ', ' '], [' ', ' ', ' ']))
root = Node(temp_board)
get_possible_states(root, ('X', 'O'))

print(root)