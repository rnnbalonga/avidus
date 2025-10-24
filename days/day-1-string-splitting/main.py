# Open anomaly_labels.txt
# Ignore header and newlines (if any)
# Split each line in txt file with a delimiter.
# Last line has multiple delimiters. Find a solution that can handle everything all at once.

import re

def uniform_delimiters(line):
    return re.split(r"[|;+-]", line)

with open("OpenStack/anomaly_labels.txt", "r") as file:
    next(file)
    content = file.readlines() 
    for line in content:
        if line != "\n":
            formatted_line = uniform_delimiters(line.rstrip("\n"))
            print(formatted_line)
        else:
            pass