import tkinter as tk
from pages.page import Page
import modules.backend as backend

class SavePage(Page):
   def __init__(self, *args, **kwargs):
      Page.__init__(self, *args, **kwargs)

      top_frame = tk.Frame(self)
      top_frame.pack(side = 'top', expand = False, anchor = 'nw')

      save_button = tk.Button(top_frame, text = 'Save Card', fg = "white", bg = "#c62b24",
                              width="15", height="2", command = backend.power_off)

      file_name_label = tk.Button(top_frame, text = 'File Name:', bg = 'light gray', 
                                 width = '80', height = '2', anchor = 'w', borderwidth = 0)

      save_button.pack(side = 'left', expand = False)
      file_name_label.pack(side = 'left', expand = False)

      bottom_frame = tk.Frame(self)
      bottom_frame.pack(side = 'top', expand = False)

      left_frame = tk.Frame(bottom_frame)
      left_frame.pack(side = 'left', expand = False, anchor = 'n')

      button_height = 3
      button_width = 50

      cartridge_label = tk.Button(left_frame, text = "Cartridge:", bg = 'light gray', 
                                 width = button_width, height = button_height, anchor = 'nw', borderwidth = 0)
      bullet_label = tk.Button(left_frame, text = "Bullet:", bg = 'light gray', 
                                 width = button_width, height = button_height, anchor = 'nw', borderwidth = 0)
      powder_label = tk.Button(left_frame, text = "Powder:", bg = 'light gray', 
                                 width = button_width, height = button_height, anchor = 'nw', borderwidth = 0)
      charge_weight_label = tk.Button(left_frame, text = "Charge Weight:", bg = 'light gray', 
                                 width = button_width, height = button_height, anchor = 'nw', borderwidth = 0)
      coal_label = tk.Button(left_frame, text = "C.O.A.L", bg = 'light gray', 
                                 width = button_width, height = button_height, anchor = 'nw', borderwidth = 0)

      cartridge_label      .pack(side = 'top', expand = False, pady = 4, padx = 10)
      bullet_label         .pack(side = 'top', expand = False, pady = 4, padx = 10)
      powder_label         .pack(side = 'top', expand = False, pady = 4, padx = 10)
      charge_weight_label  .pack(side = 'top', expand = False, pady = 4, padx = 10)
      coal_label           .pack(side = 'top', expand = False, pady = 4, padx = 10)


      right_frame = tk.Frame(bottom_frame)
      right_frame.pack(side = 'right', expand = False, anchor = 'n')

      primer_label = tk.Button(right_frame, text = "Primer:", bg = 'light gray', 
                                 width = button_width, height = button_height, anchor = 'nw', borderwidth = 0)
      brass_label = tk.Button(right_frame, text = "Brass:", bg = 'light gray', 
                                 width = button_width, height = button_height, anchor = 'nw', borderwidth = 0)
      notes_label = tk.Button(right_frame, text = "Notes:", bg = 'light gray', 
                                 width = button_width, height = button_height * 3, anchor = 'nw', borderwidth = 0)
                                 
      primer_label   .pack(side = 'top', expand = False, pady = 4, padx = 10)
      brass_label    .pack(side = 'top', expand = False, pady = 4, padx = 10)
      notes_label    .pack(side = 'top', expand = False, pady = 4, padx = 10)

        