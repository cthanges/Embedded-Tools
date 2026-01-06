import re

LOG_PATTERN = re.compile(r"\[(\d+)\]\[(\w+)\]\[(\w+)\]\s+(.*)") # Pattern for the log entries

file_path = "sample_logs.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()

    for line in lines:
        print(line.strip())