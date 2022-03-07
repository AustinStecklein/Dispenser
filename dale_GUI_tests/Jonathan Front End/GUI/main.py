from tkinter import *
from tkinter.ttk import *

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
        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", expand=False, anchor="se")

        # Menu Bar
        menu_bar_image = tk.Label(button_frame, borderwidth = 0, image = menu_bar)
        menu_bar_image.pack(side = 'bottom', expand = False, anchor = 'se')
        
        # Power Button
        power_button = tk.Button(menu_bar_image, image = power, borderwidth = 0, command = power_off_page.show)
        power_button.place(relx = 1, rely = 1, anchor = "se")

        # Home Button
        home_button = tk.Button(menu_bar_image, image = home, borderwidth = 0,command = home_page.go_home)
        home_button.place(relx = .9, rely = 1, anchor = "se")

        # Right Arrow Button
        right_arrow_button = tk.Button(menu_bar_image, image = right_arrow, borderwidth = 0,)
        right_arrow_button.place(relx = .8, rely = 1, anchor = "se")

        # Left Arrow Button
        left_arrow_button = tk.Button(menu_bar_image, image = left_arrow, borderwidth = 0,)
        left_arrow_button.place(relx = .7, rely = 1, anchor = "se")

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
    power =       PhotoImage(file = 'power.png')
    left_arrow =  PhotoImage(file = 'left_arrow.png')
    right_arrow = PhotoImage(file = 'right_arrow.png')
    menu_bar =    PhotoImage(file = 'Bottom Bar.png')
    load_button = Images.get('load')

    home_small = power.subsample(3, 3)
    

    main = MainView(root)
    
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x480")
    root.resizable(height=False, width=False)
    root.mainloop()