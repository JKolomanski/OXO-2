import customtkinter as ctk
from PIL import Image
import json


def get_settings() -> dict:
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
accent1 = settings['blue']
accent2 = settings['orange']


class AppFrame(ctk.CTkFrame):
    """
    Base class for all frames in the application.
    Contains only the back button.
    """
    def __init__(self, parent):
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
                         fg_color=accent1,
                         hover_color=accent2,
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
    def __init__(self, parent, text, row, col, view_numbers, command):
        self.parent = parent
        self.text = text
        self.command = command
        self.row = row
        self.col = col
        if view_numbers: text_color = settings['gray']
        else: text_color = settings['bg_color']
        super().__init__(self.parent,
                         text=self.text,
                         fg_color=settings['bg_color'],
                         hover_color=settings['bg_color'],
                         corner_radius=0,
                         width=90,
                         height=90,
                         text_color=text_color,
                         font=(settings['font'], 32),
                         command=self.command)

        self.grid(row=self.row, column=self.col)


class ButtonTypeLabel(ctk.CTkLabel):
    def __init__(self, parent, text: str):
        self.parent = parent
        super().__init__(self.parent,
                         text=text,
                         font=(settings['font'], 14),
                         text_color=settings['dark_bg_color'])
        self.pack(pady=(15, 0), anchor='w')

class ComboBox(ctk.CTkComboBox):
    def __init__(self, parent, values: tuple):
        self.parent = parent
        super().__init__(self.parent,
                         width=160,
                         height=30,
                         values=values,
                         state='readonly',
                         fg_color=settings['blue'],
                         border_color=settings['blue'],
                         dropdown_fg_color=settings['blue'],
                         dropdown_hover_color=settings['orange'],
                         dropdown_text_color=settings['bg_color'],
                         font=(settings['font'], 16),
                         text_color=settings['bg_color'])
        self.set(values[0])
        self.pack()
