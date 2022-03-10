
import tkinter as tk
from tkinter import ttk

key = tk.Tk()

key.title('On Screen Keyboard')

BUTTON_X_PAD = 1
BUTTON_Y_PAD = 1
BUTTON_WIDTH = 4

key.geometry('800x480')  # Window size
key.maxsize(width=800, height=480)
key.minsize(width=800, height=480)

style = ttk.Style()
key.configure(bg='gray99')
style.configure('TButton', background='#c62b24')
style.configure('TButton', foreground='black')

theme = "light"

# entry box
equation = tk.StringVar()
Dis_entry = ttk.Entry(key, state='readonly', textvariable=equation)
Dis_entry.grid(rowspan=1, columnspan=14, ipadx=180, ipady=20)

exp = " "
is_shift = False

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
    display()


def Clear():
    global exp
    exp = " "
    equation.set(exp)

def display():
    if (is_shift):
        # Adding keys line wise
        # First Line Button

        num1 = ttk.Button(key, text='!', width=BUTTON_WIDTH, command=lambda: press('!'))
        num1.grid(row=1, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num2 = ttk.Button(key, text='@', width=BUTTON_WIDTH, command=lambda: press('@'))
        num2.grid(row=1, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num3 = ttk.Button(key, text='#', width=BUTTON_WIDTH, command=lambda: press('#'))
        num3.grid(row=1, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num4 = ttk.Button(key, text='$', width=BUTTON_WIDTH, command=lambda: press('$'))
        num4.grid(row=1, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num5 = ttk.Button(key, text='%', width=BUTTON_WIDTH, command=lambda: press('%'))
        num5.grid(row=1, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num6 = ttk.Button(key, text='^', width=BUTTON_WIDTH, command=lambda: press('^'))
        num6.grid(row=1, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num7 = ttk.Button(key, text='&', width=BUTTON_WIDTH, command=lambda: press('&'))
        num7.grid(row=1, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num8 = ttk.Button(key, text='*', width=BUTTON_WIDTH, command=lambda: press('*'))
        num8.grid(row=1, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num9 = ttk.Button(key, text='(', width=BUTTON_WIDTH, command=lambda: press('('))
        num9.grid(row=1, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num0 = ttk.Button(key, text=')', width=BUTTON_WIDTH, command=lambda: press(')'))
        num0.grid(row=1, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        under = ttk.Button(key, text='_', width=BUTTON_WIDTH, command=lambda: press('_'))
        under.grid(row=1, column=11, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        plus = ttk.Button(key, text='+', width=BUTTON_WIDTH, command=lambda: press('+'))
        plus.grid(row=1, column=12, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        backspace = ttk.Button(
            key, text='<---', width=BUTTON_WIDTH, command=Backspace)
        backspace.grid(row=1, column=13, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        # Second Line Buttons

        Q = ttk.Button(key, text='Q', width=BUTTON_WIDTH, command=lambda: press('Q'))
        Q.grid(row=2, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        W = ttk.Button(key, text='W', width=BUTTON_WIDTH, command=lambda: press('W'))
        W.grid(row=2, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        E = ttk.Button(key, text='E', width=BUTTON_WIDTH, command=lambda: press('E'))
        E.grid(row=2, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        R = ttk.Button(key, text='R', width=BUTTON_WIDTH, command=lambda: press('R'))
        R.grid(row=2, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        T = ttk.Button(key, text='T', width=BUTTON_WIDTH, command=lambda: press('T'))
        T.grid(row=2, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        Y = ttk.Button(key, text='Y', width=BUTTON_WIDTH, command=lambda: press('Y'))
        Y.grid(row=2, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        U = ttk.Button(key, text='U', width=BUTTON_WIDTH, command=lambda: press('U'))
        U.grid(row=2, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        I = ttk.Button(key, text='I', width=BUTTON_WIDTH, command=lambda: press('I'))
        I.grid(row=2, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        O = ttk.Button(key, text='O', width=BUTTON_WIDTH, command=lambda: press('O'))
        O.grid(row=2, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        P = ttk.Button(key, text='P', width=BUTTON_WIDTH, command=lambda: press('P'))
        P.grid(row=2, column=11, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        # Third Line Buttons

        A = ttk.Button(key, text='A', width=BUTTON_WIDTH, command=lambda: press('A'))
        A.grid(row=3, column=0, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        S = ttk.Button(key, text='S', width=BUTTON_WIDTH, command=lambda: press('S'))
        S.grid(row=3, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        D = ttk.Button(key, text='D', width=BUTTON_WIDTH, command=lambda: press('D'))
        D.grid(row=3, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        F = ttk.Button(key, text='F', width=BUTTON_WIDTH, command=lambda: press('F'))
        F.grid(row=3, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        G = ttk.Button(key, text='G', width=BUTTON_WIDTH, command=lambda: press('G'))
        G.grid(row=3, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        H = ttk.Button(key, text='H', width=BUTTON_WIDTH, command=lambda: press('H'))
        H.grid(row=3, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        J = ttk.Button(key, text='J', width=BUTTON_WIDTH, command=lambda: press('J'))
        J.grid(row=3, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        K = ttk.Button(key, text='K', width=BUTTON_WIDTH, command=lambda: press('K'))
        K.grid(row=3, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        L = ttk.Button(key, text='L', width=BUTTON_WIDTH, command=lambda: press('L'))
        L.grid(row=3, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        colon = ttk.Button(key, text=':', width=BUTTON_WIDTH,
                           command=lambda: press(':'))
        colon.grid(row=3, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        quotation = ttk.Button(key, text='"', width=BUTTON_WIDTH,
                               command=lambda: press('"'))
        quotation.grid(row=3, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        # Fourth line Buttons

        shift = ttk.Button(key, text='Shift', width=BUTTON_WIDTH, command=Shift)
        shift.grid(row=4, column=0, columnspan=2, ipadx=BUTTON_X_PAD * 9, ipady=BUTTON_Y_PAD, padx=0)

        Z = ttk.Button(key, text='Z', width=BUTTON_WIDTH, command=lambda: press('Z'))
        Z.grid(row=4, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        X = ttk.Button(key, text='X', width=BUTTON_WIDTH, command=lambda: press('X'))
        X.grid(row=4, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        C = ttk.Button(key, text='C', width=BUTTON_WIDTH, command=lambda: press('C'))
        C.grid(row=4, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        V = ttk.Button(key, text='V', width=BUTTON_WIDTH, command=lambda: press('V'))
        V.grid(row=4, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        B = ttk.Button(key, text='B', width=BUTTON_WIDTH, command=lambda: press('B'))
        B.grid(row=4, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        N = ttk.Button(key, text='N', width=BUTTON_WIDTH, command=lambda: press('N'))
        N.grid(row=4, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        M = ttk.Button(key, text='M', width=BUTTON_WIDTH, command=lambda: press('M'))
        M.grid(row=4, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        question = ttk.Button(key, text='?', width=BUTTON_WIDTH,
                              command=lambda: press('?'))
        question.grid(row=4, column=11, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        clear = ttk.Button(key, text='Clear', width=BUTTON_WIDTH, command=Clear)
        clear.grid(row=4, column=12, columnspan=2, ipadx=BUTTON_X_PAD * 9, ipady=BUTTON_Y_PAD, padx=0)

        # Fifth Line Buttons

        space = ttk.Button(key, text='Space', width=BUTTON_WIDTH,
                           command=lambda: press(' '))
        space.grid(row=5, column=2, columnspan=8, ipadx=BUTTON_X_PAD * 58, ipady=BUTTON_Y_PAD, padx=0)

        key.mainloop()
    else:
        # Adding keys line wise
        # First Line Button
        tick = ttk.Button(key, text='`', width=BUTTON_WIDTH, command=lambda: press('`'))
        tick.grid(row=1, column=0, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num1 = ttk.Button(key, text='1', width=BUTTON_WIDTH, command=lambda: press('1'))
        num1.grid(row=1, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num2 = ttk.Button(key, text='2', width=BUTTON_WIDTH, command=lambda: press('2'))
        num2.grid(row=1, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num3 = ttk.Button(key, text='3', width=BUTTON_WIDTH, command=lambda: press('3'))
        num3.grid(row=1, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num4 = ttk.Button(key, text='4', width=BUTTON_WIDTH, command=lambda: press('4'))
        num4.grid(row=1, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num5 = ttk.Button(key, text='5', width=BUTTON_WIDTH, command=lambda: press('5'))
        num5.grid(row=1, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num6 = ttk.Button(key, text='6', width=BUTTON_WIDTH, command=lambda: press('6'))
        num6.grid(row=1, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num7 = ttk.Button(key, text='7', width=BUTTON_WIDTH, command=lambda: press('7'))
        num7.grid(row=1, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num8 = ttk.Button(key, text='8', width=BUTTON_WIDTH, command=lambda: press('8'))
        num8.grid(row=1, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num9 = ttk.Button(key, text='9', width=BUTTON_WIDTH, command=lambda: press('9'))
        num9.grid(row=1, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        num0 = ttk.Button(key, text='0', width=BUTTON_WIDTH, command=lambda: press('0'))
        num0.grid(row=1, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        minus = ttk.Button(key, text='-', width=BUTTON_WIDTH, command=lambda: press('-'))
        minus.grid(row=1, column=11, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        equal = ttk.Button(key, text='=', width=BUTTON_WIDTH, command=lambda: press('='))
        equal.grid(row=1, column=12, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        backspace = ttk.Button(
            key, text='<---', width=BUTTON_WIDTH, command=Backspace)
        backspace.grid(row=1, column=13, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        # Second Line Buttons

        Q = ttk.Button(key, text='q', width=BUTTON_WIDTH, command=lambda: press('q'))
        Q.grid(row=2, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        W = ttk.Button(key, text='w', width=BUTTON_WIDTH, command=lambda: press('w'))
        W.grid(row=2, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        E = ttk.Button(key, text='e', width=BUTTON_WIDTH, command=lambda: press('e'))
        E.grid(row=2, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        R = ttk.Button(key, text='r', width=BUTTON_WIDTH, command=lambda: press('r'))
        R.grid(row=2, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        T = ttk.Button(key, text='t', width=BUTTON_WIDTH, command=lambda: press('t'))
        T.grid(row=2, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        Y = ttk.Button(key, text='y', width=BUTTON_WIDTH, command=lambda: press('y'))
        Y.grid(row=2, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        U = ttk.Button(key, text='u', width=BUTTON_WIDTH, command=lambda: press('u'))
        U.grid(row=2, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        I = ttk.Button(key, text='i', width=BUTTON_WIDTH, command=lambda: press('i'))
        I.grid(row=2, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        O = ttk.Button(key, text='o', width=BUTTON_WIDTH, command=lambda: press('o'))
        O.grid(row=2, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        P = ttk.Button(key, text='p', width=BUTTON_WIDTH, command=lambda: press('p'))
        P.grid(row=2, column=11, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        # Third Line Buttons

        A = ttk.Button(key, text='a', width=BUTTON_WIDTH, command=lambda: press('a'))
        A.grid(row=3, column=0, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        S = ttk.Button(key, text='s', width=BUTTON_WIDTH, command=lambda: press('s'))
        S.grid(row=3, column=1, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        D = ttk.Button(key, text='d', width=BUTTON_WIDTH, command=lambda: press('d'))
        D.grid(row=3, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        F = ttk.Button(key, text='f', width=BUTTON_WIDTH, command=lambda: press('f'))
        F.grid(row=3, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        G = ttk.Button(key, text='g', width=BUTTON_WIDTH, command=lambda: press('g'))
        G.grid(row=3, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        H = ttk.Button(key, text='h', width=BUTTON_WIDTH, command=lambda: press('h'))
        H.grid(row=3, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        J = ttk.Button(key, text='j', width=BUTTON_WIDTH, command=lambda: press('j'))
        J.grid(row=3, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        K = ttk.Button(key, text='k', width=BUTTON_WIDTH, command=lambda: press('k'))
        K.grid(row=3, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        L = ttk.Button(key, text='l', width=BUTTON_WIDTH, command=lambda: press('l'))
        L.grid(row=3, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        semi_co = ttk.Button(key, text=';', width=BUTTON_WIDTH,
                             command=lambda: press(';'))
        semi_co.grid(row=3, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        quotation = ttk.Button(key, text="'", width=BUTTON_WIDTH,
                               command=lambda: press('"'))
        quotation.grid(row=3, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        back_slash = ttk.Button(key, text='\\', width=BUTTON_WIDTH,
                                command=lambda: press('\\'))
        back_slash.grid(row=3, column=11, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        enter = ttk.Button(key, text='Enter', width=BUTTON_WIDTH,
                           command=lambda: press('\n'))
        enter.grid(row=3, column=12, columnspan=2, ipadx=BUTTON_X_PAD * 9, ipady=BUTTON_Y_PAD, padx=0)

        # Fourth line Buttons

        shift = ttk.Button(key, text='Shift', width=BUTTON_WIDTH, command=Shift)
        shift.grid(row=4, column=0, columnspan=2, ipadx=BUTTON_X_PAD * 9, ipady=BUTTON_Y_PAD, padx=0)

        Z = ttk.Button(key, text='z', width=BUTTON_WIDTH, command=lambda: press('z'))
        Z.grid(row=4, column=2, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        X = ttk.Button(key, text='x', width=BUTTON_WIDTH, command=lambda: press('x'))
        X.grid(row=4, column=3, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        C = ttk.Button(key, text='c', width=BUTTON_WIDTH, command=lambda: press('c'))
        C.grid(row=4, column=4, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        V = ttk.Button(key, text='v', width=BUTTON_WIDTH, command=lambda: press('v'))
        V.grid(row=4, column=5, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        B = ttk.Button(key, text='b', width=BUTTON_WIDTH, command=lambda: press('b'))
        B.grid(row=4, column=6, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        N = ttk.Button(key, text='n', width=BUTTON_WIDTH, command=lambda: press('n'))
        N.grid(row=4, column=7, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        M = ttk.Button(key, text='m', width=BUTTON_WIDTH, command=lambda: press('m'))
        M.grid(row=4, column=8, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        comma = ttk.Button(key, text=',', width=BUTTON_WIDTH, command=lambda: press(','))
        comma.grid(row=4, column=9, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        dot = ttk.Button(key, text='.', width=BUTTON_WIDTH, command=lambda: press('.'))
        dot.grid(row=4, column=10, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        slash = ttk.Button(key, text='/', width=BUTTON_WIDTH, command=lambda: press('/'))
        slash.grid(row=4, column=11, ipadx=BUTTON_X_PAD, ipady=BUTTON_Y_PAD, padx=0)

        clear = ttk.Button(key, text='Clear', width=BUTTON_WIDTH, command=Clear)
        clear.grid(row=4, column=12, columnspan=2, ipadx=BUTTON_X_PAD * 9, ipady=BUTTON_Y_PAD, padx=0)

        # Fifth Line Buttons

        space = ttk.Button(key, text='Space', width=BUTTON_WIDTH,
                           command=lambda: press(' '))
        space.grid(row=5, column=2, columnspan=8, ipadx=BUTTON_X_PAD * 58, ipady=BUTTON_Y_PAD, padx=0)

        key.mainloop()

display()





