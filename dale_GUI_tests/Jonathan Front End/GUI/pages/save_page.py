import tkinter as tk
from pages.page import Page
import modules.backend as backend
import tkinter.font as font
from pages.home_page      import *
import Images
from pages.keyboard import *


new_filename = backend.get_filename()

class SavePage(Page):
     def __init__(self, *args, **kwargs):
          Page.__init__(self, *args, **kwargs)

          # Fonts, which include type, size, and weight 

          main_font = font.Font(family = "Bahnschrift", size = 25)
          scale_font = font.Font(family='Bahnschrift', size=26, weight='bold')
          details_font = font.Font(family='Bahnschrift', size=18, weight='bold')

          # Pop out Window for the user to input text using digital keyboard

          self.keyboard      = Keyboard(self)
          self.keyboard      .place(in_ = self, x = 0, y = 0, relwidth = 1, relheight = 1)


          def filename_keyboard():
               backend.set_label("Filename")
               backend.set_counter(0)

               self.keyboard.show()

          def cart_keyboard():
               backend.set_label("Notes")
               backend.set_counter(1)

               self.keyboard.show()

          def notes_keyboard():
               backend.set_label("Notes")
               backend.set_counter(1)

               self.keyboard.show()

          def notes_keyboard():
               backend.set_label("Notes")
               backend.set_counter(1)

               self.keyboard.show()
          def notes_keyboard():
               backend.set_label("Notes")
               backend.set_counter(1)

               self.keyboard.show()

          def notes_keyboard():
               backend.set_label("Notes")
               backend.set_counter(1)

               self.keyboard.show()

          
          full_filename_text = "Filename:" + "    " + new_filename

          # Initialize Page

          save_page = tk.Frame(self)
          save_page .place(in_=self, x=0, y=0, relwidth=1, relheight=1)

          top_bar = tk.Frame(save_page, borderwidth=0, width = 800, background="light gray")
          top_bar.pack(side = 'top', expand = False,  fill = 'x', anchor = 'w', pady = 2)

          save_button = tk.Button(top_bar, image = Images.get('save_card'), width = '225', borderwidth=0)
          save_button.pack(side="left", expand=False, fill = "both", anchor = 'w')

          filename_button = tk.Button(top_bar, text = full_filename_text, width = 800-225, anchor = 'w', font = scale_font, command = filename_keyboard, borderwidth=0, background = "light gray")
          filename_button.pack(side="left", expand=False, fill = "both", anchor = 'w')

          load_list = backend.get_save_list()
          load_list1 = backend.get_save_list1()
          load_list2 = backend.get_save_list()

          def update_units():
               filename_updated = backend.get_filename()
               full_filename_text =  "Filename:" + "   " + filename_updated
               filename_button.config(text = full_filename_text)
               save_page.after(10, update_units)

          update_units()
          

          info_section = tk.Frame(save_page)
          info_section.pack(side = 'top', expand = False, pady = 2)

          left_side = tk.Canvas(info_section, width = 250,)
          left_side.grid(row = 0, column = 0, sticky = 'w', ipadx = "25")

          right_side = tk.Canvas(info_section, width = 350)
          right_side.grid(row = 0, column = 1, sticky = 'w')

          for load_string in load_list:
               load_frame = tk.Frame(left_side)
               load_frame.pack(side = 'top', expand = False, pady = 3, fill = 'x', anchor = 'w')

               load_label = tk.Button(load_frame, text = load_string, bg = 'light gray', font = details_font, borderwidth=0, width = '30',  anchor = 'w', pady = 4)
               load_label.pack(side = 'left', expand = False)

          for load_string in load_list1:
               if (load_string == "Notes: "):
                    load_frame = tk.Frame(right_side)
                    load_frame.pack(side = 'top', expand = False, pady = 20, fill = 'x', anchor = 'e')

                    load_label = tk.Button(load_frame, text = load_string, command = notes_keyboard, bg = 'light gray', font = details_font, borderwidth=0, width = '25', height = "4", pady = 2, anchor = "nw")
                    load_label.pack(side = 'right', expand = False)

               else:
                    load_frame = tk.Frame(right_side)
                    load_frame.pack(side = 'top', expand = False, pady = 3, fill = 'x', anchor = 'e')

                    load_label = tk.Button(load_frame, text = load_string, bg = 'light gray', font = details_font, borderwidth=0, width = '25',  anchor = 'w', pady = 4)
                    load_label.pack(side = 'right', expand = False)

          self.keyboard      .lower()

          
