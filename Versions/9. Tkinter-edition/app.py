# import tkinter as tk
import webbrowser
from random import choice

from players import HumanPlayer, AiPlayer
from board import Board
from ui_elements import *


class App(ctk.CTk):
    """
    Main application class for the whole game
    initializes the main menu, frames and bottom text
    """
    def __init__(self):
        super().__init__(fg_color=settings['bg_color'])
        self.geometry(f'{settings["window_width"]}x{settings["window_height"]}')
        ctk.set_appearance_mode("light")
        self.resizable(False, False)
        self.title(f'OXO{self.get_random_splash()}')

        # Initialize all ui components

        self.game_active = False
        self.logo = OXOLogo(self, 359, 93)
        self.about_frame = AboutFrame(parent=self)
        self.settings_frame = SettingsFrame(parent=self)
        self.game_creation_frame = GameCreationFrame(parent=self)
        self.play_frame = PlayFrame(parent=self)
        self.main_menu_frame = MainMenuFrame(parent=self)
        self.main_menu_frame.pack_propagate(False)

        # Bottom text (link to website)
        self.bottom_text = ctk.CTkButton(self,
                                         text='Jakub Kołomański |  MMXXV',
                                         fg_color=settings['bg_color'],
                                         hover_color=settings['bg_color'],
                                         width=160,
                                         height=20,
                                         text_color=settings['gray'],
                                         font=(settings['font'], 13),
                                         command=lambda: webbrowser.open('https://jkolomanski.github.io/'))

        self.bottom_text.bind("<Enter>", lambda event: self.bottom_text.configure(font=(settings['font'], 13, 'underline')))
        self.bottom_text.bind("<Leave>", lambda event: self.bottom_text.configure(font=(settings['font'], 13)))
        self.bottom_text.pack(side='bottom', pady=(0, 5))

    @ staticmethod
    def get_random_splash() -> str:
        """
        Load the splashes.txt file and return a random line

        :return: a randomly chosen line with the end-line character stripped (str)
        """
        with open('splashes.txt') as f:
            splashes = f.readlines()
            return choice(splashes).strip('\n')



class MainMenuFrame(AppFrame):
    """Main menu screen containing navigation buttons"""
    def __init__(self, parent):
        self.parent = parent
        self.button_size = [160, 42]
        super().__init__(self.parent)

        # Initialise buttons for different sections
        self.play_button = Button(self.button_frame, 'Play', self.button_size,
                                  command=lambda: self.change_frame(parent.game_creation_frame) if not self.parent.game_active else self.change_frame(parent.play_frame))
        self.settings_button = Button(self.button_frame, 'Settings', self.button_size, command=lambda: self.change_frame(parent.settings_frame))
        self.about_button = Button(self.button_frame, 'About', self.button_size, command=lambda: self.change_frame(parent.about_frame))
        self.quit_button = Button(self.button_frame, 'Quit', self.button_size, command=self.parent.destroy)

        self.button_frame.pack(pady=(20, 0))
        self.pack(expand=True, fill="both", pady=(5, 5), padx=(5, 5))


class AboutFrame(AppFrame):
    """Contains the info about the game and links to GitHub repository"""
    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent)

        self.back_button = BackButton(self)
        self.button_frame.pack(side='bottom', pady=(0, 5))
        self.title_label = ctk.CTkLabel(self,
                                        text='=== Welcome to OXO 2: tkinter edition ===',
                                        font=(settings['font'], 16, 'bold'),
                                        text_color=settings['dark_bg_color'])
        self.text_label = ctk.CTkLabel(self,
                                        text='OXO 2: tkinter edition is a simple tic-tac-toe game '
                                             'written in python with tkinter. '
                                             'It\'s just one of many different versions of this simple game. '
                                             'The source code for it and all the other ones can be found here:',
                                        font=(settings['font'], 14),
                                        text_color=settings['dark_bg_color'],
                                        width=settings['window_height'] - 90,
                                        pady=20,
                                        justify='left',
                                        wraplength=300)
        self.github_button = Button(self,
                                    'GitHub Page',
                                    [160, 42],
                                    command=lambda: webbrowser.open('https://github.com/JKolomanski/OXO-2'))

        self.title_label.pack()
        self.text_label.pack()
        self.github_button.pack(side='bottom', pady=(0, 150))


