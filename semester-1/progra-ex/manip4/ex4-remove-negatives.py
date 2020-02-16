def remove_negatives(lst: list) -> None:
    lst_without_zeroes = []
    for elem in lst: 
        lst_without_zeroes.append(elem)
    print(lst_without_zeroes)
    length = len(lst)

lst = [-6, -7, 1, -9, 3]
remove_negatives(lst)
