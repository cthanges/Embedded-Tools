from fsm import FSM, State
from events import Event

def event_menu():
    print("\nAvailable events:")
    for event in Event:
        print(f"- {event.name.lower()}")

def user_event_choice():
    user_input = input("\nEnter event (or 'exit'): ").strip().upper()

    if user_input == "EXIT":
        return None

    try:
        return Event[user_input]
    except KeyError:
        print("ERROR: Invalid event. Enter a valid event name.")
        return "INVALID"

def main():
    fsm = FSM()
    print("=== Embedded FSM Simulator ===")
    print(f"Initial State: {fsm.state.name}")

    while True:
        event_menu()
        event = user_event_choice()

        if event is None:
            print("Exiting simulator.")
            break

        if event == "INVALID":
            continue

        fsm.on_event(event)
        print(f"Current State: {fsm.state.name}")

if __name__ == "__main__":
    main()

'''
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
    for event in events:
        fsm.on_event(event)

if __name__ == "__main__":
    main()
'''