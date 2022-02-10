# numpad.py

from tkinter import *
import tkinter.font as font

import backend

# Used this guide:
# https://www.pythontutorial.net/tkinter/tkinter-object-oriented-frame/

def button_press(btn):
    print(btn)
    backend.add_target_digit(btn)

class NumPad(Frame):
    def __init__(self, window):
        super().__init__(window)
        # self.grid()
        self.create_buttons()

    def create_buttons(self):
        button_list = [ 
                        '7',    '8',    '9',
                        '4',    '5',    '6',
                        '1',    '2',    '3',
                        'Back', '0',    'Enter']

        r = 0
        c = 0
        button_font = font.Font(family='Bahnschrift', size=12, weight='bold')
        for button in button_list:
            self.btn =  Button(self, 
                                text=button,
                                bg='#c62b24',
                                fg='white',
                                width=10, 
                                height=2, 
                                command=lambda txt=button:button_press(txt)) 
            self.btn['font'] = button_font
            self.btn.grid(row=r, column=c)
            
            c = (c + 1) % 3
            if c == 0:
                r += 1