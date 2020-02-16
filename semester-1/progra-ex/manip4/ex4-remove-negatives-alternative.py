def remove_negatives(lst: list) -> None:
    i = len(lst) - 1
    while i >= 0:
        if lst[i] < 0:
            del lst[i]
        i -= 1
    print(lst)

lst = [-99, -101, 204, 52, -64]
remove_negatives(lst)

