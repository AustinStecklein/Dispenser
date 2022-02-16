import tkinter as tk

from page           import Page
from settings_page  import *
from calibrate_page import *
from load_page      import *
from home_page      import *
from save_page      import *
from power_off_page import *
from mainmenu_page  import *

import backend

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)


        # Page Frames
        home_page       = HomePage(self)
        settings_page   = SettingsPage(self)
        calibrate_page  = CalibratePage(self)
        load_page       = LoadPage(self)
        save_page       = SavePage(self)
        power_off_page  = PowerOffPage(self)
        mainmenu_page   = MainMenuPage(self)

        page_frame = tk.Frame(self)
        page_frame.pack(side="top", fill="both", expand=True)

        home_page.place     (in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        load_page.place     (in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        save_page.place     (in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        calibrate_page.place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        settings_page.place (in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        power_off_page.place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        mainmenu_page.place (in_=page_frame, x=0, y=0, relwidth=1, relheight=1)

        # Page Buttons
        button_frame = tk.Canvas(self)
        button_frame.pack(side="bottom", fill="x", expand=False, anchor="nw" )

        logo = PhotoImage(file = 'home.gif')

        home_button          = tk.Button(button_frame, image = logo,         fg = "white", bg = "#c62b24", width = 20, height=20, command = mainmenu_page.show)
        #load_button         = tk.Button(button_frame, text = "Load",        fg = "white", bg = "#c62b24", width="15", height="4", command = load_page.show)
        #save_button         = tk.Button(button_frame, text = "Save",        fg = "white", bg = "#c62b24", width="15", height="4", command = save_page.show)
        #calibrate_button    = tk.Button(button_frame, text = "Calibrate",   fg = "white", bg = "#c62b24", width="15", height="4", command = calibrate_page.show)
        #settings_button     = tk.Button(button_frame, text = "Settings",    fg = "white", bg = "#c62b24", width="15", height="4", command = settings_page.show)

        button_pad_y = 4 # space above and below each button
        home_button.place(       x = 795,    anchor="se",   y = 475)
        #load_button.pack(       side="top", anchor="w", pady = button_pad_y)
        #save_button.pack(       side="top", anchor="w", pady = button_pad_y)
        #calibrate_button.pack(  side="top", anchor="w", pady = button_pad_y)
        #settings_button.pack(   side="top", anchor="w", pady = button_pad_y)
        
        # Power Button
        #mini = PhotoImage(file = 'dale_GUI_tests\Jonathan Front End\Merged Files\mini.png')

        

        

        #mainmenu_page.show()

        #home_page.show()
        

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)

    #Sets Size of Program and ensures the Program stays the same height and width
    root.wm_geometry("800x480")
    root.resizable(height=False, width=False)

    #End of Program
    root.mainloop()