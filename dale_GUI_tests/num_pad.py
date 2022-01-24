from tkinter import *
import tkinter.font as font

# Used this guide:
# https://www.pythontutorial.net/tkinter/tkinter-object-oriented-frame/

def button_press(btn):
    print(btn)

class NumPad(Frame):
    def __init__(self, window, c_root, r_root):
        super().__init__(window)
        self.c_root = c_root
        self.r_root = r_root
        self.grid()
        
        self.create_buttons()

    def create_buttons(self):
        button_list = [ '-1',   '+0.1', '+1',
                        '7',    '8',    '9',
                        '4',    '5',    '6',
                        '1',    '2',    '3',
                        'Back', '0',    'Enter']

        r_count = 0
        c_count = 0
        button_font = font.Font(family='Arial Unicode MS', size=18, weight='bold')
        for button in button_list:
            self.btn =  Button(self, 
                                text=button,
                                bg='#c62b24',
                                fg='white',
                                width=6, 
                                height=2, 
                                command=lambda txt=button:button_press(txt)) 
            self.btn['font'] = button_font
            self.btn.grid(row=(r_count + self.r_root), column=c_count + self.c_root)
            
            c_count = (c_count + 1) % 3
            if c_count == 0:
                r_count += 1
