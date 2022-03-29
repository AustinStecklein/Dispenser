import tkinter as tk
from pages.page import Page
import pages.backend as backend
import pages.images.images as Images
import tkinter.font as font


# TODO: Font
# TODO: Buttons

class PowerOffPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        question_font = font.Font(family='Bahnschrift', size=20, weight='bold')
        button_font = font.Font(family='Bahnschrift', size=14, weight='bold')
        previous_font = font.Font(family='Bahnschrift', size=12, weight='bold')

        response_frame = tk.Frame(self)
        response_frame.pack(side = 'top', expand = True)

        label = tk.Label(response_frame, text="Are you sure you want to power off?", font = question_font)
        label.pack(side="top", fill="both", expand=False, pady = 10)

        yes_button = tk.Button(response_frame, text = "Yes", fg = "white", bg = "#c62b24", width="20", height="2", command = backend.power_off, font = button_font)
        yes_button.pack(side="left", expand = False, padx = 10)

        no_button = tk.Button(response_frame, text = "No", fg = "white", bg = "#c62b24", width="20", height="2", command = self.lower, font = button_font)
        no_button.pack(side="left", expand = False, padx = 10)
        

