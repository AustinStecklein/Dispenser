# keyboard.py

from tkinter import *
import tkinter as tk
import tkinter.font as font
import Images

is_shift = False
exp = " "

start = True

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

        # # # # # # # # # # button_list = [ 
        # # # # # # # # # #                 number1,  number2,  number3,  number4,  number5,  number6,  number7,  number8,  number9,  number0,
        # # # # # # # # # #                 letter_Q, letter_W, letter_E, letter_R, letter_T, letter_Y, letter_U, letter_I, letter_O, letter_P, 
        # # # # # # # # # #                 letter_A, letter_S, letter_D, letter_F, letter_G, letter_H, letter_J, letter_K, letter_L, 
        # # # # # # # # # #                 UP_ARROW, letter_Z, letter_X, letter_C, letter_V, letter_B, letter_N, letter_M, BACK_BUTTON]

        # # # # # # # # # # r = 0
        # # # # # # # # # # c = 0
        
        # # # # # # # # # # for button in button_list:

        # # # # # # # # # #     self.btn = Button(self, image = button, borderwidth="0")

        # # # # # # # # # #     if (((r == 2) or (r == 3)) and (c == 8)):

        # # # # # # # # # #         self.btn.grid(row = r, column = c, padx = 2, pady = 2, columnspan=2, sticky = 'w')

        # # # # # # # # # #     else:

        # # # # # # # # # #         self.btn.grid(row = r, column = c, padx = 2, pady = 2 , sticky = 'w')

        # # # # # # # # # #     if (r == 0) or (r == 1):
            
        # # # # # # # # # #         c = (c + 1) % 10
        # # # # # # # # # #         if c == 0:
        # # # # # # # # # #             r += 1

        # # # # # # # # # #     else:
        # # # # # # # # # #         c = (c + 1) % 9
        # # # # # # # # # #         if c == 0:
        # # # # # # # # # #             r += 1

        # # # # # # # # # # dispense_button = Button(self,
        # # # # # # # # # #                         image = SPACE_BUTTON,
        # # # # # # # # # #                         borderwidth="0",
        # # # # # # # # # #                         )    
        
        # # # # # # # # # # dispense_button.grid(columnspan = 8, row = r, column = c, padx = 2, pady = 2)

        # # # # # # # # # # keyboard_enter = Button(self,
        # # # # # # # # # #                         image = ENTER_BUTTON,
        # # # # # # # # # #                         borderwidth="0",
        # # # # # # # # # #                         )    
        
        # # # # # # # # # # keyboard_enter.grid(columnspan = 2, row = r, column = c + 8, padx = 2, pady = 2, sticky = 'w')

        #def display():

        BUTTON_X_PAD = 2
        BUTTON_Y_PAD = 2
        BUTTON_WIDTH = 4

        equation = tk.StringVar()
        Dis_entry = tk.Entry(self, state='readonly', textvariable=equation)
        Dis_entry.grid(rowspan=1, columnspan=14, ipadx=180, ipady=20)        

        def press(num):
            global exp
            exp = exp + str(num)
            equation.set(exp)


        def Backspace():
            global exp
            exp = exp[:-1]
            equation.set(exp)


        def Shift():
            
            global is_shift
            is_shift = not is_shift
            self.create_buttons()

        if (is_shift):
            # Adding keys line wise
            # First Line Button

            num1 = tk.Button(self, text='1', width=BUTTON_WIDTH, command=lambda: press('1'))
            num1.grid(row=1, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num2 = tk.Button(self, text='2', width=BUTTON_WIDTH, command=lambda: press('2'))
            num2.grid(row=1, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num3 = tk.Button(self, text='3', width=BUTTON_WIDTH, command=lambda: press('3'))
            num3.grid(row=1, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num4 = tk.Button(self, text='4', width=BUTTON_WIDTH, command=lambda: press('4'))
            num4.grid(row=1, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num5 = tk.Button(self, text='5', width=BUTTON_WIDTH, command=lambda: press('5'))
            num5.grid(row=1, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num6 = tk.Button(self, text='6', width=BUTTON_WIDTH, command=lambda: press('6'))
            num6.grid(row=1, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num7 = tk.Button(self, text='7', width=BUTTON_WIDTH, command=lambda: press('7'))
            num7.grid(row=1, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num8 = tk.Button(self, text='8', width=BUTTON_WIDTH, command=lambda: press('8'))
            num8.grid(row=1, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num9 = tk.Button(self, text='9', width=BUTTON_WIDTH, command=lambda: press('9'))
            num9.grid(row=1, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num0 = tk.Button(self, text='0', width=BUTTON_WIDTH, command=lambda: press('0'))
            num0.grid(row=1, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Second Line Buttons

            Q = tk.Button(self, text='!', width=BUTTON_WIDTH, command=lambda: press('!'))
            Q.grid(row=2, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            W = tk.Button(self, text='@', width=BUTTON_WIDTH, command=lambda: press('@'))
            W.grid(row=2, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            E = tk.Button(self, text='#', width=BUTTON_WIDTH, command=lambda: press('#'))
            E.grid(row=2, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            R = tk.Button(self, text='$', width=BUTTON_WIDTH, command=lambda: press('$'))
            R.grid(row=2, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            T = tk.Button(self, text='%', width=BUTTON_WIDTH, command=lambda: press('%'))
            T.grid(row=2, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            Y = tk.Button(self, text='&', width=BUTTON_WIDTH, command=lambda: press('&'))
            Y.grid(row=2, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            U = tk.Button(self, text='*', width=BUTTON_WIDTH, command=lambda: press('*'))
            U.grid(row=2, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            I = tk.Button(self, text='(', width=BUTTON_WIDTH, command=lambda: press('('))
            I.grid(row=2, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            O = tk.Button(self, text=')', width=BUTTON_WIDTH, command=lambda: press(')'))
            O.grid(row=2, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            P = tk.Button(self, text='?', width=BUTTON_WIDTH, command=lambda: press('?'))
            P.grid(row=2, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Third Line Buttons

            A = tk.Button(self, text='+', width=BUTTON_WIDTH, command=lambda: press('+'))
            A.grid(row=3, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            S = tk.Button(self, text='-', width=BUTTON_WIDTH, command=lambda: press('-'))
            S.grid(row=3, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            D = tk.Button(self, text='=', width=BUTTON_WIDTH, command=lambda: press('='))
            D.grid(row=3, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            F = tk.Button(self, text=',', width=BUTTON_WIDTH, command=lambda: press(','))
            F.grid(row=3, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            G = tk.Button(self, text=';', width=BUTTON_WIDTH, command=lambda: press(';'))
            G.grid(row=3, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            H = tk.Button(self, text=':', width=BUTTON_WIDTH, command=lambda: press(':'))
            H.grid(row=3, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            J = tk.Button(self, text='/', width=BUTTON_WIDTH, command=lambda: press('/'))
            J.grid(row=3, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            K = tk.Button(self, text="'", width=BUTTON_WIDTH, command=lambda: press("'"))
            K.grid(row=3, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            L = tk.Button(self, text='"', width=BUTTON_WIDTH, command=lambda: press('"'))
            L.grid(row=3, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Fourth line Buttons

            shift = tk.Button(self, text='Shift', width=BUTTON_WIDTH, command=Shift)
            shift.grid(row=4, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            Z = tk.Button(self, text='Z', width=BUTTON_WIDTH, command=lambda: press('Z'))
            Z.grid(row=4, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            X = tk.Button(self, text='X', width=BUTTON_WIDTH, command=lambda: press('X'))
            X.grid(row=4, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            C = tk.Button(self, text='C', width=BUTTON_WIDTH, command=lambda: press('C'))
            C.grid(row=4, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            V = tk.Button(self, text='V', width=BUTTON_WIDTH, command=lambda: press('V'))
            V.grid(row=4, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            B = tk.Button(self, text='B', width=BUTTON_WIDTH, command=lambda: press('B'))
            B.grid(row=4, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            N = tk.Button(self, text='N', width=BUTTON_WIDTH, command=lambda: press('N'))
            N.grid(row=4, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            M = tk.Button(self, text='M', width=BUTTON_WIDTH, command=lambda: press('M'))
            M.grid(row=4, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            backspace = tk.Button(self, text='Back', width=BUTTON_WIDTH, command=Backspace)
            backspace.grid(row=4, column=9, columnspan = 2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Fifth Line Buttons

            space = tk.Button(self, text='Space', width=BUTTON_WIDTH,
                            command=lambda: press(' '))
            space.grid(row=5, column=1, columnspan=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            enter = tk.Button(self, text='Enter', width=BUTTON_WIDTH, command=lambda: press('\n'))
            enter.grid(row=5, column=9, columnspan=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        else:
            # Adding selfs line wise
            # First Line Button

            num1 = tk.Button(self, text='1', width=BUTTON_WIDTH, command=lambda: press('1'))
            num1.grid(row=1, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num2 = tk.Button(self, text='2', width=BUTTON_WIDTH, command=lambda: press('2'))
            num2.grid(row=1, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num3 = tk.Button(self, text='3', width=BUTTON_WIDTH, command=lambda: press('3'))
            num3.grid(row=1, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num4 = tk.Button(self, text='4', width=BUTTON_WIDTH, command=lambda: press('4'))
            num4.grid(row=1, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num5 = tk.Button(self, text='5', width=BUTTON_WIDTH, command=lambda: press('5'))
            num5.grid(row=1, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num6 = tk.Button(self, text='6', width=BUTTON_WIDTH, command=lambda: press('6'))
            num6.grid(row=1, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num7 = tk.Button(self, text='7', width=BUTTON_WIDTH, command=lambda: press('7'))
            num7.grid(row=1, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num8 = tk.Button(self, text='8', width=BUTTON_WIDTH, command=lambda: press('8'))
            num8.grid(row=1, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num9 = tk.Button(self, text='9', width=BUTTON_WIDTH, command=lambda: press('9'))
            num9.grid(row=1, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num0 = tk.Button(self, text='0', width=BUTTON_WIDTH, command=lambda: press('0'))
            num0.grid(row=1, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Second Line Buttons

            Q = tk.Button(self, text='Q', width=BUTTON_WIDTH, command=lambda: press('Q'))
            Q.grid(row=2, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            W = tk.Button(self, text='W', width=BUTTON_WIDTH, command=lambda: press('W'))
            W.grid(row=2, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            E = tk.Button(self, text='E', width=BUTTON_WIDTH, command=lambda: press('E'))
            E.grid(row=2, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            R = tk.Button(self, text='R', width=BUTTON_WIDTH, command=lambda: press('R'))
            R.grid(row=2, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            T = tk.Button(self, text='T', width=BUTTON_WIDTH, command=lambda: press('T'))
            T.grid(row=2, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            Y = tk.Button(self, text='Y', width=BUTTON_WIDTH, command=lambda: press('Y'))
            Y.grid(row=2, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            U = tk.Button(self, text='U', width=BUTTON_WIDTH, command=lambda: press('U'))
            U.grid(row=2, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            I = tk.Button(self, text='I', width=BUTTON_WIDTH, command=lambda: press('I'))
            I.grid(row=2, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            O = tk.Button(self, text='O', width=BUTTON_WIDTH, command=lambda: press('O'))
            O.grid(row=2, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            P = tk.Button(self, text='P', width=BUTTON_WIDTH, command=lambda: press('P'))
            P.grid(row=2, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Third Line Buttons

            A = tk.Button(self, text='A', width=BUTTON_WIDTH, command=lambda: press('A'))
            A.grid(row=3, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            S = tk.Button(self, text='S', width=BUTTON_WIDTH, command=lambda: press('S'))
            S.grid(row=3, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            D = tk.Button(self, text='D', width=BUTTON_WIDTH, command=lambda: press('D'))
            D.grid(row=3, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            F = tk.Button(self, text='F', width=BUTTON_WIDTH, command=lambda: press('F'))
            F.grid(row=3, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            G = tk.Button(self, text='G', width=BUTTON_WIDTH, command=lambda: press('G'))
            G.grid(row=3, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            H = tk.Button(self, text='H', width=BUTTON_WIDTH, command=lambda: press('H'))
            H.grid(row=3, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            J = tk.Button(self, text='J', width=BUTTON_WIDTH, command=lambda: press('J'))
            J.grid(row=3, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            K = tk.Button(self, text='K', width=BUTTON_WIDTH, command=lambda: press('K'))
            K.grid(row=3, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            L = tk.Button(self, text='L', width=BUTTON_WIDTH, command=lambda: press('L'))
            L.grid(row=3, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Fourth line Buttons

            shift = tk.Button(self, text='Shift', width=BUTTON_WIDTH, command=Shift)
            shift.grid(row=4, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            Z = tk.Button(self, text='Z', width=BUTTON_WIDTH, command=lambda: press('Z'))
            Z.grid(row=4, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            X = tk.Button(self, text='X', width=BUTTON_WIDTH, command=lambda: press('X'))
            X.grid(row=4, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            C = tk.Button(self, text='C', width=BUTTON_WIDTH, command=lambda: press('C'))
            C.grid(row=4, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            V = tk.Button(self, text='V', width=BUTTON_WIDTH, command=lambda: press('V'))
            V.grid(row=4, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            B = tk.Button(self, text='B', width=BUTTON_WIDTH, command=lambda: press('B'))
            B.grid(row=4, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            N = tk.Button(self, text='N', width=BUTTON_WIDTH, command=lambda: press('N'))
            N.grid(row=4, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            M = tk.Button(self, text='M', width=BUTTON_WIDTH, command=lambda: press('M'))
            M.grid(row=4, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            backspace = tk.Button(self, text='<---', width=BUTTON_WIDTH, command=Backspace)
            backspace.grid(row=4, column=9, columnspan = 2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Fifth Line Buttons

            space = tk.Button(self, text='Space', width=BUTTON_WIDTH,
                            command=lambda: press(' '))
            space.grid(row=5, column=1, columnspan=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            enter = tk.Button(self, text='Enter', width=BUTTON_WIDTH, command=lambda: press('\n'))
            enter.grid(row=5, column=9, columnspan=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

    #display()


            