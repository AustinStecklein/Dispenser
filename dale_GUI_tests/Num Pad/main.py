from num_pad import NumPad

from tkinter import *

window = Tk()
window.title("Dale's GUI test")
window.geometry("800x480")
window.configure(background="black")


num_pad = NumPad(window, 0, 0) # column 0, row 0


window.mainloop()