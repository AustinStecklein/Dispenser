from tkinter import *

imagelist = {
  # Menu Bar
  'power': ['power.png', None],
  'home': ['home.png', None],
  'right': ['right_arrow.png', None],
  'left': ['left_arrow.png', None],

  # NumPad
  '1': ['1_button.png', None],
  '2': ['2_Button.png', None],
  '3': ['3_Button.png', None],
  '4': ['4_Button.png', None],
  '5': ['5_Button.png', None],
  '6': ['6_Button.png', None],
  '7': ['7_Button.png', None],
  '8': ['8_Button.png', None],
  '9': ['9_Button.png', None],
  '0': ['0_Button.png', None],
  'dispense': ['dispense_Button.png', None],

  # Top Bar
  'load': ['load_Button.png', None],
  'save': ['Save_Button.png', None],
  'view': ['viewedit_Button.png', None],
  

  # Middle Bar
  'coarse': ['Coarse_Button.png', None],
  'fine': ['fine_Button.png', None],
  'bump': ['bump_Button.png', None],
  'clear': ['Clear_Button.png', None],
  'calibrate': ['Calibrate_Button.png', None],
  'settings': ['Settings_Button.png', None],

  # Save Card
  'save_card': ['Save_Card.png', None],
  'keyboard': ['keyboard.png', None],

}

def get(name):
  if name in imagelist:
    if imagelist[name][1] is None:
       imagelist[name][1] = PhotoImage(file=imagelist[name][0])
    return imagelist[name][1]
  return None