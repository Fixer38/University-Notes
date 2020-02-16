def str_to_low(s: str) -> str:
    lowered_s = ""
    for letter in s:
        if 'A' <= letter <= 'Z':
            lowered_letter = chr(ord(letter)+32)
        lowered_s += lowered_letter
    return lowered_s

s = "HELlO"
print(str_to_low(s))
