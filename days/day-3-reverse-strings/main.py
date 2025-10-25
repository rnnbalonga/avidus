#Mission: Reverse every second word of a string.
#Bonus:
# Create a cleaner looking file.
# Arrange pars neatly. One par (poem) per par in new file.
# One line break in between stanzas.

def split_sentence(sentence):
    return sentence.split(" ")

def reverse_second_word(sentence_list):
    if len(sentence_list) > 1:
        second_word = sentence_list[1]
        reverse_second_word = second_word[::-1]
        sentence_list[1] = reverse_second_word
        return sentence_list
    else:
        return sentence_list

def join_sentence_list(sentence_list):
    sentence = " ".join(sentence_list)
    return sentence

with open("poem.txt", "r") as file:
    content = file.readlines()
    for par in content:
        if par == "\n":
            print("")
        else:
            par = par.split(".") #split pars with . as delimiter
            if "\n" in par:
                par.remove("\n")
            for sentence in par:
                clean_sentence = sentence.strip()
                sentence_list = split_sentence(clean_sentence)
                sentence_list = reverse_second_word(sentence_list)
                clean_sentence = join_sentence_list(sentence_list)
                if "Desiderata" in clean_sentence:
                    print(clean_sentence)
                else:
                    print(f"{clean_sentence}.")