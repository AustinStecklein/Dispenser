import tkinter as tk

from pages.page           import *
from pages.settings_page  import *
from pages.calibrate_page import *
from pages.home_page      import *
from pages.save_page      import *
from pages.power_off_page import *

import modules.backend

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        # Page Frames
        home_page       = HomePage(self)
        settings_page   = SettingsPage(self)
        calibrate_page  = CalibratePage(self)
        save_page       = SavePage(self)
        power_off_page  = PowerOffPage(self)

        # Image Declarations
        #home = tk.PhotoImage("home.png")

        
        # Page Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", expand=False, anchor="se")
        
        # Power Button
        power_button = tk.Button(button_frame, image = power, width = 80, height = 80, background = "black", command = power_off_page.show)
        power_button.pack(side = 'right', expand = False, anchor = 'w', padx = 2)

        # Home Button
        home_button = tk.Button(button_frame, image = home, width = 80, height = 80, background = "black", command = home_page.go_home)
        home_button.pack(side = "right", anchor = "w", pady = 4)

        # Power Button
        right_arrow_button = tk.Button(button_frame, image = power, width = 80, height = 80, background = "black", command = power_off_page.show)
        right_arrow_button.pack(side = 'right', expand = False, anchor = 'w', padx = 2)

        # Home Button
        left_arrow_button = tk.Button(button_frame, image = home, width = 80, height = 80, background = "black", command = home_page.go_home)
        left_arrow_button.pack(side = "right", anchor = "w", pady = 4)

        page_frame = tk.Frame(self)
        page_frame.pack(side="right", fill="both", expand=True)

        home_page       .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        save_page       .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        calibrate_page  .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        settings_page   .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        power_off_page  .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        
        home_page.show()

if __name__ == "__main__":
    root = tk.Tk()


    home = PhotoImage(file = 'home.png')
    power = PhotoImage(file = 'power.png')
    
    

    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x480")
    root.resizable(height=False, width=False)
    root.mainloop()