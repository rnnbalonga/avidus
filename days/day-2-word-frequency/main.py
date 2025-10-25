#Find how many errors
#Find which day & hour had the most errors
#Which module contained the most errors

import re

with open("log.txt", "r") as log_file:
    lines = log_file.readlines(1)
    pattern = r"\[(\w{3})\s\w{3}\s\d{2}\s(\d{2}):\d{2}:\d{2}\s\d{4}\]\s\[(.*?)\]\s(.*)"
    for line in lines:
        match = re.match(pattern, line)
        if pattern:
            day_of_week, hour, level, message = match.groups()
            print(f"Day of week: {day_of_week}")
            print(f"Hour: {hour}")
            print(f"Level: {level}")
            print(f"Message: {message}")