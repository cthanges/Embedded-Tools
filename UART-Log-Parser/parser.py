import re

LOG_PATTERN = re.compile(r"\[(\d+)\]\[(\w+)\]\[(\w+)\]\s+(.*)") # Pattern for the log entries

# Parse a single log line
def parse_line(line):
    match = LOG_PATTERN.match(line) # Check if the line matches the log pattern
    if not match:
        return None
    
    return {"timestamp": int(match.group(1)),
            "level": match.group(2),
            "module": match.group(3),
            "message": match.group(4)}

file_path = "UART-Log-Parser/sample_logs.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()

    for line in lines:
        print(parse_line(line.strip()))