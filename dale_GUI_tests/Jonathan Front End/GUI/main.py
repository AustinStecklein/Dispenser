import tkinter as tk

from pages.page           import *
from pages.settings_page  import *
from pages.calibrate_page import *
from pages.home_page      import *
from pages.save_page      import *
from pages.power_off_page import *
import Images

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
        button_frame = tk.Frame(self, background="black")
        button_frame.pack(side="bottom", expand=False, anchor="se")
        
        # Power Button
        power_button = tk.Button(button_frame, image = power, background = "black", borderwidth = 0, command = power_off_page.show)
        power_button.pack(side = 'right', expand = False, anchor = 'w')

        # Home Button
        home_button = tk.Button(button_frame, image = home, width = 80, height = 80, background = "black", borderwidth = 0,command = home_page.go_home)
        home_button.pack(side = "right", anchor = "w")

        # Power Button
        right_arrow_button = tk.Button(button_frame, image = right_arrow, width = 80, height = 80, background = "black", borderwidth = 0,)
        right_arrow_button.pack(side = 'right', expand = False, anchor = 'w')

        # Home Button
        left_arrow_button = tk.Button(button_frame, image = left_arrow, background = "black", borderwidth = 0,)
        left_arrow_button.pack(side = "right", anchor = "w")

        # Home Button

        page_frame = tk.Frame(self)
        page_frame.pack(side="right", fill="both", expand=True)

        home_page       .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        save_page       .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        calibrate_page  .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        settings_page   .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        power_off_page  .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        
        home_page.load_image = PhotoImage(file = 'load_Button.png')

        home_page.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Dispenser')

    #Define Menu Image Variables

    home =        PhotoImage(file = 'home.png')
    home_small = home.subsample(2, 2)

    power =       PhotoImage(file = 'power.png')
    left_arrow =  PhotoImage(file = 'left_arrow.png')
    right_arrow = PhotoImage(file = 'right_arrow.png')
    load_button =   PhotoImage(file = 'load_Button.png')
    home_small = load_button.subsample(2, 2)

    load_image = PhotoImage(file = 'load_Button.png')
    

    main = MainView(root)
    
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x480")
    root.resizable(height=False, width=False)
    root.mainloop()