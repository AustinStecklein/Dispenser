import tkinter as tk

from pages.page           import *
from pages.home_page      import *
from pages.power_off_page import *

import modules.backend

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        # Page Frames
        home_page       = HomePage(self)
        power_off_page  = PowerOffPage(self)

        # Image Declarations
        home = tk.PhotoImage("home.png")

        
        # Page Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", expand=False, anchor="se")
        
        # Power Button
        power_button = tk.Button(button_frame, text = "Power", fg = '#FFFFFF', bg = "#c62b24", width = '10', height = '2', command = power_off_page.show)
        power_button.pack(side = 'right', expand = False, anchor = 'w', padx = 2)

        # Home Button
        home_button = tk.Button(button_frame, text = "Home", fg = "white", bg = "#c62b24", width="10", height="2", command = home_page.go_home)
        home_button.pack(side = "right", anchor = "w", pady = 4)

        page_frame = tk.Frame(self)
        page_frame.pack(side="right", fill="both", expand=True)

        home_page       .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        power_off_page  .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        
        home_page.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x480")
    root.resizable(height=False, width=False)
    root.mainloop()