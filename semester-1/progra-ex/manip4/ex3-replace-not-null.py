def replace_non_zeros(lst: list) -> None:
    lst_length = len(lst)
    for x in range(lst_length):
        if lst[x] != 0:
            lst[x] = 1
    print(lst)

lst = [1, 32, 0, 1, 0]
replace_non_zeros(lst)
