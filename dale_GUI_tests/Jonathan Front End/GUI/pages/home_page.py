import tkinter as tk
from pages.page import Page
from modules.numpad import *
import modules.backend as backend
from pages.load_page      import *
from pages.save_page      import *
from pages.settings_page      import *
from PIL import ImageTk, Image
from tkinter import *
import Images

class HomePage(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # Initialize other pages
        self.load_page = LoadPage(self)
        self.load_page .place(in_=self, x=0, y=0, relwidth=1, relheight=1)

        self.save_page = SavePage(self)
        self.save_page .place(in_=self, x=0, y=0, relwidth=1, relheight=1)

        self.settings_page = SettingsPage(self)
        self.settings_page .place(in_=self, x=0, y=0, relwidth=1, relheight=1)

        home_page = tk.Frame(self)
        home_page .place(in_=self, x=0, y=0, relwidth=1, relheight=1)

        ## Num Pad
        numpad_frame = tk.Frame(home_page)
        numpad_frame.pack(side = 'left', padx = 4)

        numpad = NumPad(numpad_frame)
        numpad.pack()

        ## load / save / view
        right_frame = tk.Frame(home_page)
        right_frame.pack(side = 'right', expand = True)

        top_buttons_frame = tk.Frame(right_frame)
        top_buttons_frame.pack(side = 'top', pady = 4)


        load_button = tk.Button(top_buttons_frame, command = self.load_page.show, width = 100, height= 50, image = Images.get('load'), borderwidth=0)
        save_button = tk.Button(top_buttons_frame, command = self.save_page.show, width = 100, height= 50, image = Images.get('save'), borderwidth=0)
        view_button = tk.Button(top_buttons_frame, image = Images.get('view'), width="100", height="50", command = backend.power_off, borderwidth=0)

        save_button.pack(side = 'left', expand = False, padx = 8)
        load_button.pack(side = 'left', expand = False, padx = 8)
        view_button.pack(side = 'left', expand = False, padx = 8)

        ## display

            # Scale Weight
        scale_weight_frame = tk.Frame(right_frame)
        scale_weight_frame.pack(side = 'top', expand = False, padx = 2)


        scale_font = font.Font(family='Bahnschrift', size=96, weight='bold')
        scale_weight = Label(scale_weight_frame, text ="00.00", bg = "light gray")
        scale_weight['font'] = scale_font
        scale_weight.pack(side = "left", pady = 5, anchor = 's')

        scale_unit_font = font.Font(family='Bahnschrift', size=20, weight='bold')
        scale_unit = Label(scale_weight_frame, text ="gr", bg = "light gray")
        scale_unit['font'] = scale_unit_font
        scale_unit.pack(side = "left", pady = 5, anchor = 'sw')

        def get_scale_reading():
            scale_reading = backend.read_scale()
            scale_weight.config(text = scale_reading)
            home_page.after(10, get_scale_reading)
        
        get_scale_reading()

            # Target Weight
        small_displays_frame = tk.Frame(right_frame)
        small_displays_frame.pack(side = "top", expand = True)

        target_weight_frame = tk.Frame(small_displays_frame)
        target_weight_frame.pack(side = 'left', expand = True, padx = 2)

        target_weight = Label(target_weight_frame, text ="Target Weight: 0.00", bg = "light gray")
        target_weight.pack(side = "left", pady = 5, anchor = 's')

        def get_target_weight():
            target_value = backend.get_target()
            target_weight.config(text = "Target Weight: " + target_value)
            home_page.after(10, get_target_weight)
        
        get_target_weight()

            # Speed Display
        speed_display_frame = tk.Frame(small_displays_frame)
        speed_display_frame.pack(side = 'right', expand = True, padx = 2)

        speed_display_label = Label(speed_display_frame, text = "Speed:", bg = 'light gray')
        speed_display_label.pack(side = 'left', expand = False)

        speed_display_value = Label(speed_display_frame, text = "0000", bg = 'light gray')
        speed_display_value.pack(side = 'left', expand = False)

        def get_speed():
            speed_value = backend.get_trickler_speed()
            speed_display_value.config(text = speed_value + '%')
            home_page.after(10, get_speed)
        
        get_speed()

        ## feed buttons
        feed_button_frame = tk.Frame(right_frame)
        feed_button_frame.pack(side = 'top', expand = False, anchor = 's', pady = 4)

        coarse_feed_button = tk.Button( feed_button_frame, image = Images.get('coarse'), 
                                        width="100", height="50", command = backend.coarse_feed, borderwidth=0)
        fine_feed_button = tk.Button(   feed_button_frame, image = Images.get('fine'), 
                                        width="100", height="50", command = backend.fine_feed, borderwidth=0)
        bump_feed_button = tk.Button(   feed_button_frame, image = Images.get('bump'), 
                                        width="100", height="50", command = backend.bump_feed, borderwidth=0)
        
        bump_feed_button.pack(  side = 'right', expand = False, anchor = 's', padx = 8)
        fine_feed_button.pack(  side = 'right', expand = False, anchor = 's', padx = 8)
        coarse_feed_button.pack(side = 'right', expand = False, anchor = 's', padx = 8)



        ## clear / calibrate / settings

        bottom_buttons_frame = tk.Frame(right_frame)
        bottom_buttons_frame.pack(side = 'top', anchor = 's', pady = 4)

        clear_button = tk.Button(bottom_buttons_frame, image = Images.get('clear'), 
                                    width="100", height="50", command = backend.numpad_clear, borderwidth=0)
        calibrate_button = tk.Button(bottom_buttons_frame, image = Images.get('calibrate'), 
                                    width="100", height="50", command = backend.power_off, borderwidth=0)
        settings_button = tk.Button(bottom_buttons_frame, image = Images.get('settings'), 
                                    width="100", height="50", command = self.settings_page.show, borderwidth=0)
                                
        clear_button    .pack(side = 'left', expand = False, padx = 8)
        calibrate_button.pack(side = 'left', expand = False, padx = 8)
        settings_button .pack(side = 'left', expand = False, padx = 8)

    def go_home(self):
        self.load_page.lower()
        self.save_page.lower()
