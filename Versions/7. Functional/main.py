"""
    OXO 2: Functional
    Loner edition wrtten following
    the functional programming paradigm
    uses some more advanced techniques
"""

from game_logic import *
from ui import *
from turns import *

    
def game(board: tuple, template: tuple, player: str, current_turn, next_turn) -> str:
    """
        Handle the game: display the board, check result and get to the next turn

        :param current_turn: a function that handles the current turn
        :param next_turn: a function that handles the next turn
        :return: return the result of the game when it has finished (str):

        '=' - tie;  'X' - player X won; 'O' - player O won
    """
    display_board(board)

    RESULT = check_result(board)
    return RESULT if RESULT else game(*current_turn(board, template, player), next_player(player), next_turn, current_turn)


def main():
    """
        Main loop for the whole program, uses recursion for looping
    """
    RESULT = game(generate_board(), generate_template(), *main_menu(player_turn, ai_turn))
    display_result(RESULT)

    if continue_playing():
        main()


if __name__ == '__main__':
    display_greeting_message()
    main()
    display_goodbye_message()