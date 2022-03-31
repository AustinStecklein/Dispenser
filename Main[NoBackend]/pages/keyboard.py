# keyboard.py

from tkinter import *
import tkinter as tk
import tkinter.font as font
import pages.backend as backend
from pages.page import Page
import pages.images.images as Images

# Default settings for each of the variables listed below
is_shift = False
exp = ""
counter = 0

class Keyboard(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # Calls the create_buttons function 
        self.create_buttons()

    # create_buttons is the entire Keyboard
    def create_buttons(self):


        # Sets spacing for each button
        BUTTON_X_PAD = 2
        BUTTON_Y_PAD = 2

        # Sets the equation to a String variable to ensure 
        equation = tk.StringVar()

        # When a button is pressed
        def press(num):
            global exp
            exp = exp + str(num)
            equation.set(exp)

        # When the Back button is pressed 
        def Backspace():
            global exp
            exp = exp[:-1]
            equation.set(exp)

        # When the UP Arrow button is pressed
        def Shift():
            global exp
            equation.set(exp)

            global is_shift
            is_shift = not is_shift

            # Deletes and recalls the create_buttons function to show the updated keyboard
            keyboard_frame.destroy()
            self.create_buttons()

        # Ensures the string within the text field is up to date according to user input
        def reset():
            global exp
            equation.set(exp)

            # Ensures the function loops after the initial call
            self.after(1, reset)

        # Calls the reset function defined above
        reset()

        

        # Sets the variable for the display of which field the user is editting
        label = backend.get_label() + ":"

        # Keyboard container
        keyboard_frame = tk.Frame(self)
        keyboard_frame.grid(padx = 20, sticky = "s", pady = 30)

        #Font for Text
        scale_font = font.Font(family='Bahnschrift', size=26, weight='bold')


        # Displays the field the user is editting
        item_label = tk.Label(keyboard_frame, text = label, font = scale_font)
        item_label.grid(row = 0, column = 1, columnspan = 4, sticky = 'w')

        # Text Entry Field 
        Dis_entry = tk.Entry(keyboard_frame, state='readonly', textvariable=equation, font = scale_font, border = 2, bg = "black")
        Dis_entry.grid(row = 0, column = 5, columnspan=11, ipadx=30, ipady=15, sticky = 'w')  


        # Updates the units for the label and counter for the enter field
        def update_units():
            
            # Ensures label_updated and counter can be modified
            global label_updated
            global counter

            # sets the label_updated variable to the label variable in the backend
            # then assigns the label value to the label_updated variable
            # afterwhich the item_label's text is reassigned to the now current label value 
            label_updated = backend.get_label()
            label =  label_updated + ":"
            item_label.config(text = label)

            # Sets the counter value to the counter variable in the backend
            counter = backend.get_counter()

            # This ensures the function loops every 10 milliseconds after the inital call
            keyboard_frame.after(10, update_units)

        # Calls the update_units function defined above
        update_units()

        # Enter Function
        def Enter():

            # Ensures the variable, exp, can be editted
            global exp

            # Based on the counter variable, which was set on the Save Page,
            # sets the current exp variable to the desired variable
            if (counter == 0):
                backend.set_filename(exp)
            if (counter == 1):
                backend.set_cartridge(exp)
            if (counter == 2):
                backend.set_bullet(exp)
            if (counter == 3):
                backend.set_powder(exp)
            if (counter == 4):
                backend.set_charge(exp)
            if (counter == 5):
                backend.set_coal(exp)
            if (counter == 6):
                backend.set_primer(exp)
            if (counter == 7):
                backend.set_brass(exp)
            if (counter == 8):
                backend.set_notes(exp)


            # Resets the exp variable and lowers the Keyboard Page to reveal the Save Page
            exp = ""
            self.lower()



        # If the is_shift variable is true, which it is set to false on default
        if (is_shift):
            # Adding keys line wise
            # First Line Button

            ### This is the template for each button in the keyboard:
            # variable = Button(attachment, image, borderwidth: is 0 to ensure no hidden borders and give the image a curved feel, command: associated with the button press)

            num1 = tk.Button(keyboard_frame, image = Images.get('small_1'), borderwidth = 0, command=lambda: press('1'))
            num1.grid(row=1, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num2 = tk.Button(keyboard_frame, image = Images.get('small_2'), borderwidth = 0, command=lambda: press('2'))
            num2.grid(row=1, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num3 = tk.Button(keyboard_frame, image = Images.get('small_3'), borderwidth = 0, command=lambda: press('3'))
            num3.grid(row=1, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num4 = tk.Button(keyboard_frame, image = Images.get('small_4'), borderwidth = 0, command=lambda: press('4'))
            num4.grid(row=1, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num5 = tk.Button(keyboard_frame, image = Images.get('small_5'), borderwidth = 0, command=lambda: press('5'))
            num5.grid(row=1, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num6 = tk.Button(keyboard_frame, image = Images.get('small_6'), borderwidth = 0, command=lambda: press('6'))
            num6.grid(row=1, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num7 = tk.Button(keyboard_frame, image = Images.get('small_7'), borderwidth = 0, command=lambda: press('7'))
            num7.grid(row=1, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num8 = tk.Button(keyboard_frame, image = Images.get('small_8'), borderwidth = 0, command=lambda: press('8'))
            num8.grid(row=1, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num9 = tk.Button(keyboard_frame, image = Images.get('small_9'), borderwidth = 0, command=lambda: press('9'))
            num9.grid(row=1, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num0 = tk.Button(keyboard_frame, image = Images.get('small_0'), borderwidth = 0, command=lambda: press('0'))
            num0.grid(row=1, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Second Line Buttons

            Q = tk.Button(keyboard_frame, image = Images.get('!'), borderwidth=0, command=lambda: press('!'))
            Q.grid(row=2, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            W = tk.Button(keyboard_frame, image = Images.get('@'), borderwidth=0, command=lambda: press('@'))
            W.grid(row=2, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            E = tk.Button(keyboard_frame, image = Images.get('#'), borderwidth=0, command=lambda: press('#'))
            E.grid(row=2, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            R = tk.Button(keyboard_frame, image = Images.get('$'), borderwidth=0, command=lambda: press('$'))
            R.grid(row=2, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            T = tk.Button(keyboard_frame, image = Images.get('%'), borderwidth=0, command=lambda: press('%'))
            T.grid(row=2, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            Y = tk.Button(keyboard_frame, image = Images.get('&'), borderwidth=0, command=lambda: press('&'))
            Y.grid(row=2, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            U = tk.Button(keyboard_frame, image = Images.get('*'), borderwidth=0, command=lambda: press('*'))
            U.grid(row=2, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            I = tk.Button(keyboard_frame, image = Images.get('('), borderwidth=0, command=lambda: press('('))
            I.grid(row=2, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            O = tk.Button(keyboard_frame, image = Images.get(')'), borderwidth=0, command=lambda: press(')'))
            O.grid(row=2, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            P = tk.Button(keyboard_frame, image = Images.get('?'), borderwidth=0, command=lambda: press('?'))
            P.grid(row=2, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Third Line Buttons

            A = tk.Button(keyboard_frame, image = Images.get('+'), borderwidth=0, command=lambda: press('+'))
            A.grid(row=3, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            S = tk.Button(keyboard_frame, image = Images.get('-'), borderwidth=0, command=lambda: press('-'))
            S.grid(row=3, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            D = tk.Button(keyboard_frame, image = Images.get('='), borderwidth=0, command=lambda: press('='))
            D.grid(row=3, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            F = tk.Button(keyboard_frame, image = Images.get(','), borderwidth=0, command=lambda: press(','))
            F.grid(row=3, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            G = tk.Button(keyboard_frame, image = Images.get(';'), borderwidth=0, command=lambda: press(';'))
            G.grid(row=3, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            H = tk.Button(keyboard_frame, image = Images.get(':'), borderwidth=0, command=lambda: press(':'))
            H.grid(row=3, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            J = tk.Button(keyboard_frame, image = Images.get('/'), borderwidth=0, command=lambda: press('/'))
            J.grid(row=3, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            K = tk.Button(keyboard_frame, image = Images.get("apostrophe"), borderwidth=0, command=lambda: press("'"))
            K.grid(row=3, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            L = tk.Button(keyboard_frame, image = Images.get('quotation'), borderwidth=0, command=lambda: press('"'))
            L.grid(row=3, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Fourth line Buttons

            shift = tk.Button(keyboard_frame, image = Images.get('UP_ARROW'), borderwidth=0, command=Shift)
            shift.grid(row=4, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            Z = tk.Label(keyboard_frame)
            Z.grid(row=4, column=2)

            X = tk.Label(keyboard_frame)
            X.grid(row=4, column=3)

            C = tk.Label(keyboard_frame)
            C.grid(row=4, column=4)

            V = tk.Label(keyboard_frame)
            V.grid(row=4, column=5)

            B = tk.Label(keyboard_frame)
            B.grid(row=4, column=6)

            N = tk.Label(keyboard_frame)
            N.grid(row=4, column=7)

            M = tk.Label(keyboard_frame)
            M.grid(row=4, column=8)

            backspace = tk.Button(keyboard_frame, image = Images.get('BACK'), borderwidth=0, command=Backspace)
            backspace.grid(row=4, column=9, columnspan = 2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0, sticky='w')

            # Fifth Line Buttons

            space = tk.Button(keyboard_frame, image = Images.get('SPACE'), borderwidth = 0,
                            command=lambda: press(' '))
            space.grid(row=5, column=1, columnspan=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            enter = tk.Button(keyboard_frame, image = Images.get('ENTER'), borderwidth = 0, command = Enter)
            enter.grid(row=5, column=9, columnspan=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0, sticky='w')


        # If is_shift is False
        else:
            # Adding keyboard_frames line wise
            # First Line Button

            num1 = tk.Button(keyboard_frame, image = Images.get('small_1'), borderwidth = 0, command=lambda: press('1'))
            num1.grid(row=1, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num2 = tk.Button(keyboard_frame, image = Images.get('small_2'), borderwidth = 0, command=lambda: press('2'))
            num2.grid(row=1, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num3 = tk.Button(keyboard_frame, image = Images.get('small_3'), borderwidth = 0, command=lambda: press('3'))
            num3.grid(row=1, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num4 = tk.Button(keyboard_frame, image = Images.get('small_4'), borderwidth = 0, command=lambda: press('4'))
            num4.grid(row=1, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num5 = tk.Button(keyboard_frame, image = Images.get('small_5'), borderwidth = 0, command=lambda: press('5'))
            num5.grid(row=1, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num6 = tk.Button(keyboard_frame, image = Images.get('small_6'), borderwidth = 0, command=lambda: press('6'))
            num6.grid(row=1, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num7 = tk.Button(keyboard_frame, image = Images.get('small_7'), borderwidth = 0, command=lambda: press('7'))
            num7.grid(row=1, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num8 = tk.Button(keyboard_frame, image = Images.get('small_8'), borderwidth = 0, command=lambda: press('8'))
            num8.grid(row=1, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num9 = tk.Button(keyboard_frame, image = Images.get('small_9'), borderwidth = 0, command=lambda: press('9'))
            num9.grid(row=1, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            num0 = tk.Button(keyboard_frame, image = Images.get('small_0'), borderwidth = 0, command=lambda: press('0'))
            num0.grid(row=1, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Second Line Buttons

            Q = tk.Button(keyboard_frame, image = Images.get('Q'), borderwidth = 0, command=lambda: press('Q'))
            Q.grid(row=2, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            W = tk.Button(keyboard_frame, image = Images.get('W'), borderwidth = 0,command=lambda: press('W'))
            W.grid(row=2, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            E = tk.Button(keyboard_frame, image = Images.get('E'), borderwidth = 0,command=lambda: press('E'))
            E.grid(row=2, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            R = tk.Button(keyboard_frame, image = Images.get('R'), borderwidth = 0,command=lambda: press('R'))
            R.grid(row=2, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            T = tk.Button(keyboard_frame, image = Images.get('T'), borderwidth = 0, command=lambda: press('T'))
            T.grid(row=2, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            Y = tk.Button(keyboard_frame, image = Images.get('Y'), borderwidth = 0,command=lambda: press('Y'))
            Y.grid(row=2, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            U = tk.Button(keyboard_frame, image = Images.get('U'),borderwidth = 0, command=lambda: press('U'))
            U.grid(row=2, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            I = tk.Button(keyboard_frame, image = Images.get('I'), borderwidth = 0,command=lambda: press('I'))
            I.grid(row=2, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            O = tk.Button(keyboard_frame, image = Images.get('O'), borderwidth = 0,command=lambda: press('O'))
            O.grid(row=2, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            P = tk.Button(keyboard_frame, image = Images.get('P'),borderwidth = 0,command=lambda: press('P'))
            P.grid(row=2, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Third Line Buttons

            A = tk.Button(keyboard_frame, image = Images.get('A'), borderwidth = 0,command=lambda: press('A'))
            A.grid(row=3, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            S = tk.Button(keyboard_frame, image = Images.get('S'), borderwidth = 0,command=lambda: press('S'))
            S.grid(row=3, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            D = tk.Button(keyboard_frame, image = Images.get('D'),borderwidth = 0,command=lambda: press('D'))
            D.grid(row=3, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            F = tk.Button(keyboard_frame, image = Images.get('F'), borderwidth = 0, command=lambda: press('F'))
            F.grid(row=3, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            G = tk.Button(keyboard_frame, image = Images.get('G'), borderwidth = 0, command=lambda: press('G'))
            G.grid(row=3, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            H = tk.Button(keyboard_frame, image = Images.get('H'), borderwidth = 0, command=lambda: press('H'))
            H.grid(row=3, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            J = tk.Button(keyboard_frame, image = Images.get('J'),borderwidth = 0, command=lambda: press('J'))
            J.grid(row=3, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            K = tk.Button(keyboard_frame, image = Images.get('K'), borderwidth = 0,command=lambda: press('K'))
            K.grid(row=3, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            L = tk.Button(keyboard_frame, image = Images.get('L'),borderwidth = 0, command=lambda: press('L'))
            L.grid(row=3, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            # Fourth line Buttons

            shift = tk.Button(keyboard_frame, image = Images.get('UP_ARROW'), borderwidth = 0, command=Shift)
            shift.grid(row=4, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            Z = tk.Button(keyboard_frame, image = Images.get('Z'),borderwidth = 0, command=lambda: press('Z'))
            Z.grid(row=4, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            X = tk.Button(keyboard_frame, image = Images.get('X'), borderwidth = 0,command=lambda: press('X'))
            X.grid(row=4, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            C = tk.Button(keyboard_frame, image = Images.get('C'), borderwidth = 0,command=lambda: press('C'))
            C.grid(row=4, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            V = tk.Button(keyboard_frame, image = Images.get('V'), borderwidth = 0,command=lambda: press('V'))
            V.grid(row=4, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            B = tk.Button(keyboard_frame, image = Images.get('B'),borderwidth = 0, command=lambda: press('B'))
            B.grid(row=4, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            N = tk.Button(keyboard_frame, image = Images.get('N'), borderwidth = 0,command=lambda: press('N'))
            N.grid(row=4, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            M = tk.Button(keyboard_frame, image = Images.get('M'),borderwidth = 0, command=lambda: press('M'))
            M.grid(row=4, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            backspace = tk.Button(keyboard_frame, image = Images.get('BACK'), borderwidth=0, command=Backspace)
            backspace.grid(row=4, column=9, columnspan = 2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0, sticky='w')

            # Fifth Line Buttons

            space = tk.Button(keyboard_frame, image = Images.get('SPACE'), borderwidth = 0,
                            command=lambda: press(' '))
            space.grid(row=5, column=1, columnspan=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

            enter = tk.Button(keyboard_frame, image = Images.get('ENTER'), borderwidth = 0, command = Enter)
            enter.grid(row=5, column=9, columnspan=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0, sticky='w')


            