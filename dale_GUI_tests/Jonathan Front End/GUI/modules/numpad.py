from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
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

        number1 = Images.get('load')


        number2 = Images.get('save')

        button_list = [ 
                        number1,    number1,    number1,
                        number1,    number1,    number1,
                        number2,    number2,    number2,
                        number2]

        r = 0
        c = 0
        
        for button in button_list:

            


            self.btn = Button(self, image = button, width = 80, height = 80, background = "black",)

            self.btn.grid(row = r, column = c, padx = 2, pady = 2)

            #test_button = Button(self, image = number2, width = 80, height = 80, background = "black",)
            #test_button.grid(row = r, column = c)
            
            c = (c + 1) % 3
            if c == 0:
                r += 1



        button_font = font.Font(family='Bahnschrift', size=12, weight='bold')

        dispense_button = Button(self,
                                text = "Dispense",
                                bg = '#c62b24',
                                fg = 'white',
                                width = 22, 
                                height = 4,
                                )    
        
        dispense_button['font'] = button_font
        dispense_button.grid(columnspan = 2, row = r, column = c, padx = 2, pady = 2)    

    if __name__ == "__numpad__":

        home =        PhotoImage(file = 'home.png')
        power =       PhotoImage(file = 'power.png')       


          