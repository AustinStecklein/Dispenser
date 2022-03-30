import tkinter as tk
from pages.page import Page
import pages.backend as backend
import pages.images.images as Images
import tkinter.font as font

# TODO: arrow buttons

class LoadPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # Font Sizes and Styles
        page_font = font.Font(family='Bahnschrift', size=16, weight='bold')
        unit_font = font.Font(family='Bahnschrift', size=14, weight='bold')
        previous_font = font.Font(family='Bahnschrift', size=12, weight='bold')

        def display_presets():

            # Clear out the presets being displayed
            for widget in bottom_frame.winfo_children():
                widget.destroy()

            # Refresh Load List
            load_list = backend.get_load_list()


            # Sets the Current Page and the Total Amount of Pages needed
            current_page = int(backend.get_page())

            current_loads = load_list[ (current_page - 1) * 5 : ( (current_page - 1) * 5 ) + 5 ]

            # Make a button for each preset on the current page
            for load_string in current_loads:
                load_frame = tk.Frame(bottom_frame)
                load_frame.pack(side = 'top', expand = False, anchor = 'w', pady = 2)

                load_button = tk.Button(load_frame, text = load_string, bg = "light gray", borderwidth = 0, font = unit_font, 
                                        width = 25, height = 2, command = lambda string = load_string: load_preset(string) )
                load_button.pack(side = 'right', expand = False)

        # Next and Previous Page Functions
        def next_page():
            if int(backend.get_page()) < backend.total_pages(): 
                backend.next_page()
                display_presets()
        
        def prev_page():
            if int(backend.get_page()) > 1:
                backend.prev_page()
                display_presets()

        # Sets the Current Page based on the backend load_page function
        self.current_page = backend.load_page

        # Previously Saved Label
        heading_label = tk.Label(self, text = 'Select a previously saved configuration to load', bg = 'light gray', font = previous_font)
        heading_label .pack(side = 'top', expand = False, anchor = 'w')

        # Container for Arrow Buttons and Page Number 
        arrows_frame = tk.Frame(self)
        arrows_frame .pack()

        left_arrow = tk.Button(arrows_frame, text = '<', fg = "white", bg = "#c62b24", width="2", height="1", command = prev_page)
        left_arrow .pack(side = 'left', padx = 10)

        page_number_label = tk.Label(arrows_frame, text = '1', font = page_font)
        page_number_label .pack(side = 'left', padx = 10)
        
        right_arrow = tk.Button(arrows_frame, text = '>', fg = "white", bg = "#c62b24", width="2", height="1", command = next_page)
        right_arrow .pack(side = 'left', padx = 10)

        # Updates Page Number 
        def get_page_number():
            new_number = backend.get_page()
            page_number_label.config(text = new_number)
            arrows_frame.after(10, get_page_number)
        get_page_number()

        # Loads the Files 
        def load_preset(load_string):
            backend.load_preset(load_string)
            self.lower()

        # Bottom Frame for buffer
        bottom_frame = tk.Frame(self)
        bottom_frame .pack()

        # Calls display_presets function to display the Load Cards
        display_presets()



