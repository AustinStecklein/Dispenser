from tkinter import *
from tkinter import ttk
import threading
from event import Event

class GUI(threading.Thread):
    def __init__(self, handler):
        threading.Thread.__init__(self)
        self.start()
        self.handler = handler
    
    #Call back for when user closes window to handle stopping the thread
    def callback(self):
        self.root.quit()
        self.handler.regEvent(Event.FULL_STOP)
    
    def killAll(self):
        self.handler.regEvent(Event.FULL_STOP)
        self.root.quit()

    #Create window
    def run(self):
        #Setup  the root structure of the frame
        self.root = Tk()
        self.root.title = "Dispenser"
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        #Add structure to the frame
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        #Add buttons with events``
        ttk.Button(frm, text="Slow", command=lambda: self.handler.regEvent(Event.MANUAL_SLOW)).grid(column=0, row=0)
        ttk.Button(frm, text="Medium", command=lambda: self.handler.regEvent(Event.MANUAL_MED)).grid(column=0, row=1)
        ttk.Button(frm, text="Fast", command=lambda: self.handler.regEvent(Event.MANUAL_FAST)).grid(column=0, row=2)
        ttk.Button(frm, text="Quit", command=lambda: self.killAll() ).grid(column=0, row=3)
        
        #Start main thread
        self.root.mainloop()