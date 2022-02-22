import tkinter as tk
from pages.page import Page
import modules.backend as backend

class SavePage(Page):
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        top_frame = tk.Frame(self)
        top_frame.pack(side = 'top', expand = True, anchor = 'nw')

        save_button = tk.Button(top_frame, text = 'Save Card', fg = "white", bg = "#c62b24",
                                width="15", height="2", command = backend.power_off)

        file_name_label = tk.Label(top_frame, text = 'File Name:', bg = 'light gray', width = '50', height = '2')

        edit_name_button = tk.Button(top_frame, text = "Edit", fg = "white", bg = "#c62b24",
                                    width="10", height="2", command = backend.power_off)

        save_button.pack(side = 'left', expand = False)
        file_name_label.pack(side = 'left', expand = False)
        edit_name_button.pack(side = 'left', expand = False)

        