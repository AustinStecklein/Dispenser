from tkinter import *

sent_text = ""
def click():
    global sent_text
    sent_text = text_entry.get()

window = Tk()
window.title("Dale's GUI test")
window.geometry("800x480")
window.configure(background="black")

image1 = PhotoImage(file="dale_GUI_tests\creedmoor_logo.png")
Label (window, image=image1, bg="black") .grid(row=0, column=0, sticky=W)

Label(window, text="This is a test message", bg="black", fg="red", font="none 14")  .grid(row=0, column=1, sticky=E)

text_entry = Entry(window, width=30, bg="white", fg="black")
text_entry.grid(row=1, column=0)

Button(window, text="Send", width=7, command=click) .grid(row=1, column=1, sticky=W)

Label(window, text=sent_text, bg="black", fg="red", font="none 14")  .grid(row=0, column=1, sticky=E)



window.mainloop()