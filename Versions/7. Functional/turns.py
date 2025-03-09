from random import choice
from time import sleep

from game_logic import get_coordinates, update_state, flatten
from ui import get_user_input, display_ai_move


def player_turn(board: tuple, template: tuple, player: str) -> str:
    """
        Handle player's turn. Get input and return the new state of the board

        :param board: The board to be modified
        :param template: The template of available moves
        :param player: The symbol of the current player
    """
    COORDS = get_coordinates(get_user_input(flatten(template), f'Player {player}, make your move!'), template)

    return update_state(COORDS, board, player), update_state(COORDS, template, '')


def ai_turn(board: tuple, template: tuple, player: str) -> str:
    """
        Handle computer's turn. Get the move and return the new state of the board

        :param board: The board to be modified
        :param template: The template of available moves
        :param player: The symbol of the current player
    """
    MOVE = choice(tuple(filter(bool, flatten(template))))
    COORDS = get_coordinates(choice(MOVE), template)

    display_ai_move(MOVE)
    sleep(1.5)
    return update_state(COORDS, board, player), update_state(COORDS, template, '')