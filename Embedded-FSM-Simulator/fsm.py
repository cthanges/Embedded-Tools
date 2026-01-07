from enum import Enum
from events import Event

class State(Enum):
    BOOT = 0
    INIT = 1
    IDLE = 2
    RUNNING = 3
    ERROR = 4
    SHUTDOWN = 5

class FSM:
    def __init__(self):
        self.state = State.BOOT

    def on_event(self, event):
        old_state = self.state # Before processing, we need to know the current state

        if self.state == State.BOOT:
            if event == Event.POWER_ON:
                self.state = State.INIT

        elif self.state == State.INIT:
            if event == Event.INIT_COMPLETE:
                self.state = State.IDLE
            elif event == Event.ERROR_DETECTED:
                self.state = State.ERROR

        elif self.state == State.IDLE:
            if event == Event.START_COMMAND:
                self.state = State.RUNNING
            elif event == Event.ERROR_DETECTED:
                self.state = State.ERROR
            elif event == Event.SHUTDOWN:
                self.state = State.SHUTDOWN

        elif self.state == State.RUNNING:
            if event == Event.ERROR_DETECTED:
                self.state = State.ERROR
            elif event == Event.SHUTDOWN:
                self.state = State.SHUTDOWN

        elif self.state == State.ERROR:
            if event == Event.RESET:
                self.state = State.INIT
            elif event == Event.SHUTDOWN:
                self.state = State.SHUTDOWN

        if old_state != self.state: # Did the state change?
            print(f"[FSM] {old_state.name} --{event}--> {self.state.name}")
        else:
            print(f"[FSM] Event '{event}' ignored in state {self.state.name}")

        return self.state