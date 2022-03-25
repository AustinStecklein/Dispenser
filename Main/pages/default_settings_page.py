import tkinter as tk
from pages.page import Page
import pages.backend as backend

class DefaultSettingsPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def defaults():
            backend.startReset()
            self.lower()

        
        label = tk.Label(self, text="Would you like to reset to default settings?")
        label.pack(side="top", fill="both", expand=True)

        buttons_frame = tk.Frame(self)
        buttons_frame .pack(side = 'top', anchor = 'n', expand = True)

        yes_button = tk.Button(buttons_frame, text = 'Yes', 
                                fg = "white", bg = "#c62b24", width="15", height="2", command = defaults)
        yes_button .pack(side = 'left', padx = 10)
        
        no_button = tk.Button(buttons_frame, text = 'No', 
                                fg = "white", bg = "#c62b24", width="15", height="2", command = self.lower)
        no_button .pack(side = 'left', padx = 10)