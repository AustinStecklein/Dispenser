from tkinter import *
import tkinter.font as font
import modules.backend as backend
import modules.image_loader as Images

# Used this guide:
# https://www.pythontutorial.net/tkinter/tkinter-object-oriented-frame/

# TODO: merge jonathan's images with button_press()

def button_press(btn):
    print(btn)
    if btn != 'Dispense':
        backend.add_target_digit(btn)

class NumPad(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.create_buttons()

    def create_buttons(self):
        button_list = [ 
                        '7',    '8',    '9',
                        '4',    '5',    '6',
                        '1',    '2',    '3',
                        '0']

        r = 0
        c = 0
        button_font = font.Font(family='Bahnschrift', size=12, weight='bold')
        for button in button_list:
            self.btn =  Button(self, 
                                text = button,
                                bg = '#c62b24',
                                fg = 'white',
                                width = 10, 
                                height = 4,
                                command = lambda txt = button:button_press(txt)) 
            self.btn['font'] = button_font
            self.btn.grid(row = r, column = c, padx = 2, pady = 2)
            
            c = (c + 1) % 3
            if c == 0:
                r += 1

        dispense_button = Button(self,
                                text = "Dispense",
                                bg = '#c62b24',
                                fg = 'white',
                                width = 22, 
                                height = 4,
                                command = lambda txt = button:button_press('Dispense'))    
        
        dispense_button['font'] = button_font
        dispense_button.grid(columnspan = 2, row = r, column = c, padx = 2, pady = 2)           