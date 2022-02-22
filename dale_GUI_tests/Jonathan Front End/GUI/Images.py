from tkinter import *

imagelist = {
  'load': ['load_button.png', None],
  'save': ['Save_Button.png', None],
}

def get(name):
  if name in imagelist:
    if imagelist[name][1] is None:
       imagelist[name][1] = PhotoImage(file=imagelist[name][0])
    return imagelist[name][1]
  return None