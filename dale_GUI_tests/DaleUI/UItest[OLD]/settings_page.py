import tkinter as tk
from page import *

class SettingsPage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        label = tk.Label(self, text ="SCALE WEIGHT", bg = "#FFFFFF")
        label.place(x = 123, y = 123)
