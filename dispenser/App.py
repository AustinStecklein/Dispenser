from GUI import GUI
from Eventhandler import Eventhandler


if __name__ == '__main__':
    event_handler = Eventhandler()
    gui = GUI(event_handler)
    print("Application started")
