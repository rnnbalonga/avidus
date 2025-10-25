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

def reverse_second_word(sentence):
    second_word = sentence.split()[1]
    return second_word[::-1]

with open("poem.txt", "r") as file:
    content = file.readlines()
    for line in content:
        line = line.strip()
        line = arrange_lines(line)