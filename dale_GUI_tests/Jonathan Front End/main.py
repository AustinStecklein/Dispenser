# main.py

from calendar import c
import tkinter as tk
from tkinter import *
import tkinter.font as font
from numpad import NumPad
from power_off import Power_off
from load import Load
import datetime


#Start of App
root = tk.Tk()

#Sets Title of App
root.title('Dispenser')

#Set App Dimensions
root.geometry('800x480')
root.resizable(height=False, width=False)

#Main Font for UI
main_font = font.Font(family = "Bahnschrift", size = 12)
power_off_text = font.Font(family = "Bahnschrift", size = 50)

#logo for UI
banner = PhotoImage(file = 'dale_GUI_tests\Jonathan Front End\\banner.png')
logo = PhotoImage(file = 'dale_GUI_tests\Jonathan Front End\\logo.png')
mini = PhotoImage(file = 'dale_GUI_tests\Jonathan Front End\mini.png')
other = PhotoImage(file = 'dale_GUI_tests\Jonathan Front End\other.png')

def main():
    app_container = Canvas(height = 480, width = 800, bg = "white")
    app_container.grid()

    image_container = Canvas(app_container, height=75, width=500, bg="#FFFFFF")
    image_container.create_image(0,0, anchor = NW, image = banner)
    image_container.place(x= 5, y = 5)

    def test_function():
        test_button.config(relief = RAISED, state = tk.ACTIVE)
        other_button.config(relief=RAISED, state = tk.ACTIVE)

    auto_button = Button(app_container, image = logo,  width = "80", height = "80", borderwidth = 0, command = test_function, background="white")
    auto_button.place(x = 250, y = 240, anchor = "center")

    def test_function1():
        test_button.config(relief = SUNKEN, state = tk.DISABLED)


    test_button = Button(app_container, image = mini, width = 80, height = 80, borderwidth=0, command = test_function1)
    test_button.place(x = 400, y = 240, anchor = "center")

    def test_function2():
        other_button.config(relief = SUNKEN, state = tk.DISABLED)


    other_button = Button(app_container, image = other, width = 80, height = 80, borderwidth=0, command = test_function2)
    other_button.place(x = 550, y = 240, anchor = "center")


    def power_off():
        app_container.destroy()

        Power_off()

    def numpad_menu():
        app_container.destroy()

        #Holds all the Things
        numpad_container = Canvas(height = 480, width = 800, bg = "white")
        numpad_container.grid()

        def power_off():
            numpad_container.destroy()

            Power_off()

        def Return():
            numpad_container.destroy()
            main()

        def load_menu():
            numpad_container.destroy()

            load_container = Canvas(height = 480, width = 800)
            load_container.grid()


            def ReturnNumpad():
                load_container.destroy()
                numpad_menu()

            return_button = Button(text = "Return", bg = "#c62b24", width = '10', height = '2', font = main_font, command = ReturnNumpad)
            return_button.place(x = 795, y = 475, anchor = 'se')

            def power_off():
                load_container.destroy()
                Power_off()

            power_button = Button(text = "Power", fg = '#FFFFFF', bg = "#c62b24", width = '10', height = '2', font = main_font, command = power_off)
            power_button.place(x = 795, y = 5, anchor = 'ne')

        def settings_menu():
            numpad_container.destroy()

            settings_container = Canvas(height = 480, width = 800)
            settings_container.grid()

            def Return():
                settings_container.destroy()
                numpad_menu()

            return_button = Button(text = "Return", bg = "#c62b24", width = '10', height = '2', font = main_font, command = Return)
            return_button.place(x = 795, y = 475, anchor = 'se')

            def power_off():
                settings_container.destroy()
                Power_off()

            power_button = Button(text = "Power", fg = 'white', bg = "#c62b24", width = '10', height = '2', font = main_font, command = power_off)
            power_button.place(x = 795, y = 5, anchor = 'ne')   

        #THE BUTTONS
        power_button = Button(numpad_container, text = "Power", fg = '#FFFFFF', bg = "#c62b24", width = '10', height = '2', font = main_font, command = power_off)
        power_button.place(x = 795, y = 5, anchor = 'ne')

        return_button = Button(text = "Return", bg = "#c62b24", width = '10', height = '2', font = main_font, command = Return)
        return_button.place(x = 795, y = 475, anchor = 'se')

        load_button = Button(numpad_container, text = "Load", fg = "white", bg = "#c62b24", width="10", height="2", command = load_menu)
        load_button.place(x = 5, y = 50, anchor = 'w')

        save_button = Button(numpad_container, text = "Save", fg = "white", bg = "#c62b24", width="10", height="2", command = load_menu)
        save_button.place(x = 5, y = 150, anchor = 'w')

        view_button = Button(numpad_container, text = "View", fg = "white", bg = "#c62b24", width="10", height="2", command = load_menu)
    

        settings_container = Canvas(height = 480, width = 800)
        settings_container.grid()

        def Return():
            settings_container.destroy()
            main()

        return_button = Button(text = "Return", bg = "#c62b24", width = '10', height = '2', font = main_font, command = Return)
        return_button.place(x = 795, y = 475, anchor = 'se')

        def power_off():
            settings_container.destroy()
            Power_off()

        power_button = Button(text = "Power", fg = 'white', bg = "#c62b24", width = '10', height = '2', font = main_font, command = power_off)
        power_button.place(x = 795, y = 5, anchor = 'ne')




    #settings_button = Button(app_container, text = "Settings", fg = "white", bg = "#c62b24", width="20", height="4", command = settings_menu)
    #settings_button.place(x = 600, y = 240, anchor = 'center')


#Call the Main function to start the program
main()

#End of App
root.mainloop()