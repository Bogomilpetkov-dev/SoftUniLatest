text = input()
#word_length = len(text)

value=0
for letter in text:

    if letter == "a":
        value = 1 + value
    elif letter == "e":
        value = 2 + value
    if letter == "i":
        value = 3 + value
    if letter == "o":
        value = 4 +value
    if letter == "u":
        value = 5 +value


print(value)
