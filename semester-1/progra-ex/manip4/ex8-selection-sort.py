def swap_min_first(lst: list) -> list:
    elem_min = min(lst)
    lst[lst.index(elem_min)] = lst[0]
    lst[0] = elem_min
    return lst

def selection_sort(lst: list) -> None:
    for _ in lst:
        lst = swap_min_first(lst)
    print(lst)

lst = [3, 2, 1, 8]
selection_sort(lst)
