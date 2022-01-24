
from ctypes import alignment
import tkinter as tk
from tkinter import *
import os
from turtle import left

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
root.maxsize(height = 480, width = 800)
root.resizable(height=False, width=False)

#Load Image into Root
logo = PhotoImage(file = 'logo.png')


def main():
    def numpad():
        canvas_main1.destroy()

        canvas_numpad = Canvas(root, height=480, width=400, bg="#00FFFF")
        canvas_numpad.grid(row=0, column=1, sticky='e')

        def back():
            canvas_numpad.destroy()
            Mainmenu.destroy()
            main()

        Mainmenu = Button(root, text = "Main", fg = "white", bg = "#c62b24", command=back)
        Mainmenu.place(x = 600, y = 450, anchor = S)
        
        
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
        btndel = Button(canvas_numpad, text = "del", bg = "#c62b24", padx=15, pady=10)
        btnclear = Button(canvas_numpad, text = "clear", bg = "#c62b24", padx=15, pady=10)
        
        btn1.grid(row=0, column=0, sticky='w')
        btn2.grid(row=0, column=1, sticky='w')
        btn3.grid(row=0, column=2, sticky='w')
        btn4.grid(row=1, column=0, sticky='w')
        btn5.grid(row=1, column=1, sticky='w')
        btn6.grid(row=1, column=2, sticky='w')
        btn7.grid(row=2, column=0, sticky='w')
        btn8.grid(row=2, column=1, sticky='w')
        btn9.grid(row=2, column=2, sticky='w')
        btndel.grid(row = 3, column = 0, sticky='w')
        btn0.grid(row=3, column=1, sticky='w')
        btnclear.grid(row=3, column=2, sticky='w')

    def settings():
        canvas_main1.destroy()

        canvas_settings = Canvas(root, height = 480, width = 400, bg = "#FF0000")
        canvas_settings.grid(row = 0, column = 1, sticky = 'e')

        canvas_list = Canvas(canvas_settings, height = 400, width = 320, bg = "#000000")
        canvas_list.grid(padx = 40, pady = 40)

        def back():
            canvas_settings.destroy()
            Mainmenu.destroy()
            main()

        Mainmenu = Button(root, text = "Main", fg = "white", bg = "#c62b24", command=back)
        Mainmenu.place(x = 600, y = 450, anchor = S)


    def manual():
        canvas_main1.destroy()

        canvas_manual = Canvas(root, height = 480, width = 400, bg = "#252525")
        canvas_manual.grid(row = 0, column = 1)

        def back():
            canvas_manual.destroy()
            Mainmenu.destroy()
            main()

        Mainmenu = Button(root, text = "Main", fg = "white", bg = "#c62b24", command=back)
        Mainmenu.place(x = 600, y = 450, anchor = S)
    

    canvas_main = Canvas(root, height=480, width=400, bg="#FFFFFF")
    canvas_main.create_image(0,0, anchor = NW, image = logo)

    target_weight = Label(text ="Target Weight", bg = "#FFFFFF", )
    target_weight.place(x = 150, y = 200)

    actual_weight = Label(text ="Actual Weight", bg = "#FFFFFF", )
    actual_weight.place(x = 150, y = 300)

    canvas_main.grid(row=0, column=0, sticky='w')

    canvas_main1 = Canvas(root, height = 480, width = 400, bg = "#FFFFFF")

    auto_button = Button(canvas_main1, text = "Auto", fg = '#000000', bg = "#c62b24", width="20", height="4")
    auto_button.grid(row = 0, column = 0, padx=15, pady=15)

    manual_button = Button(canvas_main1, text = "Manual", fg = '#000000', bg = "#c62b24", width = "20", height="4", command = manual)
    manual_button.grid(row = 0, column = 1, padx=15, pady=15)

    numbutton = Button(canvas_main1, text = "NumPad", fg = "white", bg = "#c62b24", width="20", height="4", command = numpad)
    numbutton.grid(row = 1, column = 0, padx=15, pady=15)

    settings_button = Button(canvas_main1, text = "Settings", fg = '#000000', bg = "#c62b24", width="20", height="4", command = settings)
    settings_button.grid(row = 1, column = 1, padx=15, pady=15)

    canvas_main1.grid(row=0, column=1, sticky = 'e')



#End of App
main()
root.mainloop()