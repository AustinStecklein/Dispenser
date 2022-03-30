import tkinter as tk
from pages.page import Page
import pages.images.images as Images
import tkinter.font as font

# TODO: Button

class ScaleConfigPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        button_font = font.Font(family='Bahnschrift', size=14)
        label_font = font.Font(family='Bahnschrift', size=20, weight='bold')
        
        label = tk.Label(self, text="Settings: Scale Config", font = label_font)
        label.pack(side="top", fill="both", expand=True)

        save_button = tk.Button(self, text = 'Return to Settings', 
                                fg = "white", bg = "#c62b24", width="15", height="2", command = self.lower, font = button_font)

        save_button .pack()