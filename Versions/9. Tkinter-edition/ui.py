from os import  system, name


class Ui:
    """A static class tha handles user interface and user interaction"""

    @staticmethod
    def clear_console() -> None:
        """Clears the console screen"""
        system("cls" if name == "nt" else "clear")

    @staticmethod
    def display_greeting_message() -> None:
        """Clears the console and displays the greeting message, prompting the user to pressing Enter"""
        Ui.clear_console()
        input('☰☰☰ Welcome to OXO 2 ☰☰☰\nPress Enter to START')

    @staticmethod
    def display_ai_move_message(symbol, move) -> None:
        """Displays the information about ai player making a move"""
        print(f'\nComputer player {symbol} made it\'s move: {move}')

    @staticmethod
    def display_result_message(result) -> None:
        """Displays what the result of the game is"""
        if result != 'FULL': print(f'\nPlayer {result} won!')
        else: print('\nIt\'s a tie!')

    @staticmethod
    def display_goodbye_message() -> None:
        """Clears the console and displays a goodbye message"""
        Ui.clear_console()
        print('Thank you for playing :)')

    @staticmethod
    def validate_input(valid_inputs: tuple[str], user_input: str) -> bool:
        """Checks if the given input exists in the list of valid inputs"""
        return user_input in valid_inputs if user_input else False

    @staticmethod
    def get_user_input(valid_inputs: tuple[str], prompt: str) -> str | None:
        """
        Continuously prompts the user for input until a valid string is provided.

        :param valid_inputs: A tuple of strings that contains all the correct inputs the user can make
        :param prompt: The message to ask the user for input
        :return: The valid input string provided by the user
        """
        print(f'\n{prompt}')
        while True:
            user_input = input('> ').upper()
            if Ui.validate_input(valid_inputs, user_input):
                return user_input
            print('Invalid input! Please try again.')

    @staticmethod
    def main_menu() -> tuple[str]:
        """
        Gets all the necessary info from user for the game

        :returns: Returns a tuple where the first element is the symbol of the starting player,
        and the second is the symbol of human player if the user chose singleplayer gamemode, or None otherwise
        """

        human_player = None
        Ui.clear_console()
        gamemode = Ui.get_user_input(('1', '2'), 'Please choose a gamemode, type:\n'
                                                 '  [1] for multiplayer\n'
                                                 '  [2] for singleplayer')

        if gamemode == '2':
            human_player = Ui.get_user_input(('X', 'O'), 'Which would you like to play as?\n'
                                          ' [X] to play as player X\n'
                                          ' [O] to play as player O')

        starting_player = Ui.get_user_input(('X', 'O'), 'Which player should start the game?\n'
                                          ' [X] for X to start\n'
                                          ' [O] for O to start')

        Ui.clear_console()
        return starting_player, human_player


