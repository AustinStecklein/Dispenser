import tkinter as tk
import pages.backend as backend
from pages.page import Page
import pages.images.images as Images
import tkinter.font as font

# https://python-course.eu/tkinter/sliders-in-tkinter.php
# A quality tkinter Slider guide

# TODO: prettier sliders if possible

class BrightnessSoundPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        page_font = font.Font(family='Bahnschrift', size=26, weight='bold')
        unit_font = font.Font(family='Bahnschrift', size=14, weight='bold')
        list_font = font.Font(family='Bahnschrift', size=10)
        
        haptics_list = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5', 'Option 6']
        haptics_list_var = tk.StringVar(value = haptics_list)

        banner_frame = tk.Frame(self)
        banner_frame .pack(side = 'top', expand = False, anchor = 'n')

        label = tk.Label(banner_frame, text="Settings: Brightness and Sound", font = page_font, fg = "#c62b24")
        label .pack(side = "top", fill = "both", expand = False)

        bottom_frame = tk.Frame(self)
        bottom_frame .pack(side = 'top', expand = True)


        left_frame = tk.Frame(bottom_frame)
        left_frame .pack(side = 'left', expand = False, padx = 50)

        right_frame = tk.Frame(bottom_frame)
        right_frame .pack(side = 'right', expand = False, padx = 50)


        haptic_frame = tk.Frame(left_frame)
        haptic_frame.pack(side = "bottom", expand = True)

        backlight_frame = tk.Frame(right_frame)
        backlight_frame.pack(side = "top", expand = True, pady = 5)

        notification_frame = tk.Frame(right_frame)
        notification_frame.pack(side = "top", expand = True, pady = 15)


        volume_frame = tk.Frame(right_frame)
        volume_frame.pack(side = "bottom", expand = True, pady = 5)


        backlight_slider = tk.Scale(backlight_frame, from_ = 0, to_ = 100, orient = tk.HORIZONTAL)
        backlight_slider .pack(side = 'top')
        backlight_slider .set(backend.get_backlight())

        backlight_label = tk.Label(backlight_frame, text = 'Backlight Intensity', font = unit_font)
        backlight_label .pack(side = 'top', expand = False)


        notification_volume_slider = tk.Scale(notification_frame, from_ = 0, to_ = 100, orient = tk.HORIZONTAL)
        notification_volume_slider .pack(side = 'top')
        notification_volume_slider .set(backend.get_notification_volume())
        
        notification_volume_label = tk.Label(notification_frame, text = 'Notification Volume', font = unit_font)
        notification_volume_label .pack(side = 'top', expand = False)

        
        button_volume_slider = tk.Scale(volume_frame, from_ = 0, to_ = 100, orient = tk.HORIZONTAL)
        button_volume_slider .pack(side = 'top')
        button_volume_slider .set(backend.get_button_volume())
        
        button_volume_label = tk.Label(volume_frame, text = 'Button Volume', font = unit_font)
        button_volume_label .pack(side = 'top', expand = False)


        haptic_label = tk.Label(haptic_frame, text = 'Haptic Feedback', font = unit_font)
        haptic_label .pack( side = 'top')

        haptic_select = tk.Listbox(haptic_frame, listvariable = haptics_list_var, height = 6, selectmode = 'single', font = list_font)
        haptic_select .pack(side = 'top')
        haptic_select .activate(backend.get_haptic())



        button_frame = tk.Frame(self)
        button_frame  .pack(side = "left", expand = False)

        save_button = tk.Button(button_frame,  borderwidth=0, image = Images.get('selections'), command = self.lower)
        save_button .pack(padx = 25)

        def update_settings():
            if backend.needsReset():
                backlight_slider            .set(50)
                notification_volume_slider  .set(50)
                button_volume_slider        .set(50)
                haptic_select               .activate(0)
                backend.finishReset()
            
            else:
                backend.set_backlight(backlight_slider.get())
                backend.set_notification_volume(notification_volume_slider.get())
                backend.set_button_volume(button_volume_slider.get())
                backend.set_haptic(haptic_select.curselection())

            self.after(10, update_settings)
        update_settings()
