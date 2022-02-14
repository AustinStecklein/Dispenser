import tkinter as tk
from page import Page
from numpad import *
import backend

class HomePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        ## Feed Buttons
        feed_button_frame = tk.Frame(self)
        feed_button_frame.pack(side = 'bottom', expand = False, anchor = 's', padx = 2)

        coarse_feed_button = tk.Button(feed_button_frame, text = "Coarse Feed", fg = "white", bg = "#c62b24", width="30", height="2", command = backend.coarse_feed)
        fine_feed_button = tk.Button(feed_button_frame, text = "Fine Feed", fg = "white", bg = "#c62b24", width="30", height="2", command = backend.fine_feed)
        bump_feed_button = tk.Button(feed_button_frame, text = "Bump", fg = "white", bg = "#c62b24", width="30", height="2", command = backend.bump_feed)
        
        bump_feed_button.pack(  side = 'right', expand = False, anchor = 's', padx = 2)
        fine_feed_button.pack(  side = 'right', expand = False, anchor = 's', padx = 2)
        coarse_feed_button.pack(side = 'right', expand = False, anchor = 's', padx = 2)

        ## Adjustments
        adjustments_frame = tk.Frame(self)
        adjustments_frame.pack(side = 'right', expand = False, anchor = 'se', padx = 2)

            # Speed Adjustments
        speed_frame = tk.Frame(self)
        speed_frame.pack(side = 'right', expand = False)

                # Speed Buttons
        speed_buttons_frame = tk.Frame(speed_frame)
        speed_buttons_frame.pack(side = 'bottom', expand = False)

        speed_minus_button = tk.Button(speed_buttons_frame, text = "Speed -", fg = "white", bg = "#c62b24", width="10", height="2", command = backend.decrease_speed)
        speed_minus_button.pack(side = 'bottom', expand = False)
        speed_plus_button = tk.Button(speed_buttons_frame, text = "Speed +", fg = "white", bg = "#c62b24", width="10", height="2", command = backend.increase_speed)
        speed_plus_button.pack(side = 'bottom', expand = False)

                # Speed Display
        speed_display_frame = tk.Frame(speed_frame)
        speed_display_frame.pack(side = 'bottom', expand = False, padx = 2)

        speed_display_label = Label(speed_display_frame, text = "Speed:", bg = 'light gray')
        speed_display_label.pack(side = 'top', expand = False)

        speed_display_value = Label(speed_display_frame, text = "0000", bg = 'light gray')
        speed_display_value.pack(side = 'top', expand = False)

        def get_speed():
            speed_value = backend.get_trickler_speed()
            speed_display_value.config(text = speed_value + '%')
            self.after(10, get_speed)
        
        get_speed()

            # Tilt Adjustments
        tilt_frame = tk.Frame(self)
        tilt_frame.pack(side = 'right', expand = False)

                # Tilt Buttons
        tilt_buttons_frame = tk.Frame(tilt_frame)
        tilt_buttons_frame.pack(side = 'bottom', expand = False)

        tilt_minus_button = tk.Button(tilt_buttons_frame, text = "Tilt -", fg = "white", bg = "#c62b24", width="10", height="2", command = backend.decrease_tilt)
        tilt_minus_button.pack(side = 'bottom', expand = False)
        tilt_plus_button = tk.Button(tilt_buttons_frame, text = "Tilt +", fg = "white", bg = "#c62b24", width="10", height="2", command = backend.increase_tilt)
        tilt_plus_button.pack(side = 'bottom', expand = False)

        
                # Tilt Display
        tilt_display_frame = tk.Frame(tilt_frame)
        tilt_display_frame.pack(side = 'bottom', expand = False, padx = 2)

        tilt_display_label = Label(tilt_display_frame, text = "Tilt:", bg = 'light gray')
        tilt_display_label.pack(side = 'top', expand = False)
        
        tilt_display_value = Label(tilt_display_frame, text = "0000", bg = 'light gray')
        tilt_display_value.pack(side = 'top', expand = False)

        def get_tilt():
            tilt_value = backend.get_trickler_tilt()
            tilt_display_value.config(text = tilt_value + '°')
            self.after(10, get_speed)
        
        get_tilt()
        

        ## Scale
        
            # Num pad
        num_pad_frame = tk.Frame(self)
        num_pad_frame.pack(side = 'bottom', expand = False, anchor = 's', padx = 2)
        
        num_pad = NumPad(num_pad_frame)
        num_pad.pack(side = "bottom", pady = 5, anchor = 's')

            # Target Weight
        target_weight_frame = tk.Frame(self)
        target_weight_frame.pack(side = 'bottom', expand = False, anchor = 's', padx = 2)

        target_weight = Label(target_weight_frame, text ="Target Weight: 0.00", bg = "light gray")
        target_weight.pack(side = "bottom", pady = 5, anchor = 's')

        def get_target_weight():
            target_value = backend.get_target()
            target_weight.config(text = "Target Weight: " + target_value)
            self.after(10, get_target_weight)
        
        get_target_weight()

            # Scale Weight

        scale_weight_frame = tk.Frame(self)
        scale_weight_frame.pack(side = 'bottom', expand = False, anchor = 's', padx = 2)

        scale_weight = Label(scale_weight_frame, text ="Scale Weight: 0.00", bg = "light gray")
        scale_weight.pack(side = "bottom", pady = 5, anchor = 's')

        def get_scale_reading():
            scale_reading = backend.read_scale()
            scale_weight.config(text = "Scale Weight: " + scale_reading)
            self.after(10, get_scale_reading)
        
        get_scale_reading()
