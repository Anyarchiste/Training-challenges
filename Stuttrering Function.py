
def stutter(word_def):
    new_word = ""
    for y in range(0, 2):
        for n in range(0, 2):
            new_word += word_def[n]
        new_word += "... "
    new_word += word_def
    return new_word


word = "Prout"
stutter = stutter(word)
print(stutter())
