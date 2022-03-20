import tkinter as tk
import modules.backend as backend
from pages.page import Page
import modules.image_loader as Images

# https://python-course.eu/tkinter/sliders-in-tkinter.php
# A quality tkinter Slider guide

class BrightnessSoundPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        
        haptics_list = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5', 'Option 6']
        haptics_list_var = tk.StringVar(value = haptics_list)

        banner_frame = tk.Frame(self)
        banner_frame .pack(side = 'top', expand = False, anchor = 'n')

        label = tk.Label(banner_frame, text="Settings: Brightness and Sound")
        label .pack(side = "top", fill = "both", expand = False)

        bottom_frame = tk.Frame(self)
        bottom_frame .pack(side = 'top', expand = True)

        left_frame = tk.Frame(bottom_frame)
        left_frame .pack(side = 'left', expand = True, padx = 10)

        right_frame = tk.Frame(bottom_frame)
        right_frame .pack(side = 'left', expand = True, padx = 10)

        backlight_slider = tk.Scale(left_frame, from_ = 0, to_ = 100, orient = tk.HORIZONTAL)
        backlight_slider .pack(side = 'top')

        backlight_label = tk.Label(left_frame, text = 'Backlight Intensity')
        backlight_label .pack(side = 'top', expand = False)

        notification_volume_slider = tk.Scale(right_frame, from_ = 0, to_ = 100, orient = tk.HORIZONTAL)
        notification_volume_slider .pack(side = 'top')
        
        notification_volume_label = tk.Label(right_frame, text = 'Notification Volume')
        notification_volume_label .pack(side = 'top', expand = False)
        
        button_volume_slider = tk.Scale(right_frame, from_ = 0, to_ = 100, orient = tk.HORIZONTAL)
        button_volume_slider .pack(side = 'top')
        
        button_volume_label = tk.Label(right_frame, text = 'Button Volume')
        button_volume_label .pack(side = 'top', expand = False)

        haptic_label = tk.Label(left_frame, text = 'Haptic Feedback')
        haptic_label .pack( side = 'top')

        haptic_select = tk.Listbox(left_frame, listvariable = haptics_list_var, height = 6, selectmode = 'extended')
        haptic_select .pack(side = 'top')

        save_button = tk.Button(right_frame,  borderwidth=0, image = Images.get('selections'), command = self.lower)
        save_button .pack()
