import tkinter as tk
from tkinter import *
import os

# Logo Colors are "c62b24" and "231f20"

# Hamburger / 3 Dots Button for the Menu
# Pages: Main Menu, Settings, NumPad
# Number Pad Functions: Delete, Enter, Clear, 

#Start of App
root = tk.Tk()

#Sets Title of App
root.title('Dispenser')

#Sets size of Window
root.minsize(height = 480, width = 800)
root.resizable(height=False, width=False)

#Load Image into Root
logo = PhotoImage(file = 'C:\\Users\\Temp\\Desktop\\Dispenser\\logo.png')


def main():
    def numpad():
        canvas_main.destroy()
        numbutton.destroy()


        canvas_numpad = Canvas(root, height=480, width=800, bg="#ffffff")
        canvas_numpad.create_image(400,0, anchor = N, image = logo)
        canvas_numpad.pack()


        def back():
            canvas_numpad.destroy()
            Mainmenu.destroy()
            main()
        
        
        btn1 = Button(canvas_numpad, text = "1", bg = "#c62b24", padx=15, pady=10)
        btn2 = Button(canvas_numpad, text = "2", bg = "#c62b24", padx=15, pady=10)
        btn3 = Button(canvas_numpad, text = "3", bg = "#c62b24", padx=15, pady=10)
        btn4 = Button(canvas_numpad, text = "4", bg = "#c62b24", padx=15, pady=10)
        btn5 = Button(canvas_numpad, text = "5", bg = "#c62b24", padx=15, pady=10)
        btn6 = Button(canvas_numpad, text = "6", bg = "#c62b24", padx=15, pady=10)
        btn7 = Button(canvas_numpad, text = "7", bg = "#c62b24", padx=15, pady=10)
        btn8 = Button(canvas_numpad, text = "8", bg = "#c62b24", padx=15, pady=10)
        btn9 = Button(canvas_numpad, text = "9", bg = "#c62b24", padx=15, pady=10)
        btn0 = Button(canvas_numpad, text = "0", bg = "#c62b24", padx=15, pady=10)
        
        
        
        btn1.place(y = 200, x = 350, anchor= N)
        btn2.place(y = 200, x = 400, anchor= N)
        btn3.place(y = 200, x = 450, anchor= N)
        btn4.place(y = 250, x = 350, anchor= N)
        btn5.place(y = 250, x = 400, anchor= N)
        btn6.place(y = 250, x = 450, anchor= N)
        btn7.place(y = 300, x = 350, anchor= N)
        btn8.place(y = 300, x = 400, anchor= N)
        btn9.place(y = 300, x = 450, anchor= N)
        btn0.place(y = 350, x = 400, anchor= N)

        

        Mainmenu = Button(root, text = "Main", fg = "white", bg = "#c62b24", command=back)
        Mainmenu.place(x = 400, y = 450, anchor = S)
        

    canvas_main = Canvas(root, height=480, width=800, bg="#ffffff")
    canvas_main.create_image(400,0, anchor = N, image = logo)
    canvas_main.pack()


    numbutton = Button(root, text = "NumPad", fg = "white", bg = "#c62b24", command=numpad)
    numbutton.place(x = 400, y = 450, anchor = S)

#End of App
main()
root.mainloop()