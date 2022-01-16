import threading
from StepperDrivers import startStepper
from event import Event
import time

class Eventhandler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.start()
        self.Eventbuffer = []
    
    def quit(self):
        pass #Fill with threading ending calls

    def regEvent(self, event, *args):
        self.Eventbuffer.append(event)

    def startThread(self, pros):
        thread = threading.Thread(target=pros, args=())
        thread.start()

    def run(self):
        while(1):
            time.sleep(5)
            if(len(self.Eventbuffer) > 0):
                event = self.Eventbuffer.pop(0)
                if event == Event.MANUAL_SLOW:
                    self.startThread(startStepper)