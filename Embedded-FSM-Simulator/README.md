# Embedded FSM Simulator

## Summary
This is a Python-based Finite State Machine (FSM) simulator designed to model and test embedded-style state transitions driven by events. This project demonstrates how FSM logic commonly used in embedded systems and firmware can be structured, validated, and tested in a high-level environment before being ported to C. FSMs are a core concept in embedded systems, used in boot sequences, device control logic, communication protocols, and fault handling and recovery.

## Design
**STATES:**
- BOOT
- INIT
- IDLE
- RUNNING
- ERROR
- SHUTDOWN

**EVENTS:**
- POWER_ON
- INIT_COMPLETE
- START_COMMAND
- ERROR_DETECTED
- RESET
- SHUTDOWN

## Features
This simulator models a realistic embedded FSM with:
- Explicit states and events
- Deterministic state transitions
- Error handling paths
- Console-based interactive testing

## Project Structure
- **fsm.py:** FSM logic and state transitions
- **events.py:** Event enum definitions
- **main.py:** Interactive console interface (for user input)

## Running the Program
Ensure that Python 3 is installed.

To run the simulator:
```
python main.py
```