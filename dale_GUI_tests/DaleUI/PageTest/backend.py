import datetime

target = ""

def read_scale():
    return str(datetime.datetime.now())

def set_target(new_target):
    global target
    target = new_target

def add_target_digit(digit):
    global target
    target = target + digit



def get_target():
    global target
    return target
