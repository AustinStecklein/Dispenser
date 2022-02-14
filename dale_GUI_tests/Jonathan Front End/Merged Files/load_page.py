import tkinter as tk
from page import Page

class LoadPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is load page")
       label.pack(side="top", fill="both", expand=True)