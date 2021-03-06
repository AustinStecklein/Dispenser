from tkinter import *
from tkinter.ttk import *

from pages.page           import *
from pages.home_page      import *
from pages.power_off_page import *

import pages.images.images as Images

# TODO: Forward button
# TODO: Back button

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        # Page Frames
        home_page       = HomePage(self)
        power_off_page  = PowerOffPage(self)
        
        # Page Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", expand=False, anchor="se")

        # Menu Bar
        menu_bar_image = tk.Label(button_frame, borderwidth = 0, image = Images.get('menu_bar'))
        menu_bar_image.pack(side = 'bottom', expand = False, anchor = 'se')
        
        # Power Button
        power_button = tk.Button(menu_bar_image, image = Images.get('power'), borderwidth = 0, command = power_off_page.show, background="black")
        power_button.place(relx = .98, rely = .92, anchor = "se")

        # Home Button
        home_button = tk.Button(menu_bar_image, image = Images.get('home'), borderwidth = 0,command = home_page.go_home, background="black")
        home_button.place(relx = .88, rely = .92, anchor = "se")

        # Right Arrow Button
        right_arrow_button = tk.Button(menu_bar_image, image = Images.get('right'), borderwidth = 0 , background="black")
        right_arrow_button.place(relx = .78, rely = .92, anchor = "se")

        # Left Arrow Button
        left_arrow_button = tk.Button(menu_bar_image, image = Images.get('left'), borderwidth = 0 , background="black")
        left_arrow_button.place(relx = .68, rely = .92, anchor = "se")

        # Page Frame which each page will be placed on top of the main page
        page_frame = tk.Frame(self)
        page_frame.pack(side="right", fill="both", expand=True)

        # Enables the Home Page and Power off Pages to be placed underneath the menu bar with the arrow, home and power buttons
        home_page       .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        power_off_page  .place(in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        
        # Show Home_Page
        home_page.show()


if __name__ == "__main__":
    
    # Starts the Program and labels the Screen as Dispenser
    root = tk.Tk()
    root.title('Dispenser')

    # Ensures that the window fills the entire screen, however, it is disabled for Main[No Backend] to allow 
    # the programmer to run and debug the user interface without the Beaglebone Black Wireless 
    #root.attributes('-fullscreen',True)

    # Sets the MainView Class on the root, ensuring it stays on screen on every page while filling the screen
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)

    # Sets the Size of the Screen and disables the user's ability to change the dimensions 
    root.wm_geometry("800x480")
    root.resizable(height=False, width=False)

    # Ensures the Program remains open until the user decides to close it
    root.mainloop()