import tkinter as tk
from pages.page import Page
import pages.backend as backend
import tkinter.font as font
from pages.home_page      import *
import pages.images.images as Images
from pages.keyboard import *


# Sets each variable to its corresponding value in the backend
new_filename = backend.get_filename()
new_cartridge = backend.get_cartridge()
new_bullet = backend.get_bullet()
new_powder = backend.get_powder()
new_charge = backend.get_charge()
new_coal = backend.get_coal()
new_primer = backend.get_primer()
new_brass = backend.get_brass()
new_notes = backend.get_notes()

class SavePage(Page):
     def __init__(self, *args, **kwargs):
          Page.__init__(self, *args, **kwargs)

          # Fonts, which include type, size, and weight
          scale_font = font.Font(family='Bahnschrift', size=26, weight='bold')
          details_font = font.Font(family='Bahnschrift', size=18, weight='bold')

          # Sets the Keyboard Page to the same dimensions as other pages
          self.keyboard      = Keyboard(self)
          self.keyboard      .place(in_ = self, x = 0, y = 0, relwidth = 1, relheight = 1)

          ## Set of functions, which send the desired label and counter to the Keyboard then displays the Keyboard
          def filename_keyboard():
               backend.set_label("Filename")
               backend.set_counter(0)

               self.keyboard.show()

          def cartridge_keyboard():
               backend.set_label("Cartridge")
               backend.set_counter(1)

               self.keyboard.show()

          def bullet_keyboard():
               backend.set_label("Bullet")
               backend.set_counter(2)

               self.keyboard.show()

          def powder_keyboard():
               backend.set_label("Powder")
               backend.set_counter(3)

               self.keyboard.show()

          def charge_keyboard():
               backend.set_label("Charge Weight")
               backend.set_counter(4)

               self.keyboard.show()

          def coal_keyboard():
               backend.set_label("C.O.A.L.")
               backend.set_counter(5)

               self.keyboard.show()

          def primer_keyboard():
               backend.set_label("Primer")
               backend.set_counter(6)

               self.keyboard.show()

          def brass_keyboard():
               backend.set_label("Brass")
               backend.set_counter(7)

               self.keyboard.show()

          def notes_keyboard():
               backend.set_label("Notes")
               backend.set_counter(8)

               self.keyboard.show()

          
          # Sets each variable for every field with its corresponding label
          full_filename_text = "Filename:" + "    " + new_filename
          full_cartridge_text = "Cartridge: " + new_cartridge
          full_bullet_text = "Bullet: " + new_bullet
          full_powder_text = "Powder: " + new_powder
          full_charge_text = "Charge Weight: " + new_charge
          full_coal_text = "C.O.A.L.: " + new_coal
          full_primer_text = "Primer: " + new_primer
          full_brass_text = "Brass: " + new_brass
          full_notes_text = "Notes: " + new_notes

          # Initialize Page
          save_page = tk.Frame(self)
          save_page .place(in_=self, x=0, y=0, relwidth=1, relheight=1)

          # Sets the top menu aside from the rest of the page
          top_bar = tk.Frame(save_page, borderwidth=0, width = 800, background="light gray")
          top_bar.pack(side = 'top', expand = False,  fill = 'x', anchor = 'w', pady = 2)

          # Sets the Save button 
          save_button = tk.Button(top_bar, image = Images.get('save_card'), width = '225', borderwidth=0, command = self.lower)
          save_button.pack(side="left", expand=False, fill = "both", anchor = 'w')

          # Sets the Filename Button allowing the user to edit the latter half of the text
          filename_button = tk.Button(top_bar, text = full_filename_text, width = 800-225, anchor = 'w', font = scale_font, command = filename_keyboard, borderwidth=0, background = "light gray")
          filename_button.pack(side="left", expand=False, fill = "both", anchor = 'w')


          # Sets the rest of the page within its own container
          info_section = tk.Frame(save_page)
          info_section.pack(side = 'top', expand = False, pady = 2)

          # Splits the rest of the page into left side and right 
          left_side = tk.Canvas(info_section, width = 250,)
          left_side.grid(row = 0, column = 0, sticky = 'w', ipadx = "25")

          right_side = tk.Canvas(info_section, width = 350)
          right_side.grid(row = 0, column = 1, sticky = 'w')

          ## Each category has its own frame and button to ensure they can be editted indiviually and not have any conflicts with the others
          cartridge_frame = tk.Frame(left_side)
          cartridge_frame.pack(side = 'top', expand = False, pady = 3, fill = 'x', anchor = 'w')

          cartridge_label = tk.Button(cartridge_frame, text = full_cartridge_text, command = cartridge_keyboard, bg = 'light gray', font = details_font, borderwidth=0, width = '30',  anchor = 'w', pady = 4)
          cartridge_label.pack(side = 'left', expand = False)

          bullet_frame = tk.Frame(left_side)
          bullet_frame.pack(side = 'top', expand = False, pady = 3, fill = 'x', anchor = 'w')

          bullet_label = tk.Button(bullet_frame, text = full_bullet_text, command = bullet_keyboard, bg = 'light gray', font = details_font, borderwidth=0, width = '30',  anchor = 'w', pady = 4)
          bullet_label.pack(side = 'left', expand = False)

          powder_frame = tk.Frame(left_side)
          powder_frame.pack(side = 'top', expand = False, pady = 3, fill = 'x', anchor = 'w')

          powder_label = tk.Button(powder_frame, text = full_powder_text, command = powder_keyboard, bg = 'light gray', font = details_font, borderwidth=0, width = '30',  anchor = 'w', pady = 4)
          powder_label.pack(side = 'left', expand = False)

          charge_frame = tk.Frame(left_side)
          charge_frame.pack(side = 'top', expand = False, pady = 3, fill = 'x', anchor = 'w')

          charge_label = tk.Button(charge_frame, text = full_charge_text, command = charge_keyboard, bg = 'light gray', font = details_font, borderwidth=0, width = '30',  anchor = 'w', pady = 4)
          charge_label.pack(side = 'left', expand = False)

          coal_frame = tk.Frame(left_side)
          coal_frame.pack(side = 'top', expand = False, pady = 3, fill = 'x', anchor = 'w')

          coal_label = tk.Button(coal_frame, text = full_coal_text, command = coal_keyboard, bg = 'light gray', font = details_font, borderwidth=0, width = '30',  anchor = 'w', pady = 4)
          coal_label.pack(side = 'left', expand = False)

          primer_frame = tk.Frame(right_side)
          primer_frame.pack(side = 'top', expand = False, pady = 3, fill = 'x', anchor = 'e')

          primer_label = tk.Button(primer_frame, text = full_primer_text, command = primer_keyboard, bg = 'light gray', font = details_font, borderwidth=0, width = '25',  anchor = 'w', pady = 4)
          primer_label.pack(side = 'right', expand = False)

          brass_frame = tk.Frame(right_side)
          brass_frame.pack(side = 'top', expand = False, pady = 3, fill = 'x', anchor = 'e')

          brass_label = tk.Button(brass_frame, text = full_brass_text, command = brass_keyboard, bg = 'light gray', font = details_font, borderwidth=0, width = '25',  anchor = 'w', pady = 4)
          brass_label.pack(side = 'right', expand = False)

          notes_frame = tk.Frame(right_side)
          notes_frame.pack(side = 'top', expand = False, pady = 20, fill = 'x', anchor = 'e')

          notes_label = tk.Button(notes_frame, text = full_notes_text, command = notes_keyboard, bg = 'light gray', font = details_font, borderwidth=0, width = '25', height = "4", pady = 2, anchor = "nw")
          notes_label.pack(side = 'right', expand = False)

          # Defines the update_units function, which allows the user to see the changes they have made
          def update_units():
               filename_updated = backend.get_filename()
               full_filename_text =  "Filename:" + "   " + filename_updated
               filename_button.config(text = full_filename_text)

               cartridge_updated = backend.get_cartridge()
               full_cartridge_text =  "Cartridge:" + "   " + cartridge_updated
               cartridge_label.config(text = full_cartridge_text)

               bullet_updated = backend.get_bullet()
               full_bullet_text =  "Bullet:" + "   " + bullet_updated
               bullet_label.config(text = full_bullet_text)

               powder_updated = backend.get_powder()
               full_powder_text =  "Powder:" + "   " + powder_updated
               powder_label.config(text = full_powder_text)

               charge_updated = backend.get_charge()
               full_charge_text =  "Charge Weight:" + "   " + charge_updated
               charge_label.config(text = full_charge_text)

               coal_updated = backend.get_coal()
               full_coal_text =  "C.O.A.L.:" + "   " + coal_updated
               coal_label.config(text = full_coal_text)

               primer_updated = backend.get_primer()
               full_primer_text =  "Primer:" + "   " + primer_updated
               primer_label.config(text = full_primer_text)

               brass_updated = backend.get_brass()
               full_brass_text =  "Brass:" + "   " + brass_updated
               brass_label.config(text = full_brass_text)

               notes_updated = backend.get_notes()
               full_notes_text = "Notes: " + notes_updated
               notes_label.config(text = full_notes_text)

               # Ensures the function loops after the inital call
               save_page.after(10, update_units)

          # Initial Call of the update_units function
          update_units()

          # Ensures the user does not see the Keyboard unless they click on a field to edit
          self.keyboard      .lower()
