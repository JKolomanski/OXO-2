from itertools import chain


def generate_template() -> tuple:
    """Get the base board template"""
    return ('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9')


def generate_board() -> tuple:
    """Get an empty board"""
    return (' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' ')


def check_row(row: tuple) -> str | None:
    """Check if a row has been filled with the same symbol"""
    return row[0] if all(cell == row[0] for cell in row) and row[0] != ' ' else None


def check_col(board: tuple, col_index: int) -> str | None:
    """Check if a column has been filled with the same symbol"""
    return board[0][col_index] if all(row[col_index] == board[0][col_index] for row in board) and board[0][col_index] != ' ' else None


def check_rows_and_cols(board: tuple, i: int = 0) -> str | None:
    """Check if any row or column has been filled with the same symbol"""
    if i >= len(board): 
        return None

    row_winner = check_row(board[i])
    col_winner = check_col(board, i)

    return row_winner or col_winner or check_rows_and_cols(board, i + 1) # Returns the first truthy value


def check_diag(board: tuple) -> str | None:
    """Check if any diagonal has been filled with the same symbol"""
    if board[1][1] != ' ' and (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
        return board[1][1]
    
    return None


def check_full(board: tuple) -> str | None:
    """Check if the board has been filled completely"""
    return '=' if all(cell != ' ' for cell in flatten(board)) else None


def check_result(board: tuple) -> str:
    """Check if the game has finished, return the information about the game result. Return None otherwise"""
    return check_full(board) or check_rows_and_cols(board) or check_diag(board)


def flatten(tup: tuple[tuple]) -> tuple:
    """
        Flattens a tuple of nested tuples into a single tuple
        :param tup: A 2-dimensional tuple
        :return: The flattened tuple
    """
    return tuple(chain(*tup))


def get_coordinates(move: str, template: tuple, i: int = 0) -> tuple:
    """
        search for the row and column indices of the specified 
        cell number within the provided board template.

        :param move: The number string corresponding to the cell
        :param template: The board template containing cell numbers
        :param i: The current row index being checked (default is 0), used for recursion
        :return: A tuple (row_index, col_index) representing the coordinates
    """
    try: 
        return (i, template[i].index(move))
    
    except ValueError: 
        return get_coordinates(move, template, i+1)


def update_state(coords: tuple[int], board_type: tuple, cell_value: str) -> tuple:   
    """
        Returns a modified board/template.

        :param coords: The coordinates of the cell to be changed (tuple[int] with 2 elements)
        :param board_type: The board to be modified
        :param cell_value: The value to replace the cell with
        :return: The modified tuple
    """
    ROW, COL = coords

    return tuple(
    tuple(cell_value if (r, c) == (ROW, COL) else cell for c, cell in enumerate(row_data))
    for r, row_data in enumerate(board_type)
    )


def next_player(player: str) -> str:
    """
        Return the next player based on the current one

        :param player: The current player
        :return: The next player
    """
    return 'O' if player == 'X' else 'X'
