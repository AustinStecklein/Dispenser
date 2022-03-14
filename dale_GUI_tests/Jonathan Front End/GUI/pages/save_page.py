from ctypes import alignment
import tkinter as tk
from turtle import left
from pages.page import Page
import modules.backend as backend
import tkinter.font as font
from pages.home_page      import *
import Images
from modules.keyboard import *

class SavePage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       main_font = font.Font(family = "Bahnschrift", size = 25)
       scale_font = font.Font(family='Bahnschrift', size=26, weight='bold')

       test_name = backend.get_test_name()


       def popup_test():
            popup = tk.Toplevel()
            popup.geometry('800x480')
            popup.resizable(height=False, width=False)
            #test_name = input("Please Input Filename: ")
            
            ## Num Pad
            keyboard_frame = tk.Frame(popup)
            keyboard_frame.pack(side = 'bottom', padx = 4, pady = 30)

            keyboard = Keyboard(keyboard_frame)
            keyboard.pack()

            

       # Initialize Page

       save_page = tk.Frame(self)
       save_page .place(in_=self, x=0, y=0, relwidth=1, relheight=1)

       top_bar = tk.Frame(save_page, borderwidth=0, width = 800, background="light gray")
       top_bar.pack(side = 'top', expand = False,  fill = 'x', anchor = 'w', pady = 2)

       save_button = tk.Button(top_bar, image = Images.get('save_card'), width = '225', borderwidth=0)
       save_button.pack(side="left", expand=False, fill = "both", anchor = 'w')

       filename_label = tk.Button(top_bar, text="Filename: ", width = '10', font = scale_font, command = popup_test, borderwidth=0, background = "light gray")
       filename_label.pack(side="left", expand=False, fill = "both", anchor = 'w')

       name_label = tk.Label(top_bar, text=test_name, width = '20', font = scale_font, borderwidth=0, background = "light gray", anchor = 'w')
       name_label.pack(side="left", expand=False, anchor = 'w')

       load_list = backend.get_save_list()
       load_list1 = backend.get_save_list1()

       

       info_section = tk.Frame(save_page)
       info_section.pack(side = 'top', expand = False, pady = 2)

       left_side = tk.Canvas(info_section, width = 250)
       left_side.grid(row = 0, column = 0, sticky = 'nw', ipadx = "25")

       right_side = tk.Canvas(info_section, width = 350)
       right_side.grid(row = 0, column = 1, sticky = 'nw')

       for load_string in load_list:
            load_frame = tk.Frame(left_side)
            load_frame.pack(side = 'top', expand = False, pady = 3, fill = 'x', anchor = 'w')

            load_label = tk.Button(load_frame, text = load_string, bg = 'light gray', font = scale_font, width = '20',  anchor = 'w', pady = 4)
            load_label.pack(side = 'left', expand = False)

       for load_string in load_list1:
            if (load_string == "Notes: "):
               load_frame = tk.Frame(right_side)
               load_frame.pack(side = 'top', expand = False, pady = 25, fill = 'x')

               load_label = tk.Button(load_frame, text = load_string, bg = 'light gray', font = scale_font, width = '20', height = "4", pady = 2, anchor = "nw")
               load_label.pack(side = 'right', expand = False)

            else:
                load_frame = tk.Frame(right_side)
                load_frame.pack(side = 'top', expand = False, pady = 3, fill = 'x', anchor = 'w')

                load_label = tk.Button(load_frame, text = load_string, bg = 'light gray', font = scale_font, width = '20',  anchor = 'w', pady = 4)
                load_label.pack(side = 'right', expand = False)

        
