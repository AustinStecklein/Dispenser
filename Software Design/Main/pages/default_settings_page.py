import tkinter as tk
from pages.page import Page
import pages.backend as backend
import tkinter.font as font

# TODO: Buttons

class DefaultSettingsPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        # Fonts and Styles
        unit_font = font.Font(family='Bahnschrift', size=14)
        label_font = font.Font(family='Bahnschrift', size=20, weight='bold')

        # Default Function that resets
        def defaults():
            backend.startReset()
            self.lower()

        # Default Question
        label = tk.Label(self, text="Would you like to reset to default settings?", font = label_font)
        label.pack(side="top", fill="both", expand=True)

        # Yes and No Buttons Frame 
        buttons_frame = tk.Frame(self)
        buttons_frame .pack(side = 'top', anchor = 'n', expand = True)

        yes_button = tk.Button(buttons_frame, text = 'Yes', 
                                fg = "white", bg = "#c62b24", width="15", height="2", command = defaults, font = unit_font)
        yes_button .pack(side = 'left', padx = 10)
        
        no_button = tk.Button(buttons_frame, text = 'No', 
                                fg = "white", bg = "#c62b24", width="15", height="2", command = self.lower, font = unit_font)
        no_button .pack(side = 'left', padx = 10)