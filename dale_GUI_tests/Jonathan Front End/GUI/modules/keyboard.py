# keyboard.py

from tkinter import *
import tkinter as tk
import tkinter.font as font
import Images

class Keyboard(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.create_buttons()

    

    def create_buttons(self):


        # Numbers
        number1 = Images.get('small_1')
        number2 = Images.get('small_2')
        number3 = Images.get('small_3')
        number4 = Images.get('small_4')
        number5 = Images.get('small_5')
        number6 = Images.get('small_6')
        number7 = Images.get('small_7')
        number8 = Images.get('small_8')
        number9 = Images.get('small_9')
        number0 = Images.get('small_0')

        #Letters
        letter_A = Images.get('A')
        letter_B = Images.get('B')
        letter_C = Images.get('C')
        letter_D = Images.get('D')
        letter_E = Images.get('E')
        letter_F = Images.get('F')
        letter_G = Images.get('G')
        letter_H = Images.get('H')
        letter_I = Images.get('I')
        letter_J = Images.get('J')
        letter_K = Images.get('K')
        letter_L = Images.get('L')
        letter_M = Images.get('M')
        letter_N = Images.get('N')
        letter_O = Images.get('O')
        letter_P = Images.get('P')
        letter_Q = Images.get('Q')
        letter_R = Images.get('R')
        letter_S = Images.get('S')
        letter_T = Images.get('T')
        letter_U = Images.get('U')
        letter_V = Images.get('V')
        letter_W = Images.get('W')
        letter_X = Images.get('X')
        letter_Y = Images.get('Y')
        letter_Z = Images.get('Z')
        
        #Other Buttons
        BACK_BUTTON = Images.get('BACK')
        ENTER_BUTTON = Images.get('ENTER')
        SPACE_BUTTON = Images.get('SPACE')
        UP_ARROW = Images.get('UP_ARROW')

        


        button_list = [ 
                        number1,  number2,  number3,  number4,  number5,  number6,  number7,  number8,  number9,  number0,
                        letter_Q, letter_W, letter_E, letter_R, letter_T, letter_Y, letter_U, letter_I, letter_O, letter_P, 
                        letter_A, letter_S, letter_D, letter_F, letter_G, letter_H, letter_J, letter_K, letter_L, 
                        UP_ARROW, letter_Z, letter_X, letter_C, letter_V, letter_B, letter_N, letter_M, BACK_BUTTON]

        r = 0
        c = 0
        
        for button in button_list:

            self.btn = Button(self, image = button, borderwidth="0")

            if (((r == 2) or (r == 3)) and (c == 8)):

                self.btn.grid(row = r, column = c, padx = 2, pady = 2, columnspan=2, sticky = 'w')

            else:

                self.btn.grid(row = r, column = c, padx = 2, pady = 2 , sticky = 'w')

            if (r == 0) or (r == 1):
            
                c = (c + 1) % 10
                if c == 0:
                    r += 1

            else:
                c = (c + 1) % 9
                if c == 0:
                    r += 1

        dispense_button = Button(self,
                                image = SPACE_BUTTON,
                                borderwidth="0",
                                )    
        
        dispense_button.grid(columnspan = 8, row = r, column = c, padx = 2, pady = 2)

        keyboard_enter = Button(self,
                                image = ENTER_BUTTON,
                                borderwidth="0",
                                )    
        
        keyboard_enter.grid(columnspan = 2, row = r, column = c + 8, padx = 2, pady = 2, sticky = 'w')


          