import datetime

# Placeholders for backend functions

target = ""

def read_scale():
    return str(datetime.datetime.now())

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
    print('increase tilt')
    
def decrease_tilt():
    print('decrease tilt')
    
def increase_speed():
    print('increase speed')
    
def decrease_speed():
    print('decrease speed')

def get_trickler_speed():
    return "95"
    
def get_trickler_tilt():
    return "5"