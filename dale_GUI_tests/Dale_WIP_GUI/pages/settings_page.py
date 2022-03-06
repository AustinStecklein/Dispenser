import tkinter as tk
from pages.page import *
import modules.backend as backend
from pages.adjust_feeds_page        import *
from pages.brightness_sound_page    import * 
from pages.scale_config_page        import *
from pages.default_settings_page    import *

class SettingsPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

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

        settings_label = tk.Label(settings_frame, text = "Settings", bg = "light gray")
        settings_label.pack(side = 'top', expand = False, padx = 50, pady = 50)

        buttons_frame = tk.Frame(settings_frame)
        buttons_frame.pack(side = 'top', expand = True)

        right_buttons_frame = tk.Frame(buttons_frame)
        right_buttons_frame.pack(side = 'right', expand = True)

        left_buttons_frame = tk.Frame(buttons_frame)
        left_buttons_frame.pack(side = 'right', expand = True)

        scale_config_button     = tk.Button(left_buttons_frame, text = "Scale Config", fg = "white", bg = "#c62b24",
                                            width="30", height="2", command = self.scale_config_page.show)
        adjust_feeds_button     = tk.Button(left_buttons_frame, text = "Adjust Feeds", fg = "white", bg = "#c62b24",
                                            width="30", height="2", command = self.adjust_feeds_page.show)
        brightness_sound_button = tk.Button(right_buttons_frame, text = "Brightness & Sounds", fg = "white", bg = "#c62b24",
                                            width="30", height="2", command = self.brightness_sound_page.show)
        defaults_button         = tk.Button(right_buttons_frame, text = "Restore to Defaults", fg = "white", bg = "#c62b24",
                                            width="30", height="2", command = self.default_page.show)


        brightness_sound_button .pack(side = 'top', expand = False, padx = 50, pady = 20)
        defaults_button         .pack(side = 'top', expand = False, padx = 50, pady = 20)
        adjust_feeds_button     .pack(side = 'top', expand = False, padx = 50, pady = 20)
        scale_config_button     .pack(side = 'top', expand = False, padx = 50, pady = 20)

        
        self.scale_config_page      .lower()
        self.brightness_sound_page  .lower()
        self.adjust_feeds_page      .lower()