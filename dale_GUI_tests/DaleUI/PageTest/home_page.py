import tkinter as tk
from page import Page
from numpad import *

def coarse_feed():
    print('coarse feed')

def fine_feed():
    print('fine feed')

def bump_feed():
    print('bump feed')

class HomePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # Feed Buttons
        feed_button_frame = tk.Frame(self)
        feed_button_frame.pack(side = 'bottom', expand = False, anchor = 's', padx = 2)

        coarse_feed_button = tk.Button(feed_button_frame, text = "Coarse Feed", fg = "white", bg = "#c62b24", width="30", height="2", command = coarse_feed)
        fine_feed_button = tk.Button(feed_button_frame, text = "Fine Feed", fg = "white", bg = "#c62b24", width="30", height="2", command = fine_feed)
        bump_feed_button = tk.Button(feed_button_frame, text = "Bump", fg = "white", bg = "#c62b24", width="30", height="2", command = bump_feed)
        
        bump_feed_button.pack(  side = 'right', expand = False, anchor = 's', padx = 2)
        fine_feed_button.pack(  side = 'right', expand = False, anchor = 's', padx = 2)
        coarse_feed_button.pack(side = 'right', expand = False, anchor = 's', padx = 2)

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

        # Scale Weight
        scale_weight_frame = tk.Frame(self)
        scale_weight_frame.pack(side = 'bottom', expand = False, anchor = 's', padx = 2)

        scale_weight = Label(scale_weight_frame, text ="Scale Weight: 0.00", bg = "light gray")
        scale_weight.pack(side = "bottom", pady = 5, anchor = 's')

        # Adjustments
        adjustments_frame = tk.Frame(self)
        adjustments_frame.pack(side = 'right', expand = False, anchor = 'se', padx = 2)


