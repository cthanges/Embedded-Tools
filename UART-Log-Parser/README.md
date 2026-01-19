# UART Log Parser

## Summary
This is a mini-project (in Python (parser.py) and C (main.c)) that parses UART-style log output from embedded systems, converts raw log lines into structured data, and generates a system-level summary report. This tool simulates host-side log analysis commonly used during embedded firmware development and debugging.

Specifically, this tools demonstrates how it can be used to:
- Analyze firmware behavior
- Detect system faults
- Track state transitions
- Improve observability during development

## Features
- Parses UART-style logs using regular expressions
- Extracts timestamp, log level, module, and message
- Supports filtering logs by severity level (ERROR, WARN)
- Generates a system summary including:
    - Total error count
    - Total warning count
    - Last finite state machine (FSM) state
- Clean separation between parsing, analysis, and reporting logic

## Running the Program
### PYTHON
Ensure that Python 3 is installed.

For ALL entries:
```
python parser.py
```

For specific entries:
```
python parser.py ERROR
python parser.py WARN
```

### C
Ensure that a compiler for C (like gcc) is installed.

**Compilation:**
```
gcc main.c -o uart_parser
```

**Execution:**

For ALL entries:
```
./uart_parser
```

For specific entries:
```
./uart_parser ERROR
./uart_parser WARN
```

**On Windows:**
```
gcc main.c -o uart_parser.exe
uart_parser.exe
uart_parser.exe ERROR
```

Please note that this program expects [sample_logs.txt](https://github.com/cthanges/Embedded-Tools/blob/main/UART-Log-Parser/sample_logs.txt) to be in the same directory as the executable.