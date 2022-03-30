import datetime
import math
from pages.backend_modules.Eventhandler import *

# TODO: give actual backend functions

event_handler = Eventhandler()

target = ""
tilt = 0
speed = 50
load_list = ['Test Load #' + str(x) for x in range(17)]
load_page = 1
bump_strength = 0.01
fine_strength = 0.1
coarse_strength = 1.00

# Sets the default value for the units variable shown on the main menu page to grains
units = "gr"
tilt = 0
speed = 50

# Sets the default value for label_counter to 0
label_counter = 0

# Sets the default value for every category for the Save Page to blank to ensure the user can start fresh everytime
keyboard_label = ""
file_name = "Card #2"
cartridge = ""
bullet = ""
powder = ""
charge = ""
coal = ""
primer = ""
brass = ""
notes = ""

# Settings variables
backlight_brightness = 50 # 0 to 100
notification_volume = 50 # 0 to 100
button_volume = 50 # 0 to 100
haptic_mode = 'Option 1'
startResetDefaults = False

def coarse_feed(x):
    global event_handler
    event_handler.Manual_fast()

def stop_coarse_feed(x):
    global event_handler
    event_handler.stop()

def fine_feed(x):
    global event_handler
    event_handler.Manual_med()
    
def stop_fine_feed(x):
    global event_handler
    event_handler.stop()

def bump_feed(x):
    global event_handler
    event_handler.Manual_slow()

def stop_bump_feed(x):
    global event_handler
    event_handler.stop()

def power_off():
    print('Power off')

def set_backlight(value):
    global backlight_brightness
    backlight_brightness = value

def get_backlight():
    global backlight_brightness
    return backlight_brightness

def set_notification_volume(value):
    global notification_volume
    notification_volume = value

def get_notification_volume():
    global notification_volume
    return notification_volume

def set_button_volume(value):
    global button_volume
    button_volume = value

def get_button_volume():
    global button_volume
    return button_volume

def set_haptic(option):
    global haptic_mode
    haptic_mode = option

def get_haptic():
    global haptic_mode
    return int(haptic_mode[-1]) - 1

def needsReset():
    global startResetDefaults
    return startResetDefaults

def startReset():
    global startResetDefaults
    startResetDefaults = True

def finishReset():
    global startResetDefaults
    startResetDefaults = False

def next_page():
    global load_page
    load_page += 1

def prev_page():
    global load_page
    load_page -= 1

def get_page():
    global load_page
    return str(load_page)

def total_pages():
    global load_list
    return int(math.ceil(len(load_list) / 5))

def get_target():
    global event_handler
    target = event_handler.getTargetWeight()
    return str(target)

def increase_bump():
    global bump_strength
    bump_strength += 0.01

def decrease_bump():
    global bump_strength
    bump_strength -= 0.01

def increase_fine():
    global fine_strength
    fine_strength += 0.1

def decrease_fine():
    global fine_strength
    fine_strength -= 0.1

def increase_coarse():
    global coarse_strength
    coarse_strength += 1

def decrease_coarse():
    global coarse_strength
    coarse_strength -= 1

def load_preset(load_string):
    print(f'Loading {load_string}')

def edit_preset(load_string):
    print(f'Editing {load_string}')

def begin_calibration():
    print('Calibrating...')
    global event_handler
    event_handler.calibrate()

def set_counter(new_counter):
    global label_counter
    label_counter = new_counter

def get_counter():
    global label_counter
    return label_counter

def set_label(new_label):
    global keyboard_label
    keyboard_label = new_label

def get_label():
    global keyboard_label
    return keyboard_label

def read_scale():
    global event_handler
    return event_handler.getcurrentWeight()

def set_filename(new_filename):
    global file_name
    file_name = new_filename

def get_filename():
    global file_name
    return str(file_name)

def set_cartridge(new_cartridge):
    global cartridge
    cartridge = new_cartridge

def get_cartridge():
    global cartridge
    return str(cartridge)

def set_bullet(new_bullet):
    global bullet
    bullet = new_bullet

def get_bullet():
    global bullet
    return str(bullet)

def set_powder(new_powder):
    global powder
    powder = new_powder

def get_powder():
    global powder
    return str(powder)

def set_charge(new_charge):
    global charge
    charge = new_charge

def get_charge():
    global charge
    return str(charge)

def set_coal(new_coal):
    global coal
    coal = new_coal

def get_coal():
    global coal
    return str(coal)

def set_primer(new_primer):
    global primer
    primer = new_primer

def get_primer():
    global primer
    return str(primer)

def set_brass(new_brass):
    global brass
    brass = new_brass

def get_brass():
    global brass
    return str(brass)

def set_notes(new_notes):
    global notes
    notes = new_notes

def get_notes():
    global notes
    return str(notes)

def new_units(new_units):
    global units
    units = new_units

def get_units():
    global units
    return units

def set_target(new_target):
    global target
    target = new_target

def add_target_digit(digit):
    global target
    target = target + digit

def numpad_clear():
    global target
    target = ''

def increase_tilt():
    global tilt
    tilt += 1
    
def decrease_tilt():
    global tilt
    tilt -= 1
    
def increase_speed():
    global speed
    speed += 1
    
def decrease_speed():
    global speed
    speed -= 1

def get_trickler_speed():
    global speed
    return str(speed)

def get_test_name():
    global file_name
    return str(file_name)
    
def get_trickler_tilt():
    global tilt
    return str(tilt)

def get_load_list():
    global load_list
    return load_list

def get_save_list():
    global save_list
    return save_list

def get_save_list1():
    global save_list1
    return save_list1






