from tkinter import *

imagelist = {

  ## Menu Bar
  'power': ['power.png', None],
  'home': ['home.png', None],
  'right': ['right_arrow.png', None],
  'left': ['left_arrow.png', None],
  'menu_bar': ['Bottom Bar.png', None],

  ## NumPad
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


  ## Main Menu

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


  ##KEYBOARD IMAGES

  # Keyboard Numbers
  'small_1': ['keyboard_numbers/1_Button.png', None],
  'small_2': ['keyboard_numbers/2_Button.png', None],
  'small_3': ['keyboard_numbers/3_Button.png', None],
  'small_4': ['keyboard_numbers/4_Button.png', None],
  'small_5': ['keyboard_numbers/5_Button.png', None],
  'small_6': ['keyboard_numbers/6_Button.png', None],
  'small_7': ['keyboard_numbers/7_Button.png', None],
  'small_8': ['keyboard_numbers/8_Button.png', None],
  'small_9': ['keyboard_numbers/9_Button.png', None],
  'small_0': ['keyboard_numbers/0_Button.png', None],

  # Keyboard Letters
  'A': ['images/A.png', None],
  'B': ['images/B.png', None],
  'C': ['images/C.png', None],
  'D': ['images/D.png', None],
  'E': ['images/E.png', None],
  'F': ['images/F.png', None],
  'G': ['images/G.png', None],
  'H': ['images/H.png', None],
  'I': ['images/I.png', None],
  'J': ['images/J.png', None],
  'K': ['images/K.png', None],
  'L': ['images/L.png', None],
  'M': ['images/M.png', None],
  'N': ['images/N.png', None],
  'O': ['images/O.png', None],
  'P': ['images/P.png', None],
  'Q': ['images/Q.png', None],
  'R': ['images/R.png', None],
  'S': ['images/S.png', None],
  'T': ['images/T.png', None],
  'U': ['images/U.png', None],
  'V': ['images/V.png', None],
  'W': ['images/W.png', None],
  'X': ['images/X.png', None],
  'Y': ['images/Y.png', None],
  'Z': ['images/Z.png', None],


  # Keyboard Buttons: Other
  'BACK': ['images/BACK.png', None],
  'ENTER': ['images/ENTER.png', None],
  'SPACE': ['images/SPACE.png', None],
  'UP_ARROW': ['images/UP_ARROW.png', None],

  # Keyboard Symbols
  '!': ['images/exclamation_point.png', None],
  '@': ['images/at.png', None],
  '#': ['images/hashtag.png', None],
  '$': ['images/dollar_sign.png', None],
  '%': ['images/percent.png', None],
  '&': ['images/and.png', None],
  '*': ['images/asterisk.png', None],
  '(': ['images/left_paren.png', None],
  ')': ['images/right_paren.png', None],
  '?': ['images/question_mark.png', None],
  '+': ['images/plus.png', None],
  '-': ['images/minus.png', None],
  '=': ['images/equals.png', None],
  ',': ['images/comma.png', None],
  ';': ['images/semicolon.png', None],
  ':': ['images/colon.png', None],
  '/': ['images/backslash.png', None],
  'apostrophe': ['images/apostrophe.png', None],
  'quotation': ['images/quotation_marks.png', None],


  ## Settings Pages

  # First Screen
  'bright': ['brightness and sound_Button.png', None],
  'adjust': ['adjust feeds_Button.png', None],
  'restore': ['restore to defaults_Button.png', None],
  'scale': ['scale config_Button.png', None],

  # Brightness Screen
  'selections': ['save selections_Button.png', None],

  # Adjust Feed Screen
  'adjust bump': ['bump for adjust feed screen_Button.png', None],
  'adjust coarse': ['coarse for adjust feed screen_Button.png', None],
  'adjust fine': ['fine for adjust feed screen_Button.png', None],
  'save adjustments': ['save adjustments_Button.png', None],


}

def get(name):
  if name in imagelist:
    if imagelist[name][1] is None:
       imagelist[name][1] = PhotoImage(file=imagelist[name][0])
    return imagelist[name][1]
  return None