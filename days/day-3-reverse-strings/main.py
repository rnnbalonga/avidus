#Mission: Reverse every second word of a string.
#Bonus:
# Create a cleaner looking file.
# Arrange lines neatly. One line (poem) per line in new file.
# One line break in between stanzas.
def arrange_lines(text):
    line = text.split(".")
    for sentence in line:
        if sentence != "":
            print(f"{sentence.strip()}.")

with open("poem.txt", "r") as file:
    content = file.readlines()
    for line in content:
        line = line.strip()
        arrange_lines(line)