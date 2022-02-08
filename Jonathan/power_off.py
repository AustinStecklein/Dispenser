# off.py

import tkinter.font as font
from tkinter import *

def Power_off():

    power_off_text = font.Font(family = "Bahnschrift", size = 50)

    power_container = Canvas(height=480, width=800, bg = "black")
    power_container.grid()

    power_text = Label(power_container, text = "Power is Off", bg = "#000000", font = power_off_text, fg = "white")
    power_text.place(x = 400, y = 240, anchor = "center")