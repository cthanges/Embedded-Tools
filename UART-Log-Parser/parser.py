import re
import sys

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

file_path = "sample_logs.txt"

parsed_entries = [] # Store a list of all parsed log entries

with open(file_path, 'r') as file:
    lines = file.readlines()

    for line in lines:
        parsed = parse_line(line.strip())
        if parsed:
            parsed_entries.append(parsed) # This is where we add the parsed entry to the list

# Analyze parsed log entries (Only considering error and warning levels for the summary report)
def analyze_logs(entries):
    stats = {"errors": 0,
             "warnings": 0,
             "last_fsm_state": None}

    for entry in entries:
        if entry["level"] == "ERROR":
            stats["errors"] += 1
        elif entry["level"] == "WARN":
            stats["warnings"] += 1

        if entry["module"] == "FSM":
            stats["last_fsm_state"] = entry["message"]

    return stats

# Prints the system summary
def print_summary(stats):
    print("\nSystem Summary")
    print("----------------")
    print(f"Errors: {stats['errors']}")
    print(f"Warnings: {stats['warnings']}")
    print(f"Last FSM State: {stats['last_fsm_state']}")

if __name__ == "__main__":
    filter_level = None
    if len(sys.argv) > 1:
        filter_level = sys.argv[1].upper() # enter ERROR or WARN

    for entry in parsed_entries:
        if filter_level and entry["level"] != filter_level:
            continue # Skip the entries that don't match the filter level
        print(entry)

    stats = analyze_logs(parsed_entries)
    print_summary(stats)