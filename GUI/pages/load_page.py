import tkinter as tk

from pages.page import Page
import modules.backend as backend

# TODO: up / down arrow buttons show a few at a time
class LoadPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.current_page = backend.load_page

        heading_label = tk.Label(self, text = 'Select a previously saved configuration', bg = 'light gray')
        heading_label .pack(side = 'top', expand = False, anchor = 'w')

        arrows_frame = tk.Frame(self)
        arrows_frame .pack()

        left_arrow = tk.Button(arrows_frame, text = '<', 
                                fg = "white", bg = "#c62b24", width="2", height="1", command = backend.prev_page)
        left_arrow .pack(side = 'left', padx = 10)

        page_number_label = tk.Label(arrows_frame, text = '1')
        page_number_label .pack(side = 'left', padx = 10)
        def get_page_number():
            new_number = backend.get_page()
            page_number_label.config(text = new_number)
            arrows_frame.after(10, get_page_number)
        get_page_number
        
        right_arrow = tk.Button(arrows_frame, text = '>', 
                                fg = "white", bg = "#c62b24", width="2", height="1", command = backend.next_page)
        right_arrow .pack(side = 'left', padx = 10)

        bottom_frame = tk.Frame(self)
        bottom_frame .pack()

        def load_preset(load_string):
            backend.load_preset(load_string)
            self.lower()



        load_list = backend.get_load_list()

        for load_string in load_list:
            load_frame = tk.Frame(bottom_frame)
            load_frame.pack(side = 'top', expand = False, anchor = 'w', pady = 2)

            load_button = tk.Button(load_frame, text = load_string, bg = "light gray", borderwidth = 0, 
                                    width = 40, height = 2, command = lambda string = load_string: load_preset(string) )
            load_button.pack(side = 'right', expand = False)


