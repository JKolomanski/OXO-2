#!/usr/bin/env python3

"""
    OXO 2: Tkinter edition
    OXO with full graphical ui written with tkinter
    also contains tons of new quirks and features!
"""

from frames import *


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
        self.main_menu_frame = MainMenuFrame(parent=self)
        self.play_frame = None
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


if __name__ == '__main__':
    app = App()
    app.mainloop()