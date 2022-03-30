import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
from pages.backend_modules.Database import *
import time


#Angle Motor Driver Board 
AStep = "P8_19"
ADir = "P8_7"
ASlp = "P8_9"
AMS1 = "P8_15"
AMS2 = "P8_17"
AEna = "P8_8"
#Trickler Motor Driver Board
MStep = "P8_13"
MDir = "P8_10"
MSlp = "P8_12"
MMS1 = "P8_14"
MMS2 = "P8_16"
MEna = "P8_26"



#Angle Driver Motor Board
GPIO.setup(AStep, GPIO.OUT, GPIO.PUD_DOWN)
GPIO.setup(ADir, GPIO.OUT, GPIO.PUD_DOWN)
GPIO.setup(ASlp, GPIO.OUT, GPIO.PUD_DOWN)
GPIO.setup(AMS1, GPIO.OUT, GPIO.PUD_UP)
GPIO.setup(AMS2, GPIO.OUT, GPIO.PUD_UP)
GPIO.setup(AEna, GPIO.OUT, GPIO.PUD_UP)

#Trickler Driver Motor Board
#GPIO.setup(MStep, GPIO.OUT)#, GPIO.PUD_DOWN)
GPIO.setup(MDir, GPIO.OUT, GPIO.PUD_DOWN)
GPIO.setup(MSlp, GPIO.OUT, GPIO.PUD_DOWN)
GPIO.setup(MMS1, GPIO.OUT, GPIO.PUD_UP)
GPIO.setup(MMS2, GPIO.OUT, GPIO.PUD_UP)
GPIO.setup(MEna, GPIO.OUT, GPIO.PUD_UP)

def Start(speed):
    GPIO.output(MEna,GPIO.LOW)
    GPIO.output(MSlp, GPIO.HIGH) #Turns on Driver Board
    GPIO.output(MDir, GPIO.LOW) # Sets Direction
    GPIO.output(MMS1, GPIO.LOW) # Sets MicroStep Switch 1
    GPIO.output(MMS2, GPIO.HIGH) # Sets MicroStep Switch 2
    
    if speed == 1:
        PWM.start(MStep, 50, 1000)
    elif speed == 2:
        PWM.start(MStep, 50, 1500)
    else:
        PWM.start(MStep, 50, 2000)
        
def Stop():
    PWM.stop(MStep)
    PWM.cleanup()
    GPIO.output(MEna, GPIO.HIGH)
    GPIO.output(MSlp, GPIO.LOW)
 
    
def cal():
    speeds = ["FSpeed", "MSpeed", "SSpeed"]
    for i in range(3):
        start = float(getSetting("CurrentW"))
        Start(i)
        time.sleep(2)
        Stop()
        time.sleep(5)
        finish = float(getSetting("CurrentW"))
        setSetting(speeds[i-1], str((finish-start)/2))
        
def autorun():
    slow = float(getSetting("SSpeed"))
    med = float(getSetting("MSpeed"))
    fast = float(getSetting("FSpeed"))
    target = float(getSetting("TargetW"))
    
    gab = target - float(getSetting("CurrentW"))
    while(gab > .1):
        if(gab > fast/2):
            Start(3)
        elif(gab > med/2):
            Start(2)
        elif(gab > slow/2):
            Start(1)
        else:
            print("finish")
            break
        time.sleep(.5)
        Stop()
        time.sleep(4)
        gab = target - float(getSetting("CurrentW"))
        
        
def angleChange(direction):
    
    GPIO.output(AEna,GPIO.LOW)
    GPIO.output(ASlp, GPIO.HIGH) #Turns on Driver Board
    if direction:
        GPIO.output(ADir) # Sets Direction
    else:
        GPIO.output(ADir, GPIO.HIGH)
    GPIO.output(AMS1, GPIO.LOW) # Sets MicroStep Switch 1
    GPIO.output(AMS1, GPIO.HIGH) # Sets MicroStep Switch 2
    PWM.start(AStep, 50, 1000)

    PWM.stop(AStep)
    PWM.cleanup()
    GPIO.output(AEna, GPIO.HIGH)
    GPIO.output(ASlp, GPIO.LOW)

    
    
        
