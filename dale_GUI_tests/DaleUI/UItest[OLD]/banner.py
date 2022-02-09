from tkinter import *

def display(home_screen, image_file):
    image_container = Canvas(home_screen, height=70, width=600, bg="#FFFFFF")
    image_container.create_image(0,0, anchor = NW, image = image_file)
    image_container.place(x= 5, y = 5)