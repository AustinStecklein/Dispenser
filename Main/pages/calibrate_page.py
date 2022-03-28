import tkinter as tk
from pages.page import Page
import pages.backend as backend

# TODO: font and buttons

class CalibratePage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       def begin_calibration():
           backend.begin_calibration()
           self.lower()

       response_frame = tk.Frame(self)
       response_frame.pack(side = 'top', expand = True)

       label = tk.Label(response_frame, text="Begin calibration?")
       label.pack(side="top", fill="both", expand=False, pady = 10)

       yes_button = tk.Button(response_frame, text = "Yes", fg = "white", bg = "#c62b24", width="20", height="2", command = begin_calibration)
       yes_button.pack(side="left", expand = False, padx = 10)

       no_button = tk.Button(response_frame, text = "No", fg = "white", bg = "#c62b24", width="20", height="2", command = self.lower)
       no_button.pack(side="left", expand = False, padx = 10)