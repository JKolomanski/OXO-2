import customtkinter as ctk
import json
# import tkinter as tk
from PIL import Image
import webbrowser

from board import Board


def get_settings():
    """
    Load the settings.json file and return it as a dictionary

    :return: The settings.json as a dict
    """
    with open('settings.json', 'r') as f:
        data = json.load(f)
        data["window_width"] = int(data["window_width"])
        data["window_height"] = int(data["window_height"])
        return data


settings = get_settings()


class App(ctk.CTk):
    """
    Main application class for the whole game
    initializes the main menu, frames and bottom text
    """
    def __init__(self):
        super().__init__(fg_color=settings['bg_color'])
        self.geometry(f'{settings["window_width"]}x{settings["window_height"]}')
        ctk.set_appearance_mode("light")
        # self.resizable(False, False)
        self.title('OXO 2')

        # Initialize all ui components
        self.logo = OXOLogo(self, 359, 93)
        self.about_frame = AboutFrame(parent=self)
        self.settings_frame = SettingsFrame(parent=self)
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


class AppFrame(ctk.CTkFrame):
    """
    Base class for all frames in the application.
    Contains only the back button.
    """
    def __init__(self, parent: App):
        self.parent = parent
        super().__init__(self.parent, fg_color=settings["bg_color"])
        self.button_frame = ctk.CTkFrame(self, fg_color=settings["bg_color"])

    def change_frame(self, frame: 'AppFrame') -> None:
        """
        Switches to a different menu (frame) in the application

        :param frame: The parent frame (App class)
        """
        frame.pack(expand=True, fill="both", pady=(5, 5), padx=(5, 5))
        self.pack_forget()


class MainMenuFrame(AppFrame):
    """Main menu screen containing navigation buttons"""
    def __init__(self, parent):
        self.parent = parent
        self.button_size = [160, 42]
        super().__init__(self.parent)

        # Initialise buttons for different sections
        self.play_button = Button(self.button_frame, 'Play', self.button_size, command=lambda: self.change_frame(parent.play_frame))
        self.settings_button = Button(self.button_frame, 'Settings', self.button_size, command=lambda: self.change_frame(parent.settings_frame))
        self.about_button = Button(self.button_frame, 'About', self.button_size, command=lambda: self.change_frame(parent.about_frame))
        self.Quit_button = Button(self.button_frame, 'Quit', self.button_size, command=self.parent.destroy)

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


class PlayFrame(AppFrame):
    """The frame for the tic-tac-toe game itself"""
    def __init__(self, parent):
        self.parent = parent
        self.board = Board()
        self.starting_player = 'X'
        self.player = self.starting_player
        super().__init__(self.parent)

        # Reset button
        self.reset_button_frame = ctk.CTkFrame(self.button_frame, fg_color=settings['bg_color'])
        self.reset_button_frame.pack(side='right', padx=(0, 75), fill='x')
        self.reset_button = Button(self.reset_button_frame, '⟳', [42, 42], command=self.reset_board)

        # Back button
        self.back_button = BackButton(self)
        self.back_button.place(relx=0.5, anchor="center", rely=0.5)
        self.button_frame.pack(side='bottom', pady=(0, 5), anchor='center', fill='x', expand=True)

        # Title label
        self.title_label = ctk.CTkLabel(self,
                                        text=f'Player {self.starting_player} starts the game!',
                                        font=(settings['font'], 16, 'bold'),
                                        text_color=settings['dark_bg_color'])
        self.title_label.pack()

        # Board frame
        self.board_frame = ctk.CTkFrame(self,
                                        fg_color=settings['gray'],
                                        width=300,
                                        height=300,
                                        border_color=settings['bg_color'],
                                        border_width=5,
                                        corner_radius=0)
        self.board_frame.grid_propagate(False)

        self.buttons = []
        self.create_grid()
        self.board_frame.pack(pady=(10, 6), padx=(10, 10))

    def create_grid(self):
        """Creates the grid of buttons connected to board cells"""
        for i in range(len(self.board.state)):
            self.board_frame.rowconfigure(i, weight=1, uniform='grid')
            self.board_frame.columnconfigure(i, weight=1, uniform='grid')

        for row in range(len(self.board.template)):
            for col, cell in enumerate(self.board.template[row]):
                button = BoardButton(self.board_frame, f'{self.board.state[row][col]}', row, col, command=lambda move=cell: self.make_move(move, self.player))

                self.buttons.append(button)

    def swap_player(self):
        """Swap the current player"""
        if self.player == 'X': self.player = 'O'
        else: self.player = 'X'

    def lock_board_buttons(self):
        """disable all board buttons"""
        for button in self.buttons:
            button.configure(state='disabled')

    def check_result(self):
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

        # One of the players won
        else:
            self.title_label.configure(text=f'Player {result} won!')
            self.lock_board_buttons()

        return result

    def reset_board(self):
        """Enable all board buttons and reset their labels"""
        self.board = Board()
        self.player = self.starting_player

        for button in self.buttons:
            button.configure(state='enabled', text='')

        self.title_label.configure(text=f'Player {self.starting_player} starts the game!')

    def make_move(self, move, symbol):
        """
        Handle the pressings of a board button by the current player

        :param move: The number corresponding to the board cell
        :param symbol: The symbol of the current player
        """
        self.board.update(move, symbol)
        self.buttons[int(move) - 1].configure(text=symbol, state='disabled')
        if not self.check_result():
            self.swap_player()
            self.title_label.configure(text=f'Player {self.player}, make your move!')


class OXOLogo(ctk.CTkLabel):
    """Class for the image of main game logo"""
    def __init__(self, parent, width, height):
        self.width = width
        self.height = height
        self.parent = parent
        self.image = ctk.CTkImage(Image.open('Assets/oxo_logo.png'), size=(self.width, self.height))
        super().__init__(self.parent, self.width, self.height, image=self.image, text='')
        self.pack(pady=(30, 30))


class Button(ctk.CTkButton):
    """
    Generic button class

    :param parent: The parent this button belongs to
    :param text: The text on the button
    :param size: tuple[int, int] containing its width and height
    :param command: a function to be executed on press
    """
    def __init__(self, parent, text, size: tuple[int, int], command):
        self.parent = parent
        self.text = text
        self.command = command
        self.size = size

        super().__init__(self.parent,
                         text=self.text,
                         fg_color=settings['light_blue'],
                         hover_color=settings['light_orange'],
                         width=self.size[0],
                         height=self.size[1],
                         corner_radius=10,
                         text_color=settings['bg_color'],
                         font=(settings['font'], 16),
                         command=self.command)
        self.pack(pady=(10, 10))


class BackButton(Button):
    """Button that navigates to the main menu, inherits from Button"""
    def __init__(self, parent):
        super().__init__(parent.button_frame,
                         'Back to title screen',
                         [200, 42],
                         command=lambda: parent.change_frame(parent.parent.main_menu_frame))

class BoardButton(ctk.CTkButton):
    """
    Generic button class

    :param parent: The parent this button belongs to
    :param text: The text on the button
    :command: a function to be executed on press
    """
    def __init__(self, parent, text, row, col, command):
        self.parent = parent
        self.text = text
        self.command = command
        self.row = row
        self.col = col

        super().__init__(self.parent,
                         text=self.text,
                         fg_color=settings['bg_color'],
                         hover_color=settings['gray'],
                         corner_radius=0,
                         width=90,
                         height=90,
                         text_color=settings['dark_bg_color'],
                         font=(settings['font'], 64),
                         command=self.command)
        self.grid(row=self.row, column=self.col)