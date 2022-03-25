from tkinter import *
import sys

imagelist = {

  ## Menu Bar
  'power': [sys.path[0] +'/pages/images/bottom_bar/power.png', None],
  'home': [sys.path[0] +'/pages/images/bottom_bar/home.png', None],
  'right': [sys.path[0] +'/pages/images/bottom_bar/right_arrow.png', None],
  'left': [sys.path[0] +'/pages/images/bottom_bar/left_arrow.png', None],
  'menu_bar': [sys.path[0] +'/pages/images/bottom_bar/Bottom Bar.png', None],

  ## NumPad
  '1': [sys.path[0] +'/pages/images/numpad_buttons/1_button.png', None],
  '2': [sys.path[0] +'/pages/images/numpad_buttons/2_Button.png', None],
  '3': [sys.path[0] +'/pages/images/numpad_buttons/3_Button.png', None],
  '4': [sys.path[0] +'/pages/images/numpad_buttons/4_Button.png', None],
  '5': [sys.path[0] +'/pages/images/numpad_buttons/5_Button.png', None],
  '6': [sys.path[0] +'/pages/images/numpad_buttons/6_Button.png', None],
  '7': [sys.path[0] +'/pages/images/numpad_buttons/7_Button.png', None],
  '8': [sys.path[0] +'/pages/images/numpad_buttons/8_Button.png', None],
  '9': [sys.path[0] +'/pages/images/numpad_buttons/9_Button.png', None],
  '0': [sys.path[0] +'/pages/images/numpad_buttons/0_Button.png', None],
  'dispense': [sys.path[0] +'/pages/images/numpad_buttons/dispense_Button.png', None],


  ## Main Menu

  # Top Bar
  'load': [sys.path[0] +'/pages/images/main_menu_buttons/load_Button.png', None],
  'save': [sys.path[0] +'/pages/images/main_menu_buttons/Save_Button.png', None],
  'view': [sys.path[0] +'/pages/images/main_menu_buttons/viewedit_Button.png', None],
  
  # Middle Bar
  'coarse': [sys.path[0] +'/pages/images/main_menu_buttons/Coarse_Button.png', None],
  'fine': [sys.path[0] +'/pages/images/main_menu_buttons/fine_Button.png', None],
  'bump': [sys.path[0] +'/pages/images/main_menu_buttons/bump_Button.png', None],
  'clear': [sys.path[0] +'/pages/images/main_menu_buttons/Clear_Button.png', None],
  'calibrate': [sys.path[0] +'/pages/images/main_menu_buttons/Calibrate_Button.png', None],
  'settings': [sys.path[0] +'/pages/images/main_menu_buttons/Settings_Button.png', None],

  # Save Card
  'save_card': [sys.path[0] +'/pages/images/keyboard_buttons/Save_Card.png', None],


  ##KEYBOARD IMAGES

  # Keyboard Numbers
  'small_1': [sys.path[0] +'/pages/images/keyboard_buttons/1_Button.png', None],
  'small_2': [sys.path[0] +'/pages/images/keyboard_buttons/2_Button.png', None],
  'small_3': [sys.path[0] +'/pages/images/keyboard_buttons/3_Button.png', None],
  'small_4': [sys.path[0] +'/pages/images/keyboard_buttons/4_Button.png', None],
  'small_5': [sys.path[0] +'/pages/images/keyboard_buttons/5_Button.png', None],
  'small_6': [sys.path[0] +'/pages/images/keyboard_buttons/6_Button.png', None],
  'small_7': [sys.path[0] +'/pages/images/keyboard_buttons/7_Button.png', None],
  'small_8': [sys.path[0] +'/pages/images/keyboard_buttons/8_Button.png', None],
  'small_9': [sys.path[0] +'/pages/images/keyboard_buttons/9_Button.png', None],
  'small_0': [sys.path[0] +'/pages/images/keyboard_buttons/0_Button.png', None],

  # Keyboard Letters
  'A': [sys.path[0] +'/pages/images/keyboard_buttons/A.png', None],
  'B': [sys.path[0] +'/pages/images/keyboard_buttons/B.png', None],
  'C': [sys.path[0] +'/pages/images/keyboard_buttons/C.png', None],
  'D': [sys.path[0] +'/pages/images/keyboard_buttons/D.png', None],
  'E': [sys.path[0] +'/pages/images/keyboard_buttons/E.png', None],
  'F': [sys.path[0] +'/pages/images/keyboard_buttons/F.png', None],
  'G': [sys.path[0] +'/pages/images/keyboard_buttons/G.png', None],
  'H': [sys.path[0] +'/pages/images/keyboard_buttons/H.png', None],
  'I': [sys.path[0] +'/pages/images/keyboard_buttons/I.png', None],
  'J': [sys.path[0] +'/pages/images/keyboard_buttons/J.png', None],
  'K': [sys.path[0] +'/pages/images/keyboard_buttons/K.png', None],
  'L': [sys.path[0] +'/pages/images/keyboard_buttons/L.png', None],
  'M': [sys.path[0] +'/pages/images/keyboard_buttons/M.png', None],
  'N': [sys.path[0] +'/pages/images/keyboard_buttons/N.png', None],
  'O': [sys.path[0] +'/pages/images/keyboard_buttons/O.png', None],
  'P': [sys.path[0] +'/pages/images/keyboard_buttons/P.png', None],
  'Q': [sys.path[0] +'/pages/images/keyboard_buttons/Q.png', None],
  'R': [sys.path[0] +'/pages/images/keyboard_buttons/R.png', None],
  'S': [sys.path[0] +'/pages/images/keyboard_buttons/S.png', None],
  'T': [sys.path[0] +'/pages/images/keyboard_buttons/T.png', None],
  'U': [sys.path[0] +'/pages/images/keyboard_buttons/U.png', None],
  'V': [sys.path[0] +'/pages/images/keyboard_buttons/V.png', None],
  'W': [sys.path[0] +'/pages/images/keyboard_buttons/W.png', None],
  'X': [sys.path[0] +'/pages/images/keyboard_buttons/X.png', None],
  'Y': [sys.path[0] +'/pages/images/keyboard_buttons/Y.png', None],
  'Z': [sys.path[0] +'/pages/images/keyboard_buttons/Z.png', None],


  # Keyboard Buttons: Other
  'BACK': [sys.path[0] +'/pages/images/keyboard_buttons/BACK.png', None],
  'ENTER': [sys.path[0] +'/pages/images/keyboard_buttons/ENTER.png', None],
  'SPACE': [sys.path[0] +'/pages/images/keyboard_buttons/SPACE.png', None],
  'UP_ARROW': [sys.path[0] +'/pages/images/keyboard_buttons/UP_ARROW.png', None],

  # Keyboard Symbols
  '!': [sys.path[0] +'/pages/images/keyboard_buttons/exclamation_point.png', None],
  '@': [sys.path[0] +'/pages/images/keyboard_buttons/at.png', None],
  '#': [sys.path[0] +'/pages/images/keyboard_buttons/hashtag.png', None],
  '$': [sys.path[0] +'/pages/images/keyboard_buttons/dollar_sign.png', None],
  '%': [sys.path[0] +'/pages/images/keyboard_buttons/percent.png', None],
  '&': [sys.path[0] +'/pages/images/keyboard_buttons/and.png', None],
  '*': [sys.path[0] +'/pages/images/keyboard_buttons/asterisk.png', None],
  '(': [sys.path[0] +'/pages/images/keyboard_buttons/left_paren.png', None],
  ')': [sys.path[0] +'/pages/images/keyboard_buttons/right_paren.png', None],
  '?': [sys.path[0] +'/pages/images/keyboard_buttons/question_mark.png', None],
  '+': [sys.path[0] +'/pages/images/keyboard_buttons/plus.png', None],
  '-': [sys.path[0] +'/pages/images/keyboard_buttons/minus.png', None],
  '=': [sys.path[0] +'/pages/images/keyboard_buttons/equals.png', None],
  ',': [sys.path[0] +'/pages/images/keyboard_buttons/comma.png', None],
  ';': [sys.path[0] +'/pages/images/keyboard_buttons/semicolon.png', None],
  ':': [sys.path[0] +'/pages/images/keyboard_buttons/colon.png', None],
  '/': [sys.path[0] +'/pages/images/keyboard_buttons/backslash.png', None],
  'apostrophe': [sys.path[0] +'/pages/images/keyboard_buttons/apostrophe.png', None],
  'quotation': [sys.path[0] +'/pages/images/keyboard_buttons/quotation_marks.png', None],


  ## Settings Pages

  # First Screen
  'bright': [sys.path[0] +'/pages/images/settings_buttons/brightness_and_sound_Button.png', None],
  'adjust': [sys.path[0] +'/pages/images/settings_buttons/adjust_feeds_Button.png', None],
  'restore': [sys.path[0] +'/pages/images/settings_buttons/restore_to_defaults_Button.png', None],
  'scale': [sys.path[0] +'/pages/images/settings_buttons/scale_config_Button.png', None],

  # Brightness Screen
  'selections': [sys.path[0] +'/pages/images/settings_buttons/save_selections_Button.png', None],

  # Adjust Feed Screen
  'adjust_bump': [sys.path[0] +'/pages/images/settings_buttons/bump_for_adjust_feed_screen_Button.png', None],
  'adjust_coarse': [sys.path[0] +'/pages/images/settings_buttons/coarse_for_adjust_feed_screen_Button.png', None],
  'adjust_fine': [sys.path[0] +'/pages/images/settings_buttons/fine_for_adjust_feed_screen_Button.png', None],
  'save adjustments': [sys.path[0] +'/pages/images/settings_buttons/save_adjustments_Button.png', None],


}

def get(name):
  if name in imagelist:
       imagelist[name][1] = PhotoImage(file=imagelist[name][0])
  return imagelist[name][1]