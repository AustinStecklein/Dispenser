from re import A
from Database import *
import multiprocessing
from StepperDrivers import *
from event import Event


class Eventhandler():
    def __init__(self):
        self.start()
        self.threads = []
    
    #Returns a string value for target weight
    def getTargetWeight(self):
        return getSetting("TargetW")

    #returns a string value for the current weight
    def getcurrentWeight(self):
        return getSetting("CurrentW")

    #Takes a string value and adds it to the end of the string
    def addDigit(self, digit):
        current = self.getTargetWeight * 10
        setSetting("TargetW", current + (digit * .01))
    
    #This will remove the last digit in the string
    def backspace(self):
        setSetting("TargetW", 0)

    def Manual_slow(self):
        self.regEvent(Event.MANUAL_SLOW)

    def Manual_med(self):
        self.regEvent(Event.MANUAL_MED)

    def Manual_fast(self):
        self.regEvent(Event.MANUAL_FAST)
    
    def auto_target(self):
        self.regEvent(Event.AUTO_TARGET)

    def angle_change(self, angle):
        self.regEvent(Event.MANUAL_ANGLE_CHANGE, angle)

    def get_weight(self):
        return getSetting("CurrentW")

    def stop(self):
        self.regEvent(Event.FULL_STOP)

    def save_data(self, Name, Cartridge, Bullet, Powder, Charge, Weight, COAL, Primer, Brass, Notes):
        addCard(Name, Cartridge, Bullet, Powder, Charge, Weight, COAL, Primer, Brass, Notes)


    def regEvent(self, event, *args):
        if event == Event.MANUAL_SLOW:
            self.startThread(StepperDriver.bumpBarrel, 1)
        elif event == Event.MANUAL_MED:
            self.startThread(StepperDriver.bumpBarrel, 2)
        elif event == Event.MANUAL_FAST:
            self.startThread(StepperDriver.bumpBarrel, 3)
        elif event == Event.AUTO_TARGET:
            self.startThread(StepperDriver.autorun)
        elif event == Event.MANUAL_ANGLE_CHANGE:
            currentAngle = getSetting("angle")
            self.startThread(StepperDriver.runAngle, args[0], currentAngle)
        elif event == Event.FULL_STOP:
            StepperDriver.stopBarrel()
            self.stopAllThreads()

    def startThread(self, pros, *args):
        thread = multiprocessing.Process(target=pros, args=(args))
        thread.start()
        self.threads.append(thread)

    def stopAllThreads(self):
        for thread in self.threads:
            thread.terminate()
            