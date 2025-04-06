from itertools import chain


class Board:
    """
    Represents a tic-tac-toe board.

    Attributes:
        state (list[list[str]]): A list of 3 lists, where each nested list is a row,
            which has 3 str elements which represent cells. All of them are equal to ' ' by default.
            Used to store boards state

        template (list[list[str]]): Similar to state, but used to store the cells positions.
            If a cell has been occupied, it's position is replaced with '' to represent that it has been taken
    """

    def __init__(self, base_state=([' ', ' ', ' '],[ ' ', ' ', ' '], [' ', ' ', ' '])) -> None:
        self.state = list(base_state)
        self.template = [['1', '2', '3'],
                         ['4', '5', '6'],
                         ['7', '8', '9']]

    def get_possible_moves(self) -> list[str]:
        """
        Returns a list of all possible moves based on the current template

        :return: The list of all moves
        """
        flattened_template = tuple(chain(*self.template))
        return [cell for cell in flattened_template if cell != '']

    def format_board(self) -> str:
        """
        Helper method to format the board into a human-readable string.

        :return: The formatted board as string.
        """

        divider = '━━━╋━━━╋━━━'
        rows = [' ' +  ' ┃ '.join(row) for row in self.state]
        return f'\n{divider}\n'.join(rows)

    def __str__(self) -> str:
        """Returns the current board state as a formatted string."""
        return self.format_board()

    def update(self, move: str, symbol: str) -> None:
        """
        Updates the board state with the player's move.

        :param move: The move position (1-9) as str.
        :param symbol: Player's symbol (Should be eiter 'X' or 'O').
        """
        for row, row_data in enumerate(self.template):
            for col, cell in enumerate(row_data):
                if cell == move:
                    self.state[row][col] = symbol
                    self.template[row][col] = '' # Mark cell as occupied
                    return

    @staticmethod
    def check_row(row_i: int, board: list[list[str]]) -> str | None:
        """
        Helper method to check if a whole row is filled with the same symbol.

        :param row_i: index of the row to be checked
        :param board: The board state to be checked
        :return: Returns the winning symbol if it's been found or None
        """
        first_cell = board[row_i][0] # A reference cell to compare all the other ones to
        return first_cell if first_cell != ' ' and all(cell == first_cell for cell in board[row_i]) else None

    @staticmethod
    def check_col(col_i: int, board: list[list[str]]) -> str | None:
        """
        Helper method to check if a whole column is filled with the same symbol.

        :param col_i: index of the column to be checked
        :param board: The board state to be checked
        :return: Returns the winning symbol if it's been found or None
        """
        first_cell = board[0][col_i]  # A reference cell to compare all the other ones to
        return first_cell if first_cell != ' ' and all(row[col_i] == first_cell for row in board)else None

    @staticmethod
    def check_diag(board: list[list[str]]) -> str | None:
        """
        Helper method to check if any diagonal is filled with the same symbol.

        :param board: The board state to be checked
        :return: Returns the winning symbol if it's been found or None
        """
        center_cell = board[1][1]  # A reference cell to compare all the other ones to

        if center_cell == ' ': # No need to do further checks if the center is empty
            return None

        diag1_result = board[0][0] == center_cell and board[2][2] == center_cell
        diag2_result = board[0][2] == center_cell and board[2][0] == center_cell

        return center_cell if diag1_result or diag2_result else None

    @staticmethod
    def check_full(board: list[list[str]]) -> str | None:
        """
        Helper method to check if the board is full.

        :param board: The board state to be checked
        :return: Returns 'FULL' if the board is empty and None otherwise
        """
        return 'FULL' if all(cell != ' ' for row in board for cell in row)else None

    def get_result(self) -> str | None:
        """
        Return the result of the board depending on its current state.

        :return: 'X' if player X won,
                 'O' if player O won,
                 'FULL' if the board is full, and it's a tie,
                  None if there is no final result yet
        """
        if winner := self.check_diag(self.state):
            return winner

        for i in range(len(self.state)):
            winner =  self.check_row(i, self.state) or self.check_col(i, self.state)
            if winner: return winner

        return self.check_full(self.state)