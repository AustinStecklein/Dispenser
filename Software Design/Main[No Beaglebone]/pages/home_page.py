import tkinter as tk
from tkinter import *

from pages.page import Page
from pages.load_page      import *
from pages.settings_page  import *
from pages.calibrate_page import *
from pages.save_page      import *
from pages.view_page      import *

import tkinter.font as font
from pages.numpad import *
import pages.backend as backend
import pages.images.images as Images

units = backend.get_units()

class HomePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # Initialize other pages
        self.load_page      = LoadPage(self)
        self.settings_page  = SettingsPage(self)
        self.calibrate_page = CalibratePage(self)
        self.save_page      = SavePage(self)
        self.view_page      = ViewPage(self)
        
        self.load_page      .place(in_=self, x=0, y=0, relwidth=1, relheight=1)
        self.save_page      .place(in_=self, x=0, y=0, relwidth=1, relheight=1)
        self.calibrate_page .place(in_=self, x=0, y=0, relwidth=1, relheight=1)
        self.settings_page  .place(in_=self, x=0, y=0, relwidth=1, relheight=1)
        self.view_page      .place(in_=self, x=0, y=0, relwidth=1, relheight=1)

        # Sets the Home_Page
        home_page = tk.Frame(self)
        home_page .place(in_=self, x=0, y=0, relwidth=1, relheight=1)

        ## Num Pad
        numpad_frame = tk.Frame(home_page)
        numpad_frame.pack(side = 'left', padx = 4)

        numpad = NumPad(numpad_frame)
        numpad.pack()

        # Splits the Page in Half Vertically and Contains all the Buttons and Values on the Right Side
        right_frame = tk.Frame(home_page)
        right_frame.pack(side = 'right', expand = True)

        # Load, Save and View Container
        top_buttons_frame = tk.Frame(right_frame)
        top_buttons_frame.pack(side = 'top', pady = 4)

        # Load, Save and View Buttons
        load_button = tk.Button(top_buttons_frame, command = self.load_page.show, width = 100, height = 50, image = Images.get('load'), borderwidth = 0)
        save_button = tk.Button(top_buttons_frame, command = self.save_page.show, width = 100, height = 50, image = Images.get('save'), borderwidth = 0)
        view_button = tk.Button(top_buttons_frame, command = self.view_page.show, width = 100, height = 50, image = Images.get('view'), borderwidth = 0)

        save_button.pack(side = 'left', expand = False, padx = 8)
        load_button.pack(side = 'left', expand = False, padx = 8)
        view_button.pack(side = 'left', expand = False, padx = 8)
        

        # Unit Selector
        def popup():

            # Starts a new Screen that will be on top of the main screen and sets its dimensions, with the attribute of the not being modifiable by the user
            popup = tk.Toplevel()
            popup.geometry('480x288')
            popup.resizable(height=False, width=False)

            # Allows the units variable to be editted
            global units

            # Font for the text in the Buttons
            unit_font = font.Font(family='Bahnschrift', size=16, weight='bold')

            # Sets the units variable to the desired units; sends that choice to the backend to be saved; closes the popup; then updates the get_units function
            def g_units():
                global units
                units = "g"
                backend.new_units("g")
                popup.destroy()
                home_page.after(10, backend.get_units)

            def lb_units():
                global units
                units = "lb"
                backend.new_units("lb")
                popup.destroy()
                home_page.after(10, backend.get_units)

            def gr_units():
                global units
                units = "gr"
                backend.new_units("gr")
                popup.destroy()
                home_page.after(10, backend.get_units)

            def oz_units():
                global units
                units = "oz"
                backend.new_units("oz")
                popup.destroy()
                home_page.after(10, backend.get_units)

            def ct_units():
                global units
                units = "ct"
                backend.new_units("ct")
                popup.destroy()
                home_page.after(10, backend.get_units)

            def tl_units():
                global units
                units = "tl"
                backend.new_units("tl")
                popup.destroy()
                home_page.after(10, backend.get_units)


            # If the current units is already selected, the user cannot select those units and must choose a different one
            if (units == "gr"):
                gr_button = tk.Button(popup, text = "Grains: (gr)", font = unit_font, width = 5,borderwidth = 0,)
                gr_button.config(relief = SUNKEN)
                gr_button.grid(row = 1, column = 0, ipadx = 50, ipady = 2, pady = 5, padx = 25)
            
            else:
                gr_button = tk.Button(popup, text = "Grains: (gr)", font = unit_font, width = 5,borderwidth = 0,
                                        command = gr_units,)
                gr_button.grid(row = 1, column = 0, ipadx = 50, ipady = 2, pady = 5, padx = 25)


            if (units == "g"):
                g_button = tk.Button(popup, text = "Grams: (g)", font = unit_font, width = 5,borderwidth = 0,)
                g_button.config(relief = SUNKEN)
                g_button.grid(row = 2, column = 0, ipadx = 50, ipady = 2, pady = 5, padx = 25)
            
            else: 
                g_button = tk.Button(popup, text = "Grams: (g)", font = unit_font, width = 5,borderwidth = 0,
                                        command = g_units)
                g_button.grid(row = 2, column = 0, ipadx = 50, ipady = 2, pady = 5, padx = 25)


            if (units == "lb"):
                lb_button = tk.Button(popup, text = "Pounds: (lb)", font = unit_font, width = 5,borderwidth = 0,)
                lb_button.config(relief = SUNKEN)
                lb_button.grid(row = 3, column = 0, ipadx = 50, ipady = 2, pady = 5, padx = 25)
            
            else: 
                lb_button = tk.Button(popup, text = "Pounds: (lb)", font = unit_font, width = 5,borderwidth = 0,
                                        command = lb_units)
                lb_button.grid(row = 3, column = 0, ipadx = 50, ipady = 2, pady = 5, padx = 25)

            
            if (units == "oz"):
                oz_button = tk.Button(popup, text = "Ounces: (oz)", font = unit_font, width = 5,borderwidth = 0,)
                oz_button.config(relief = SUNKEN)
                oz_button.grid(row = 1, column = 1, ipadx = 50, ipady = 2, pady = 5, padx = 25)
            
            else:
                oz_button = tk.Button(popup, text = "Ounces: (oz)", font = unit_font, width = 5,borderwidth = 0,
                                        command = oz_units,)
                oz_button.grid(row = 1, column = 1, ipadx = 50, ipady = 2, pady = 5, padx = 25)


            if (units == "ct"):
                ct_button = tk.Button(popup, text = "Carat: (ct)", font = unit_font, width = 5,borderwidth = 0,)
                ct_button.config(relief = SUNKEN)
                ct_button.grid(row = 2, column = 1, ipadx = 50, ipady = 2, pady = 5, padx = 25)
            
            else: 
                ct_button = tk.Button(popup, text = "Carat: (ct)", font = unit_font, width = 5,borderwidth = 0,
                                        command = ct_units)
                ct_button.grid(row = 2, column = 1, ipadx = 50, ipady = 2, pady = 5, padx = 25)


            if (units == "tl"):
                tl_button = tk.Button(popup, text = "Tael: (tl)", font = unit_font, width = 5,borderwidth = 0,)
                tl_button.config(relief = SUNKEN)
                tl_button.grid(row = 3, column = 1, ipadx = 50, ipady = 2, pady = 5, padx = 25)
            
            else: 
                tl_button = tk.Button(popup, text = "Tael: (tl)", font = unit_font, width = 5,borderwidth = 0,
                                        command = tl_units)
                tl_button.grid(row = 3, column = 1, ipadx = 50, ipady = 2, pady = 5, padx = 25)

            close_button = tk.Button(popup, text = "Close", font = unit_font, fg = "white", bg = "#c62b24", 
                                    width = 5, borderwidth = 0, command = popup.destroy)
            close_button.grid(row = 4, column = 1, ipadx = 50, ipady = 2, pady = 25, padx = 25)

        
        # Scale Weight Container
        scale_weight_frame = tk.Frame(right_frame)
        scale_weight_frame.pack(side = 'top', expand = False, padx = 2)

        # Scale Weight Number
        scale_font = font.Font(family='Bahnschrift', size=56, weight='bold') # size reduced from 78
        scale_weight = Label(scale_weight_frame, text ="00.00", bg = "light gray")
        scale_weight['font'] = scale_font
        scale_weight.pack(side = "left", pady = 5, anchor = 's')

        # Scale Units which has an attached function to change units
        scale_unit_font = font.Font(family='Bahnschrift', size=20, weight='bold')
        scale_unit = Button(scale_weight_frame, text = 'gr', bg = "light gray", command = popup,borderwidth = 0,)
        scale_unit['font'] = scale_unit_font
        scale_unit.pack(side = "left", pady = 5, anchor = 'sw')

        
        # Target Weight Containter
        small_displays_frame = tk.Frame(right_frame)
        small_displays_frame.pack(side = "top", expand = True)

        target_weight_frame = tk.Frame(small_displays_frame)
        target_weight_frame.pack(side = 'left', expand = True, padx = 2)

        target_font = font.Font(family='Bahnschrift', size=16, weight='bold')
        target_weight = Label(target_weight_frame, text ="Target Weight: 0.00")
        target_weight['font'] = target_font
        target_weight.pack(side = "left", pady = 5, anchor = 's')

        # Speed Container
        speed_display_frame = tk.Frame(small_displays_frame)
        speed_display_frame.pack(side = 'right', expand = True, padx = 2)

        speed_font = font.Font(family='Bahnschrift', size=16, weight='bold')

        speed_display_label = Label(speed_display_frame, text = "Speed:")
        speed_display_label['font'] = speed_font
        speed_display_label.pack(side = 'left', expand = False)

        target_font = font.Font(family='Bahnschrift', size=16, weight='bold')
        speed_display_value = Label(speed_display_frame, text = "0000")
        speed_display_value['font'] = speed_font
        speed_display_value.pack(side = 'left', expand = False)

        # Coarse, Fine Feed, and Bump Container
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


        # Clear, Calibrate, and Settings Container
        bottom_buttons_frame = tk.Frame(right_frame)
        bottom_buttons_frame.pack(side = 'top', anchor = 's', pady = 4)

        clear_button = tk.Button(bottom_buttons_frame, image = Images.get('clear'), 
                                    width="100", height="50", command = backend.numpad_clear, borderwidth=0)
        calibrate_button = tk.Button(bottom_buttons_frame, image = Images.get('calibrate'), 
                                    width="100", height="50", command = self.calibrate_page.show, borderwidth=0)
        settings_button = tk.Button(bottom_buttons_frame, image = Images.get('settings'), 
                                    width="100", height="50", command = self.settings_page.show, borderwidth=0)
                                
        clear_button    .pack(side = 'left', expand = False, padx = 8)
        calibrate_button.pack(side = 'left', expand = False, padx = 8)
        settings_button .pack(side = 'left', expand = False, padx = 8)

        # Continously called to ensure the units stay updated
        def update_units():
            updated_units = backend.get_units()
            scale_unit.config(text = updated_units)
            scale_reading = backend.read_scale()
            scale_weight.config(text = scale_reading)
            target_value = backend.get_target()
            target_weight.config(text = "Target Weight: " + target_value)
            speed_value = backend.get_trickler_speed()
            speed_display_value.config(text = speed_value + '%')
            home_page.after(10, update_units)

        # Calls update_units function to ensure that all the units stay up to date
        update_units()

    # Lowers all pages to reveal the Home Page
    def go_home(self):
        self.load_page.lower()
        self.save_page.lower()
        self.settings_page.lower()
        self.calibrate_page.lower()
        self.view_page.lower()

