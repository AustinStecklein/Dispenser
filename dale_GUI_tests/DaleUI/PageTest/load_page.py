import tkinter as tk
from page import Page
import backend

# TODO: handle more load presets than the screen can display - scrolling list or such
class LoadPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        heading_label = tk.Label(self, text = 'Select a previously saved configuration', bg = 'light gray')
        heading_label.pack(side = 'top', expand = False, anchor = 'w')

        def load_preset(load_string):
            backend.load_preset(load_string)
            self.lower()

        load_list = backend.get_load_list()

        for load_string in load_list:
            load_frame = tk.Frame(self)
            load_frame.pack(side = 'top', expand = False, anchor = 'w', pady = 2)

            load_button = tk.Button(load_frame, text = 'Load', fg = "white", bg = "#c62b24", width="10", height="2", command = lambda string = load_string: load_preset(string) )
            load_button.pack(side = 'right', expand = False)

            load_label = tk.Label(load_frame, text = load_string, bg = 'light gray')
            load_label.pack(side = 'right', expand = False)

