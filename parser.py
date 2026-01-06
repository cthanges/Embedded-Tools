file_path = "sample_logs.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()

    for line in lines:
        print(line.strip())