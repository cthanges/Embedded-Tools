# UART Log Parser

## Summary
This is a Python-based utility that parses UART-style log output from embedded systems, converts raw log lines into structured data, and generates a system-level summary report. This tool simulates host-side log analysis commonly used during embedded firmware development and debugging.

## Features
- Parses UART-style logs using regular expressions
- Extracts timestamp, log level, module, and message
- Supports filtering logs by severity level (ERROR, WARN)
- Generates a system summary including:
    - Total error count
    - Total warning count
    - Last finite state machine (FSM) state
- Clean separation between parsing, analysis, and reporting logic

[<timestamp_ms>][<LEVEL>][<MODULE>] <message>