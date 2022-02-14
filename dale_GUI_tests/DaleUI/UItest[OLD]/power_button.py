from tkinter import *
import tkinter.font as font

def display(home_screen):
    main_font = font.Font(family = "Bahnschrift", size = 12)

    button_container = Canvas(home_screen, height=50, width=50, bg="#FFFFFF")
    button_container.place(x = 795, y = 5,anchor = 'ne')

    power_button = Button(button_container, text = "Power", fg = '#FFFFFF', bg = "#c62b24", width = '10', height = '2', font = main_font, command = power_off)
    power_button.place(x = 0, y = 0, anchor = 'ne')

def power_off():
    pass