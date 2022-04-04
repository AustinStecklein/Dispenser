from tkinter import *
import tkinter as tk
import tkinter.font as font
import pages.images.images as Images
import pages.backend as backend

# Sets Variables used in Numpad Buttons
exp = ""
BUTTON_X_PAD = 2
BUTTON_Y_PAD = 2

class NumPad(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.create_buttons()

    
    def create_buttons(self):

        # Sends the Number pressed to the exp variable
        def press(btn):
            print(btn)
            if btn != 'Dispense':
                backend.add_target_digit(btn)

        # Numbers 0 - 9 Buttons and Dispense Button
        num1 = tk.Button(self, image = Images.get('1'), borderwidth = 0, command=lambda: press('1'))
        num1.grid(row=0, column=0, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num2 = tk.Button(self, image = Images.get('2'), borderwidth = 0, command=lambda: press('2'))
        num2.grid(row=0, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num3 = tk.Button(self, image = Images.get('3'), borderwidth = 0, command=lambda: press('3'))
        num3.grid(row=0, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num4 = tk.Button(self, image = Images.get('4'), borderwidth = 0, command=lambda: press('4'))
        num4.grid(row=1, column=0, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num5 = tk.Button(self, image = Images.get('5'), borderwidth = 0, command=lambda: press('5'))
        num5.grid(row=1, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num6 = tk.Button(self, image = Images.get('6'), borderwidth = 0, command=lambda: press('6'))
        num6.grid(row=1, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num7 = tk.Button(self, image = Images.get('7'), borderwidth = 0, command=lambda: press('7'))
        num7.grid(row=2, column=0, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num8 = tk.Button(self, image = Images.get('8'), borderwidth = 0, command=lambda: press('8'))
        num8.grid(row=2, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num9 = tk.Button(self, image = Images.get('9'), borderwidth = 0, command=lambda: press('9'))
        num9.grid(row=2, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num0 = tk.Button(self, image = Images.get('0'), borderwidth = 0, command=lambda: press('0'))
        num0.grid(row=3, column=0, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        dispense_button = Button(self,image = Images.get('dispense'), borderwidth="0", command = backend.auto_dispense)    
        dispense_button.grid(columnspan = 2, row = 3, column = 1, padx = 2, pady = 2)  
