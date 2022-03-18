import datetime
import Images

# Placeholders for backend functions

target = ""
tilt = 0
speed = 50
load_list =  ['load1', 'load2', 'load3']
save_list =  ['Cartridge: ', 'Bullet: ', 'Powder: ', "Charge Weight: ", 'C.O.A.L.: ']
save_list1 = ['Primer: ', 'Brass: ', 'Notes: ']
file_name = "Card #2"
units = "gr"
label_counter = 0
keyboard_label = ""

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
    if (units == "gr"):
        return "000.000"
    if (units == "lb"):
        return str(datetime.date.today().strftime('%d.%m'))
    if (units == "g"):
        return str(datetime.date.today().strftime('%y'))
    else:
        return "00.00"

def set_filename(new_filename):
    global file_name
    file_name = new_filename

def get_filename():
    global file_name
    return str(file_name)

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

def get_target():
    global target
    return target

def coarse_feed():
    print('coarse feed')

def fine_feed():
    print('fine feed')

def bump_feed():
    print('bump feed')

def power_off():
    print('Power off')

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

def load_preset(load_string):
    print(f'Loading {load_string}')






