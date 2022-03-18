# load.py

from tkinter import *
import tkinter.font as font

from power_off import Power_off

class Load(Frame):

    def __init__(self, window):
        super().__init__(window)
        self.grid()
        self.Load()


    def Load(self):

        canvas_load = Canvas(height = 480, width = 650, bg = "white")
        canvas_load.grid()

        #power_off_font = font.Font(family = "Bahnschrift", size = 10)
        main_font = font.Font(family = "Bahnschrift", size = 16)


        #top_banner = Canvas(canvas_load, height = 50, width = 700, bg = "white")
        #top_banner.place(x = 0, y = 0)

        #load_card = Label(top_banner, text = "Load Card", font = main_font)
        #load_card.grid(row = 0, column = 0, padx = 150)

        #file_name = Label(top_banner, text = "Filename:", font = main_font, bg = "white")
        #file_name.grid(row = 0, column = 1, sticky = "W")

        file_list = Canvas(canvas_load, height = 430, width = 650, bg = "white")
        file_list.place(x = 0, y = 50)

        cartridge = Label(file_list, text = "Cartridge: ", bg = "#FFFFFF", font = main_font)
        cartridge.grid(row = 1, column = 0, ipady = 10, sticky = "W")

        cartridge_type = Label(file_list, text = "User Input", bg = "#FFFFFF", font = main_font)
        cartridge_type.grid(row = 1, column = 1, ipady = 10, padx = 25, sticky = "W")

        bullet = Label(file_list, text = "Bullet: ", bg = "#FFFFFF", font = main_font)
        bullet.grid(row = 2, column = 0, ipady = 10, sticky = "W")

        bullet_type = Label(file_list, text = "User Input", bg = "#FFFFFF", font = main_font)
        bullet_type.grid(row = 2, column = 1, ipady = 10, padx = 25, sticky = "W")

        powder = Label(file_list, text = "Powder: ", bg = "#FFFFFF", font = main_font)
        powder.grid(row = 3, column = 0, ipady = 10, sticky = "W")

        charge_weight = Label(file_list, text = "Charge Weight: ", bg = "#FFFFFF", font = main_font)
        charge_weight.grid(row = 4, column = 0, ipady = 10, sticky = "W")

        coal = Label(file_list, text = "C.O.A.L.: ", bg = "#FFFFFF", font = main_font)
        coal.grid(row = 5, column = 0, ipady = 10, sticky = "W")

        primer = Label(file_list, text = "Primer: ", bg = "#FFFFFF", font = main_font)
        primer.grid(row = 6, column = 0, ipady = 10, sticky = "W")

        brass = Label(file_list, text = "Brass: ", bg = "#FFFFFF", font = main_font)
        brass.grid(row = 7, column = 0, ipady = 10, sticky = "W")

        

        