import threading
import multiprocessing
from StepperDrivers import startStepper
from event import Event
import time

class Eventhandler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.start()
        self.threads = []
    

    def regEvent(self, event, *args):
        if event == Event.MANUAL_SLOW:
            self.startThread(startStepper)
        elif event == Event.FULL_STOP:
            self.stopAllThreads()

    def startThread(self, pros):
        thread = multiprocessing.Process(target=pros, args=())
        thread.start()
        self.threads.append(thread)

    def stopAllThreads(self):
        for thread in self.threads:
            thread.terminate()
            