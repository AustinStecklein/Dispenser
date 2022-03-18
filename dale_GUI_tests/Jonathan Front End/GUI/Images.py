from tkinter import *

imagelist = {

  ## Menu Bar
  'power': ['images/bottom_bar/power.png', None],
  'home': ['images/bottom_bar/home.png', None],
  'right': ['images/right_arrow.png', None],
  'left': ['images/left_arrow.png', None],
  'menu_bar': ['images/bottom_bar/Bottom Bar.png', None],

  ## NumPad
  '1': ['images/numpad_buttons/1_button.png', None],
  '2': ['images/numpad_buttons/2_Button.png', None],
  '3': ['images/numpad_buttons/3_Button.png', None],
  '4': ['images/numpad_buttons/4_Button.png', None],
  '5': ['images/numpad_buttons/5_Button.png', None],
  '6': ['images/numpad_buttons/6_Button.png', None],
  '7': ['images/numpad_buttons/7_Button.png', None],
  '8': ['images/numpad_buttons/8_Button.png', None],
  '9': ['images/numpad_buttons/9_Button.png', None],
  '0': ['images/numpad_buttons/0_Button.png', None],
  'dispense': ['images/numpad_buttons/dispense_Button.png', None],


  ## Main Menu

  # Top Bar
  'load': ['images/main_menu_buttons/load_Button.png', None],
  'save': ['images/main_menu_buttons/Save_Button.png', None],
  'view': ['images/main_menu_buttons/viewedit_Button.png', None],
  
  # Middle Bar
  'coarse': ['images/main_menu_buttons/Coarse_Button.png', None],
  'fine': ['images/main_menu_buttons/fine_Button.png', None],
  'bump': ['images/main_menu_buttons/bump_Button.png', None],
  'clear': ['images/main_menu_buttons/Clear_Button.png', None],
  'calibrate': ['images/main_menu_buttons/Calibrate_Button.png', None],
  'settings': ['images/main_menu_buttons/Settings_Button.png', None],

  # Save Card
  'save_card': ['images/keyboard_buttons/Save_Card.png', None],


  ##KEYBOARD IMAGES

  # Keyboard Numbers
  'small_1': ['images/keyboard_buttons/1_Button.png', None],
  'small_2': ['images/keyboard_buttons/2_Button.png', None],
  'small_3': ['images/keyboard_buttons/3_Button.png', None],
  'small_4': ['images/keyboard_buttons/4_Button.png', None],
  'small_5': ['images/keyboard_buttons/5_Button.png', None],
  'small_6': ['images/keyboard_buttons/6_Button.png', None],
  'small_7': ['images/keyboard_buttons/7_Button.png', None],
  'small_8': ['images/keyboard_buttons/8_Button.png', None],
  'small_9': ['images/keyboard_buttons/9_Button.png', None],
  'small_0': ['images/keyboard_buttons/0_Button.png', None],

  # Keyboard Letters
  'A': ['images/keyboard_buttons/A.png', None],
  'B': ['images/keyboard_buttons/B.png', None],
  'C': ['images/keyboard_buttons/C.png', None],
  'D': ['images/keyboard_buttons/D.png', None],
  'E': ['images/keyboard_buttons/E.png', None],
  'F': ['images/keyboard_buttons/F.png', None],
  'G': ['images/keyboard_buttons/G.png', None],
  'H': ['images/keyboard_buttons/H.png', None],
  'I': ['images/keyboard_buttons/I.png', None],
  'J': ['images/keyboard_buttons/J.png', None],
  'K': ['images/keyboard_buttons/K.png', None],
  'L': ['images/keyboard_buttons/L.png', None],
  'M': ['images/keyboard_buttons/M.png', None],
  'N': ['images/keyboard_buttons/N.png', None],
  'O': ['images/keyboard_buttons/O.png', None],
  'P': ['images/keyboard_buttons/P.png', None],
  'Q': ['images/keyboard_buttons/Q.png', None],
  'R': ['images/keyboard_buttons/R.png', None],
  'S': ['images/keyboard_buttons/S.png', None],
  'T': ['images/keyboard_buttons/T.png', None],
  'U': ['images/keyboard_buttons/U.png', None],
  'V': ['images/keyboard_buttons/V.png', None],
  'W': ['images/keyboard_buttons/W.png', None],
  'X': ['images/keyboard_buttons/X.png', None],
  'Y': ['images/keyboard_buttons/Y.png', None],
  'Z': ['images/keyboard_buttons/Z.png', None],


  # Keyboard Buttons: Other
  'BACK': ['images/keyboard_buttons/BACK.png', None],
  'ENTER': ['images/keyboard_buttons/ENTER.png', None],
  'SPACE': ['images/keyboard_buttons/SPACE.png', None],
  'UP_ARROW': ['images/keyboard_buttons/UP_ARROW.png', None],

  # Keyboard Symbols
  '!': ['images/keyboard_buttons/exclamation_point.png', None],
  '@': ['images/keyboard_buttons/at.png', None],
  '#': ['images/keyboard_buttons/hashtag.png', None],
  '$': ['images/keyboard_buttons/dollar_sign.png', None],
  '%': ['images/keyboard_buttons/percent.png', None],
  '&': ['images/keyboard_buttons/and.png', None],
  '*': ['images/keyboard_buttons/asterisk.png', None],
  '(': ['images/keyboard_buttons/left_paren.png', None],
  ')': ['images/keyboard_buttons/right_paren.png', None],
  '?': ['images/keyboard_buttons/question_mark.png', None],
  '+': ['images/keyboard_buttons/plus.png', None],
  '-': ['images/keyboard_buttons/minus.png', None],
  '=': ['images/keyboard_buttons/equals.png', None],
  ',': ['images/keyboard_buttons/comma.png', None],
  ';': ['images/keyboard_buttons/semicolon.png', None],
  ':': ['images/keyboard_buttons/colon.png', None],
  '/': ['images/keyboard_buttons/backslash.png', None],
  'apostrophe': ['images/keyboard_buttons/apostrophe.png', None],
  'quotation': ['images/keyboard_buttons/quotation_marks.png', None],


  ## Settings Pages

  # First Screen
  'bright': ['images/settings_buttons/brightness and sound_Button.png', None],
  'adjust': ['images/settings_buttons/adjust feeds_Button.png', None],
  'restore': ['images/settings_buttons/restore to defaults_Button.png', None],
  'scale': ['images/settings_buttons/scale config_Button.png', None],

  # Brightness Screen
  'selections': ['images/settings_buttons/save selections_Button.png', None],

  # Adjust Feed Screen
  'adjust bump': ['images/settings_buttons/bump for adjust feed screen_Button.png', None],
  'adjust coarse': ['images/settings_buttons/coarse for adjust feed screen_Button.png', None],
  'adjust fine': ['images/settings_buttons/fine for adjust feed screen_Button.png', None],
  'save adjustments': ['images/settings_buttons/save adjustments_Button.png', None],


}

def get(name):
  if name in imagelist:
    if imagelist[name][1] is None:
       imagelist[name][1] = PhotoImage(file=imagelist[name][0])
    return imagelist[name][1]
  return None