def validate_input(valid_inputs: tuple, user_input: str) -> bool:
    """Check if the given input exists in the list of valid inputs"""
    return user_input in valid_inputs if user_input else False


def get_user_input(valid_inputs: tuple, message: str) -> str:
    """
        Get an input from user, if it's not valid, ask again until correct string is given

        :param valid_inputs: A tuple of strings that contains all the correct inputs the user can make
        :param message: The message to ask the user for input
        :return: The input string from user
    """
    USER_INPUT = input(f'\n{message}\n> ').upper()
    return USER_INPUT if validate_input(valid_inputs, USER_INPUT) else get_user_input(valid_inputs, 'Invalid input! Please try again.')


def format_row(row: tuple) -> str:
    """Get a formatted board row, redy for displaying"""
    return f' {row[0]} ┃ {row[1]} ┃ {row[2]}'


def format_separator() -> str:
    """Get the board row separator"""
    return '\n━━━╋━━━╋━━━\n'


def display_board(board: tuple) -> None:
    """
        Display the whole board in a human-readable format

        :param board: The board state to be displayed
    """
    clear_console()
    ROWS = [format_row(row) for row in board]
    print(f'\n{format_separator().join(ROWS)}\n')


def display_ai_move(move: tuple) -> None:
    print(f'The computer is making it\'s move: {move}!')


def display_greeting_message() -> None:
    """clear the console and display the greeting message, ask for pressing Enter"""
    clear_console()
    input('☰☰☰ Welcome to OXO 2 ☰☰☰\nPress Enter to START')


def display_goodbye_message() -> None:
    """clear the console and display the ending message"""
    clear_console()
    print('Thank you for playing :)')


def get_turn_order(starting_player: str, human_player: str, player_turn, ai_turn) -> tuple:
    """Determine turn order"""
    if not human_player: return player_turn, player_turn

    FIRST_TURN = player_turn if human_player == starting_player  else ai_turn
    SECOND_TURN = ai_turn if FIRST_TURN == player_turn else player_turn

    return FIRST_TURN, SECOND_TURN


def main_menu(player_turn, ai_turn) -> tuple:
    """Gets game mode and player choices, returning turn order."""

    clear_console()
    GAMEMODE = get_user_input(('1', '2'), 'Please choose a gamemode:\n[1] Multiplayer\n[2] Singleplayer')

    HUMAN_PLAYER = get_user_input(('X', 'O'), 'Which would you like to play as? [X/O]') if GAMEMODE == '2' else None
    STARTING_PLAYER = get_user_input(('X', 'O'), 'Which player should start the game? [X/O]')

    clear_console()
    return STARTING_PLAYER, *get_turn_order(STARTING_PLAYER, HUMAN_PLAYER, player_turn, ai_turn)


def display_result(result: str) -> None:
    """
        Display the result of the game, returns nothing

        :param result: The result of the game (str)
    """
    if result == '=':
        print('It\'s a tie!')
    else:
        print(f'Player {result} won!')


def continue_playing() -> bool:
    """
        Get info from user whether the game should continue

        :return: Return True if it should, False if it shouldn't
    """
    USER_INPUT = get_user_input(('Y', 'N'), 'Do you want to play again? [Y/N]')
    return True if USER_INPUT == 'Y' else False


def clear_console():
    """Clear the console"""
    print("\033c", end="")