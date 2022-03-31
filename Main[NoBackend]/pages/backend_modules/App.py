
from Eventhandler import Eventhandler
import time
from Database import *


if __name__ == '__main__':
    event_handler = Eventhandler()
    #setSetting("TargetW", 1)
    event_handler.playHaptic()
    time.sleep(1)
    event_handler.playSound()
    
    
    #event_handler.calibrate()
    
    #print(str(getSetting("FSpeed")))
    #print(str(getSetting("MSpeed")))
    #print(str(getSetting("SSpeed")))
    #while(1):
        #time.sleep(1)
        #print(getSetting("CurrentW"))