import tkinter as tk
from pages.page import Page

class AdjustFeedsPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        label = tk.Label(self, text="Settings: Adjust Feeds")
        label.pack(side = "top", fill="both", expand = False)

        bottom_frame = tk.Frame(self)
        bottom_frame .pack(side = 'top', expand = True)

        bump_frame = tk.Frame(bottom_frame)
        bump_frame .pack(side = 'right', expand = True, padx = 10)
        
        bump_button = tk.Button(bump_frame, text = 'Bump')
        bump_button .pack(side = 'top', pady = 2)

        bump_display = tk.Label(bump_frame, text = '0.01', bg = 'light gray')
        bump_display .pack(side = 'top', pady = 2)

        bump_select_frame = tk.Frame(bump_frame)
        bump_select_frame .pack(side = 'top', pady = 2)

        bump_left_arrow = tk.Button(bump_select_frame, text = '<', 
                                    fg = "white", bg = "#c62b24", width="2", height="1")
        bump_left_arrow .pack(side = 'left')

        bump_range_label = tk.Label(bump_select_frame, text = '0-0.5gn')
        bump_range_label .pack(side = 'left')
        
        bump_right_arrow = tk.Button(bump_select_frame, text = '>', 
                                    fg = "white", bg = "#c62b24", width="2", height="1")
        bump_right_arrow .pack(side = 'left')

        fine_frame = tk.Frame(bottom_frame)
        fine_frame .pack(side = 'right', expand = True, padx = 10)

        fine_frame = tk.Frame(bottom_frame)
        fine_frame .pack(side = 'right', expand = True, padx = 10)
        
        fine_button = tk.Button(fine_frame, text = 'Fine')
        fine_button .pack(side = 'top', pady = 2)

        fine_display = tk.Label(fine_frame, text = '0.1', bg = 'light gray')
        fine_display .pack(side = 'top', pady = 2)

        fine_select_frame = tk.Frame(fine_frame)
        fine_select_frame .pack(side = 'top', pady = 2)

        fine_left_arrow = tk.Button(fine_select_frame, text = '<', 
                                    fg = "white", bg = "#c62b24", width="2", height="1")
        fine_left_arrow .pack(side = 'left')

        fine_range_label = tk.Label(fine_select_frame, text = '0-1gn')
        fine_range_label .pack(side = 'left')
        
        fine_right_arrow = tk.Button(fine_select_frame, text = '>', 
                                    fg = "white", bg = "#c62b24", width="2", height="1")
        fine_right_arrow .pack(side = 'left')

        coarse_frame = tk.Frame(bottom_frame)
        coarse_frame .pack(side = 'right', expand = True, padx = 10)

        coarse_frame = tk.Frame(bottom_frame)
        coarse_frame .pack(side = 'right', expand = True, padx = 10)
        
        coarse_button = tk.Button(coarse_frame, text = 'Coarse')
        coarse_button .pack(side = 'top', pady = 2)

        coarse_display = tk.Label(coarse_frame, text = '1.00', bg = 'light gray')
        coarse_display .pack(side = 'top', pady = 2)

        coarse_select_frame = tk.Frame(coarse_frame)
        coarse_select_frame .pack(side = 'top', pady = 2)

        coarse_left_arrow = tk.Button(coarse_select_frame, text = '<', 
                                    fg = "white", bg = "#c62b24", width="2", height="1")
        coarse_left_arrow .pack(side = 'left')

        coarse_range_label = tk.Label(coarse_select_frame, text = '0-10gn')
        coarse_range_label .pack(side = 'left')
        
        coarse_right_arrow = tk.Button(coarse_select_frame, text = '>', 
                                    fg = "white", bg = "#c62b24", width="2", height="1")
        coarse_right_arrow .pack(side = 'left')
    



        save_button = tk.Button(self, text = 'Save Adjustments', 
                              fg = "white", bg = "#c62b24", width="15", height="2", command = self.lower)

        save_button .pack(anchor = 'w')