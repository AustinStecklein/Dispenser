import datetime

# Placeholders for backend functions

target = ""
tilt = 0
speed = 50
load_list =  ['load1', 'load2', 'load3']
save_list =  ['Cartridge: ', 'Bullet: ', 'Powder: ', "Charge Weight: ", 'C.O.A.L.: ']
save_list1 = ['Primer: ', 'Brass: ', 'Notes: ']
test_name = "Filename"
units = "gr"

def read_scale():
    return str(datetime.date.today().strftime('%m.%d'))

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
    global test_name
    return str(test_name)
    
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

def new_units(new_units):
    global units
    units = new_units

def get_units():
    global units
    return units