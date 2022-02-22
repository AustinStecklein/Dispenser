from tkinter import *

imagelist = {
  'food_0001': ['power.png', None],
  'food_0002': ['power.png', None],
}

def get(name):
  if name in imagelist:
    if imagelist[name][1] is None:
      print('loading image:', name)
      imagelist[name][1] = PhotoImage(file=imagelist[name][0])
    return imagelist[name][1]
  return None