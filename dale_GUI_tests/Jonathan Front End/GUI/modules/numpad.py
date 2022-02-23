from tkinter import *
import tkinter as tk
import tkinter.font as font
import Images

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

        number1 = Images.get('1')
        number2 = Images.get('2')
        number3 = Images.get('3')
        number4 = Images.get('4')
        number5 = Images.get('5')
        number6 = Images.get('6')
        number7 = Images.get('7')
        number8 = Images.get('8')
        number9 = Images.get('9')
        number0 = Images.get('0')
        dispense = Images.get('dispense')


        button_list = [ 
                        number1,    number2,    number3,
                        number4,    number5,    number6,
                        number7,    number8,    number9,
                        number0]

        r = 0
        c = 0
        
        for button in button_list:

            self.btn = Button(self, image = button, width = 90, height = 90, borderwidth="0")

            self.btn.grid(row = r, column = c, padx = 2, pady = 2)
            
            c = (c + 1) % 3
            if c == 0:
                r += 1

        dispense_button = Button(self,
                                image = dispense,
                                borderwidth="0",
                                width = 275, 
                                height = 100,
                                )    
        
        dispense_button.grid(columnspan = 2, row = r, column = c, padx = 2, pady = 2)    


          