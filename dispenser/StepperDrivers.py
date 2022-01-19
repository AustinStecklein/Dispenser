#import Adafruit_BBIO.PWM as PWM #looks like it runs python 3.7
import Adafruit_BBIO.PWM as PWM #import PWM library

class StepperDriver:
    def __init__(self):
        pass #Possiblly turn on pins or driver

    def run(self, speed):
        #PWM.start(channel, duty, freq=2000, polarity=0)
        #Channel needs to defined in terms of pin & polarity is direction
        pass #Running the motor

    def stop (self):
        pass #define full stop