class SettingsFrame(AppFrame):
    """Contains the settings menu"""
    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent)

        self.back_button = BackButton(self)
        self.button_frame.pack(side='bottom', pady=(0, 5))
        self.title_label = ctk.CTkLabel(self, text='work in progress')
        self.title_label.pack()


class PlayerSettingsFrame(ctk.CTkFrame):
    def __init__(self, parent, player: str):
        self.parent = parent
        self.player = player
        if player == '1':
            self.symbols = ['X', 'O']
            self.colors = ['orange', 'blue', 'green',
                           'yellow', 'red', 'purple']
        else:
            self.symbols = ['O', 'X']
            self.colors = ['blue', 'orange', 'green',
                           'yellow', 'red', 'purple']

        super().__init__(self.parent, fg_color=settings['bg_color'])


        self.label = ctk.CTkLabel(self,
                                        text=f'    Player {self.player}    ',
                                        font=(settings['font'], 16, 'bold', 'underline'),
                                        text_color=settings['dark_bg_color'])
        self.label.pack()

        self.symbol_label = ButtonTypeLabel(self, 'Symbol')
        self.symbol_combobox = ComboBox(self, values=self.symbols)

        self.type_label = ButtonTypeLabel(self, 'Player type')
        self.type_combobox = ComboBox(self, values=['Human', 'Random AI'])

        self.color_label = ButtonTypeLabel(self, 'Color')
        self.color_combobox = ComboBox(self, values=self.colors)


class GameCreationFrame(AppFrame):
    """The frame for the menu before starting the game"""
    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent)

        self.back_button = BackButton(self)
        self.button_frame.pack(side='bottom', pady=(0, 5))

        self.start_button = Button(self,
                                    'START',
                                    [200, 42],
                                    command=self.start_game)

        self.start_button.pack(side='bottom', pady=(0, 5))

        self.player_1_frame = PlayerSettingsFrame(self, '1')
        self.player_2_frame = PlayerSettingsFrame(self, '2')
        self.player_1_frame.pack(side='left', expand=True, fill='y')
        self.player_2_frame.pack(side='right', expand=True, fill='y')

    def start_game(self):
        self.parent.game_active = True
        self.parent.play_frame.reset_board()
        self.change_frame(self.parent.play_frame)


