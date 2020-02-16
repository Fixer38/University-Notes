def letters_count(word: str) -> dict:
    dict_count = {}
    for letter in word:
        if letter in dict_count:
            dict_count[letter] += 1
        else:
            dict_count[letter] = 1
    return dict_count

dict_count = letters_count('hello')
print(dict_count)
