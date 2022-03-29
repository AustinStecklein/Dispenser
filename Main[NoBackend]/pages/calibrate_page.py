import tkinter as tk
from pages.page import Page
import pages.backend as backend
import tkinter.font as font


# TODO: font and buttons

class CalibratePage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       unit_font = font.Font(family='Bahnschrift', size=14)
       label_font = font.Font(family='Bahnschrift', size=20, weight='bold')

       def begin_calibration():
           backend.begin_calibration()
           self.lower()

       response_frame = tk.Frame(self)
       response_frame.pack(side = 'top', expand = True)

       label = tk.Label(response_frame, text="Begin calibration?", font = label_font)
       label.pack(side="top", fill="both", expand=False, pady = 10)

       yes_button = tk.Button(response_frame, text = "Yes", fg = "white", bg = "#c62b24", width="15", height="2", command = begin_calibration, font = unit_font)
       yes_button.pack(side="left", expand = False, padx = 10)

       no_button = tk.Button(response_frame, text = "No", fg = "white", bg = "#c62b24", width="15", height="2", command = self.lower, font = unit_font)
       no_button.pack(side="left", expand = False, padx = 10)