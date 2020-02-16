def invert_letter_state(letter):
    if letter.isupper():
        return letter.lower()
    else:
        return letter.upper()

print(invert_letter_state("E"))
print(invert_letter_state("e"))
