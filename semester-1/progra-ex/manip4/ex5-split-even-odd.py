def split_even_odd(lst: list) -> tuple:
    return(lst[0::2], lst[1::2])

lst = [1, 4, 3, 8, 9]
print(split_even_odd(lst))
