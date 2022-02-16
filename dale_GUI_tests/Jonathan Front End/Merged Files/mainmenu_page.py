import tkinter as tk
from tkinter import *
from page import Page
from home_page      import *


import backend


class MainMenuPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        logo = PhotoImage(file = 'logo.png')

        ## Frame for Banner
        home_page       = HomePage(self)

        page_frame = tk.Frame(self)
        page_frame.pack(side="bottom", fill="both", expand=True)

        home_page.place     (in_=page_frame, x=0, y=0, relwidth=1, relheight=1)
        

        ## Frame for Buttons

        container_frame = Frame(self, width = 800, height = 480)
        container_frame.place(x = 400, y = 240, anchor = "center")

        banner = PhotoImage(file = 'banner.png')

        banner_image = Label(container_frame, image = banner, anchor = "nw")
        banner_image.place()

        center_buttons_frame = tk.Frame(container_frame)
        center_buttons_frame.place(x = 400, y = 240, anchor = "center", width=400, height=240, )

        #def auto_function():
        #    print("AUTO INITIALIZED!")

        #auto_button = Button(center_buttons_frame, text = "AUTO", command = auto_function, background="Red", foreground="white")
        #auto_button.place(x = 250, y = 240, anchor = "center", width = 100, height = 75)

        #def manual_function():
        #    print("MANUAL STARTED")

        manual_button = Button(center_buttons_frame, text = "MANUAL", command = home_page.show, background="Red", foreground="white")
        manual_button.place(x = 400, y = 240, anchor = "center", width = 100, height = 75)

        #def settings_function():
        #    print("SEETINGS DOES NOT WORK")

        #settings_button = Button(center_buttons_frame, text = "SETTINGS", command = settings_function, background="Red", foreground="white")
        #settings_button.place(x = 550, y = 240, anchor = "center", width = 100, height = 75)

        #power_button_frame = tk.Frame(container_frame)
        #power_button_frame.place(x = 795, y = 5, anchor = 'se')

        #power_button = Button(center_buttons_frame, image = logo, command = power_off_page.show)
        #power_button.place(x = 795, y = 5, anchor = 'se', width = 200, height = 200)

        



