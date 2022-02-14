import tkinter as tk
from tkinter import *
from page import Page
import backend


class MainMenuPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        ## Frame for Banner
        banner = PhotoImage(file = 'dale_GUI_tests\Jonathan Front End\Merged Files\\banner.png')

        banner_frame = tk.Frame(self)
        banner_frame.pack(side = 'top', expand = False, anchor = 'nw', padx = 2)

        banner_image = tk.Label(banner_frame, image = banner, )
        banner_image.place(x = 5, y = 5, anchor = "ne")

        ## Frame for Buttons

        center_buttons_frame = tk.Frame(self)
        center_buttons_frame.place(x = 400, y = 240, anchor = "center", width = "500", height = "150")

        def auto_function():
            print("AUTO INITIALIZED!")

        auto_button = Button(center_buttons_frame, text = "AUTO", width = "100", height = "75", command = auto_function, background="Red", foreground="white")
        auto_button.place(x = 250, y = 240, anchor = "center")

        def manual_function():
            print("MANUAL STARTED")

        manual_button = Button(center_buttons_frame, text = "MANUAL", width = "100", height = "75", command = manual_function, background="Red", foreground="white")
        manual_button.place(x = 400, y = 240, anchor = "center")

        def settings_function():
            print("SEETINGS DOES NOT WORK")

        manual_button = Button(center_buttons_frame, text = "SETTINGS", width = "100", height = "75", command = settings_function, background="Red", foreground="white")
        manual_button.place(x = 550, y = 240, anchor = "center")

        



