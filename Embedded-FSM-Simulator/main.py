from fsm import FSM
from events import Event

def main():
    fsm = FSM()

    # Just an example sequence of events
    events = [Event.POWER_ON,
              Event.INIT_COMPLETE,
              Event.START_COMMAND,
              Event.ERROR_DETECTED,
              Event.RESET,
              Event.START_COMMAND,
              Event.SHUTDOWN]

    # Process each event
    for e in events:
        fsm.on_event(e)

if __name__ == "__main__":
    main()