class PlayFrame(AppFrame):
    """The frame for the tic-tac-toe game itself"""
    def __init__(self, parent):
        self.parent = parent
        self.board = Board()
        self.player_1 = self.create_player('X', 'Human')
        self.player_2 = self.create_player('O', 'Random AI')
        self.player = self.player_1
        super().__init__(self.parent)

        # Reset button
        self.reset_button_frame = ctk.CTkFrame(self.button_frame, fg_color=settings['bg_color'])
        self.reset_button_frame.pack(side='right', padx=(0, 90), fill='x')
        self.reset_button = Button(self.reset_button_frame, '⟳', [42, 42], command=self.reset_board)

        # Back button
        self.back_button = BackButton(self)
        self.back_button.place(relx=0.5, anchor="center", rely=0.5)
        # self.button_frame.configure(fg_color='#666666')
        self.button_frame.pack(side='bottom', pady=(0, 5), anchor='center', fill='x', expand=True)

        # Game settings button
        self.settings_button_frame = ctk.CTkFrame(self.button_frame, fg_color=settings['bg_color'])
        self.settings_button_frame.pack(side='left', padx=(90, 0), fill='x')
        self.settings_button = Button(self.settings_button_frame, '⚙', [42, 42], command=self.back_to_game_settings)
        # self.settings_button.pack()

        # Title label
        self.title_label = ctk.CTkLabel(self,
                                        text=f'Player {self.player_1.symbol} ,start the game!',
                                        font=(settings['font'], 16, 'bold'),
                                        text_color=settings['dark_bg_color'])
        self.title_label.pack()

        # Board frame
        self.board_frame = ctk.CTkFrame(self,
                                        fg_color=settings['gray'],
                                        width=300,
                                        height=300,
                                        border_color=settings['bg_color'],
                                        border_width=8, # ADJUST ME LATER!!!!!!!
                                        corner_radius=0)
        self.board_frame.grid_propagate(False)

        self.buttons = []
        self.create_grid()
        self.board_frame.pack(pady=(10, 6), padx=(10, 10))

        self.player.turn()

    def create_grid(self) -> None:
        """Creates the grid of buttons connected to board cells"""
        for i in range(len(self.board.state)):
            self.board_frame.rowconfigure(i, weight=1, uniform='grid')
            self.board_frame.columnconfigure(i, weight=1, uniform='grid')

        for row in range(len(self.board.template)):
            for col, cell in enumerate(self.board.template[row]):
                button = BoardButton(self.board_frame, f'{self.board.template[row][col]}', row, col, command=lambda move=cell: self.make_move(move))

                self.buttons.append(button)

    def create_player(self, symbol, player_type):
        if player_type == 'Human':
            return HumanPlayer(symbol, self)

        elif player_type == 'Random AI':
            return AiPlayer(symbol, self)

    def swap_player(self) -> None:
        """Swap the current player"""
        if self.player == self.player_1: self.player = self.player_2
        else: self.player = self.player_1

    def lock_board_buttons(self) -> None:
        """disable all board buttons"""
        for button in self.buttons:
            button.configure(state='disabled')

    def unlock_free_buttons(self) -> None:
        """Unlock all board buttons that are still free (don't have an image on them)"""
        for button in self.buttons:
            print('a' + button.cget('text') + 'b')
            if  not button.cget('image'):
                button.configure(state='enabled')

    def check_result(self) -> str:
        """
        Check the result of the game and change the title label correspondingly

        :return: 'X' if player X won,
         'O' if player O won,
         'FULL' if the board is full, and it's a tie,
          None if there is no final result yet
        """
        result = self.board.get_result()

        # Tie
        if result == 'FULL':
            self.title_label.configure(text='It\'s a tie!')
            self.parent.game_active = False

        # One of the players won
        elif result:
            self.title_label.configure(text=f'Player {result} won!')
            self.lock_board_buttons()
            self.parent.game_active = False

        return result

    def reset_board(self) -> None:
        """Enable all board buttons and reset their images"""
        self.parent.game_active = True
        self.board = Board()
        self.player = self.player_1

        for i, button in enumerate(self.buttons):
            button.configure(state='enabled', text=str(i + 1), image=None)

        self.title_label.configure(text=f'Player {self.player_1.symbol} starts the game!')

    def back_to_game_settings(self) -> None:
        self.parent.game_active = False
        self.change_frame(self.parent.game_creation_frame)

    def make_move(self, move) -> None:
        """
        Handle the pressings of a board button by the current player

        :param move: The number corresponding to the board cell
        # :param symbol: The symbol of the current player
        """
        delay = 0
        self.board.update(move, self.player.symbol)
        image = ctk.CTkImage(Image.open(f'Assets/{self.player.symbol}_symbol.png'), size=(64, 64))
        self.buttons[int(move) - 1].configure(state='disabled', text='', image=image)

        self.update_idletasks()
        if not self.check_result():
            self.swap_player()
            self.title_label.configure(text=f'Player {self.player.symbol}, make your move!')

            if isinstance(self.player, AiPlayer):
                self.title_label.configure(text=f'AI player {self.player.symbol} is making it\'s move!')
                self.lock_board_buttons()
                delay = 700

            self.after(delay, self.player.turn)

