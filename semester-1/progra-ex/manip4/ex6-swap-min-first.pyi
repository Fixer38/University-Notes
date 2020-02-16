def swap_min_first(lst: list) -> None:
    elem_min = min(lst)
    lst[lst.index(elem_min)] = lst[0]
    lst[0] = elem_min
    print(lst)

lst = [3, 4, 1, 2]
swap_min_first(lst)
