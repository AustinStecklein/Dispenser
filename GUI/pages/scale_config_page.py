import tkinter as tk
from pages.page import Page

class ScaleConfigPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        label = tk.Label(self, text="This is scale config page")
        label.pack(side="top", fill="both", expand=True)

        save_button = tk.Button(self, text = 'Save Selections', 
                                fg = "white", bg = "#c62b24", width="15", height="2", command = self.lower)

        save_button .pack()