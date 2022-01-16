from enum import Enum 

class Event(Enum):
    AUTO_TARGET = 1,
    MANUAL_SLOW = 2,
    MANUAL_MED = 3,
    MANUAL_FAST = 4,
    MANUAL_STOP = 5,
    MANUAL_ANGLE_CHANGE = 6,
    GET_WEIGHT = 7,
    SAVE_DATA = 8,
    