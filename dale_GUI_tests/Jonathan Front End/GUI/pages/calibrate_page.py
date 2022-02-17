import tkinter as tk
from pages.page import Page

class CalibratePage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is calibrate page")
       label.pack(side="top", fill="both", expand=True)