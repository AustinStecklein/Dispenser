import tkinter as tk
import tkinter.font as font
from pages.page import *
import pages.backend as backend
from pages.adjust_feeds_page        import *
from pages.brightness_sound_page    import * 
from pages.scale_config_page        import *
from pages.default_settings_page    import *
import pages.images.images as Images

class SettingsPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        scale_font = font.Font(family='Bahnschrift', size=26, weight='bold')

        # Settings Sub Pages
        self.scale_config_page      = ScaleConfigPage(self)
        self.brightness_sound_page  = BrightnessSoundPage(self)
        self.adjust_feeds_page      = AdjustFeedsPage(self)
        self.default_page           = DefaultSettingsPage(self)

        self.scale_config_page      .place(in_ = self, x = 0, y = 0, relwidth = 1, relheight = 1)
        self.brightness_sound_page  .place(in_ = self, x = 0, y = 0, relwidth = 1, relheight = 1)
        self.adjust_feeds_page      .place(in_ = self, x = 0, y = 0, relwidth = 1, relheight = 1)
        self.default_page           .place(in_ = self, x = 0, y = 0, relwidth = 1, relheight = 1)

        settings_frame = tk.Frame(self)
        settings_frame .place(in_ = self, x = 0, y = 0, relwidth = 1, relheight = 1)

        settings_label = tk.Label(settings_frame, text = "Settings", fg = "red", font = scale_font)
        settings_label.pack(side = 'top', expand = False, padx = 50, pady = 25)

        buttons_frame = tk.Frame(settings_frame)
        buttons_frame.pack(side = 'top', expand = True)

        right_buttons_frame = tk.Frame(buttons_frame)
        right_buttons_frame.pack(side = 'right', expand = True)

        left_buttons_frame = tk.Frame(buttons_frame)
        left_buttons_frame.pack(side = 'right', expand = True)

        scale_config_button     = tk.Button(left_buttons_frame,  image = Images.get('scale'),   borderwidth = 0, command = self.scale_config_page.show)
        adjust_feeds_button     = tk.Button(left_buttons_frame,  image = Images.get('adjust'),  borderwidth = 0, command = self.adjust_feeds_page.show)
        brightness_sound_button = tk.Button(right_buttons_frame, image = Images.get('bright'),  borderwidth = 0, command = self.brightness_sound_page.show)
        defaults_button         = tk.Button(right_buttons_frame, image = Images.get('restore'), borderwidth = 0, command = self.default_page.show)

        brightness_sound_button .pack(side = 'top', expand = False, padx = 25, pady = 20)
        defaults_button         .pack(side = 'top', expand = False, padx = 25, pady = 20)
        adjust_feeds_button     .pack(side = 'top', expand = False, padx = 25, pady = 20)
        scale_config_button     .pack(side = 'top', expand = False, padx = 25, pady = 20)
   
        self.scale_config_page      .lower()
        self.brightness_sound_page  .lower()
        self.adjust_feeds_page      .lower()