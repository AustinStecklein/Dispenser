# main.py

import tkinter as tk
from tkinter import *
import tkinter.font as font
from turtle import home

from page import *
from settings_page import *
from numpad import NumPad
import banner
import power_button




class MainFrame(tk.Frame):
    def __init__(self):
        tk.Frame().__init__()

        container = tk.Frame(self)

        settings_page = SettingsPage(self)

        settings_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)






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
logo = PhotoImage(file = 'Jonathan\logo.png')  

#Call the Main function to start the program
main = MainFrame(root)

#End of App
root.mainloop()