import tkinter as tk
from pages.page import Page
import pages.backend as backend
import pages.images.images as Images

class AdjustFeedsPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        label = tk.Label(self, text="Settings: Adjust Feeds")
        label.pack(side = "top", fill="both", expand = False)

        bottom_frame = tk.Frame(self)
        bottom_frame .pack(side = 'top', expand = True)

        # Bump

        

        bump_frame = tk.Frame(bottom_frame)
        bump_frame .pack(side = 'right', expand = True, padx = 10)
        
        bump_button = tk.Button(bump_frame, image = Images.get('adjust_bump'), borderwidth=0, command = backend.bump_feed)
        bump_button .pack(side = 'top', pady = 2)

        bump_display = tk.Label(bump_frame, text = '0.01', bg = 'light gray')
        bump_display .pack(side = 'top', pady = 2)

        bump_select_frame = tk.Frame(bump_frame)
        bump_select_frame .pack(side = 'top', pady = 2)

        bump_left_arrow = tk.Button(bump_select_frame, text = '<', 
                                    fg = "white", bg = "#c62b24", width="2", height="1", 
                                    command = backend.decrease_bump)
        bump_left_arrow .pack(side = 'left')

        bump_range_label = tk.Label(bump_select_frame, text = '0-0.5gn')
        bump_range_label .pack(side = 'left')
        
        bump_right_arrow = tk.Button(bump_select_frame, text = '>', 
                                    fg = "white", bg = "#c62b24", width="2", height="1", 
                                    command = backend.increase_bump)
        bump_right_arrow .pack(side = 'left')
        
        def display_bump():
            bump_strength = str(backend.bump_strength)
            bump_display.config(text = bump_strength)
            self.after(10, display_bump)
        display_bump()
            
        # Fine

        fine_frame = tk.Frame(bottom_frame)
        fine_frame .pack(side = 'right', expand = True, padx = 10)

        fine_frame = tk.Frame(bottom_frame)
        fine_frame .pack(side = 'right', expand = True, padx = 10)
        
        fine_button = tk.Button(fine_frame, image = Images.get('adjust_fine'), borderwidth=0, command = backend.fine_feed)
        fine_button .pack(side = 'top', pady = 2)

        fine_display = tk.Label(fine_frame, text = '0.1', bg = 'light gray')
        fine_display .pack(side = 'top', pady = 2)

        fine_select_frame = tk.Frame(fine_frame)
        fine_select_frame .pack(side = 'top', pady = 2)

        fine_left_arrow = tk.Button(fine_select_frame, text = '<', 
                                    fg = "white", bg = "#c62b24", width="2", height="1", 
                                    command = backend.decrease_fine)
        fine_left_arrow .pack(side = 'left')

        fine_range_label = tk.Label(fine_select_frame, text = '0-1gn')
        fine_range_label .pack(side = 'left')
        
        fine_right_arrow = tk.Button(fine_select_frame, text = '>', 
                                    fg = "white", bg = "#c62b24", width="2", height="1", 
                                    command = backend.increase_fine)
        fine_right_arrow .pack(side = 'left')
        
        def display_fine():
            fine_strength = str(backend.fine_strength)
            fine_display.config(text = fine_strength)
            self.after(10, display_fine)
        display_fine()

        # Coarse

        coarse_frame = tk.Frame(bottom_frame)
        coarse_frame .pack(side = 'right', expand = True, padx = 10)

        coarse_frame = tk.Frame(bottom_frame)
        coarse_frame .pack(side = 'right', expand = True, padx = 10)
        
        coarse_button = tk.Button(coarse_frame, image = Images.get('adjust_coarse'), borderwidth=0, command = backend.coarse_feed)
        coarse_button .pack(side = 'top', pady = 2)

        coarse_display = tk.Label(coarse_frame, text = '1.00', bg = 'light gray')
        coarse_display .pack(side = 'top', pady = 2)

        coarse_select_frame = tk.Frame(coarse_frame)
        coarse_select_frame .pack(side = 'top', pady = 2)

        coarse_left_arrow = tk.Button(coarse_select_frame, text = '<', 
                                    fg = "white", bg = "#c62b24", width="2", height="1", 
                                    command = backend.decrease_coarse)
        coarse_left_arrow .pack(side = 'left')

        coarse_range_label = tk.Label(coarse_select_frame, text = '0-10gn')
        coarse_range_label .pack(side = 'left')
        
        coarse_right_arrow = tk.Button(coarse_select_frame, text = '>', 
                                    fg = "white", bg = "#c62b24", width="2", height="1", 
                                    command = backend.increase_coarse)
        coarse_right_arrow .pack(side = 'left')
        
        def display_coarse():
            coarse_strength = str(backend.coarse_strength)
            coarse_display.config(text = coarse_strength)
            self.after(10, display_coarse)
        display_coarse()

        # Save button
    
        
        save_button = tk.Button(self, text = 'IMAGE NOT FOUND', borderwidth=0, command = self.lower)
        #save_button = tk.Button(self, image = Images.get('save adjustments'), borderwidth=0, command = self.lower)
        save_button .pack(anchor = 'w')