from tkinter import *
import tkinter.font as font
import cv2
#import modules.backend as backend

# Used this guide:
# https://www.pythontutorial.net/tkinter/tkinter-object-oriented-frame/

#def button_press(btn):
    #print(btn)
    #if btn != 'Dispense':
        #backend.add_target_digit(btn)     

class NumPad(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.create_buttons()

    

    def create_buttons(self):

        number1 = PhotoImage("power.png")
        number2 = PhotoImage("home.png")   

        button_list = [ 
                        number2,    number2,    number1,
                        number1,    number1,    number1,
                        number2,    number2,    number1,
                        number1]

        r = 0
        c = 0
        button_font = font.Font(family='Bahnschrift', size=12, weight='bold')
        for button in button_list:
            self.btn =  Button(self, image = button, width = 5, height = 2, background = "black", foreground="white") 

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
                                )    
        
        dispense_button['font'] = button_font
        dispense_button.grid(columnspan = 2, row = r, column = c, padx = 2, pady = 2)        

          