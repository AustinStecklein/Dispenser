import tkinter as tk
from pages.page import Page
import modules.backend as backend
import tkinter.font as font

class SavePage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       # Initialize Page

       save_page = tk.Frame(self)
       save_page .place(in_=self, x=0, y=0, relwidth=1, relheight=1)

       top_bar = tk.Frame(save_page, border = "3", borderwidth=2, bg = "Black", width = 100)
       top_bar.pack(side = 'top', expand = False,  fill = 'x', anchor = 'w', pady = 2)

       label = tk.Button(top_bar, text="Save Card", width = '25')
       label.pack(side="left", expand=False, fill = "both", anchor = 'w')

       label = tk.Button(top_bar, text="Filename", width = '50')
       label.pack(side="right", expand=False, fill = "both", anchor = 'e')

       load_list = backend.get_save_list()
       load_list1 = backend.get_save_list1()

       scale_font = font.Font(family='Bahnschrift', size=20, weight='bold')

       info_section = tk.Frame(save_page, border = "3", borderwidth=2, bg = "Black", width = 50)
       info_section.pack(side = 'top', expand = False, pady = 2)

       for load_string in load_list:
            load_frame = tk.Frame(info_section, width = 45)
            load_frame.pack(side = 'top', expand = False, pady = 2, fill = 'x')

            load_label = tk.Label(load_frame, text = load_string, bg = 'light gray', font = scale_font, width = '20',  anchor = 'w', pady = 2)
            load_label.pack(side = 'left', expand = False)

       for load_string in load_list1:
            load_frame = tk.Frame(info_section, width = 45)
            load_frame.pack(side = 'top', expand = False, pady = 2, fill = 'x')

            load_label = tk.Label(load_frame, text = load_string, bg = 'light gray', font = scale_font, width = '20',  anchor = 'w', pady = 2)
            load_label.pack(side = 'right', expand = False)

        
