from enum import Enum

class State(Enum):
    BOOT = 0
    INIT = 1
    IDLE = 2
    RUNNING = 3
    ERROR = 4
    SHUTDOWN = 5