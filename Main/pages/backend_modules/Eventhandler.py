from pages.backend_modules.Database import *
import threading
from pages.backend_modules.StepperDriver import *
from pages.backend_modules.event import Event
import serial
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM


#Sets up Analog Pin values
ADC.setup()
AValue = "P9_40" #Assigns Pin to Variable, must use ADC.read to read value
speaker = "P9_22"
haptic = "P9_24"


GPIO.setup(haptic, GPIO.OUT)


def readScale():
    ser = serial.Serial()
    ser.port = '/dev/ttyUSB0'
    ser.baudrate = 9600
    ser.open()
    while 1:
        line = ser.readline()
        try:
            line = line.decode('UTF-8')
            setSetting("CurrentW", line[:-6])
        except:
            print("Started in wrong state")
    
    
class Eventhandler():
    def __init__(self):
        init_database()
        self.threads = {}
        self.startThread(readScale, "readScale")
        setSetting("CurrentW", "0")
    
    #Returns a string value for target weight
    def getTargetWeight(self):
        return getSetting("TargetW")

    #returns a string value for the current weight
    def getcurrentWeight(self):
        return getSetting("CurrentW")
    
    def clearTarget(self):
        SetSetting("TargetW", float(0))
        
    #Takes a string value and adds it to the end of the string
    def addDigit(self, digit):
        current = self.getTargetWeight * 10
        setSetting("TargetW", current + (digit * .01))
    
    #This will remove the last digit in the string
    #def backspace(self):
        #setSetting("TargetW", 0)

    def Manual_slow(self):
        self.regEvent(Event.MANUAL_SLOW)

    def Manual_med(self):
        self.regEvent(Event.MANUAL_MED)

    def Manual_fast(self):
        self.regEvent(Event.MANUAL_FAST)
    
    def auto_target(self):
        self.regEvent(Event.AUTO_TARGET)
        pass
    
    def calibrate(self):
        cal()
        
    def readAngle(self):
        ARaw = ADC.read(AValue)
        Angle = (ARaw - 0.4968)/0.0016
        setSetting("angle", Angle)
    
    def playSound(self):
        PWM.start(speaker, 50, 256)
        time.sleep(.2)
        PWM.stop(speaker)
        PWM.cleanup()

    def playHaptic(self):
        GPIO.output(haptic, GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(haptic, GPIO.LOW)
    
    def angle_change(self, angle):
        self.regEvent(Event.MANUAL_ANGLE_CHANGE, direction)

    def stop(self):
        Stop()

    def save_data(self, Name, Cartridge, Bullet, Powder, Charge, Weight, COAL, Primer, Brass, Notes):
        addCard(Name, Cartridge, Bullet, Powder, Charge, Weight, COAL, Primer, Brass, Notes)
    
    def get_data(self):
        return getCards()

    def regEvent(self, event, *args):
        if event == Event.MANUAL_SLOW:
            self.startThread(Start, "dispense", 1)
        elif event == Event.MANUAL_MED:
            self.startThread(Start, "dispense", 2)
        elif event == Event.MANUAL_FAST:
            self.startThread(Start,"dispense", 3)
        elif event == Event.AUTO_TARGET:
            self.startThread(autorun, "auto")
        elif event == Event.MANUAL_ANGLE_CHANGE:
            #currentAngle = getSetting("angle")
            self.startThread(StepperDriver.angleChange, args)
        elif event == Event.FULL_STOP:
            Stop()

    def startThread(self, pros, name, *args):
        thread = threading.Thread(target=pros, args=(args))
        thread.start()
        self.threads[name] = thread

   
            
