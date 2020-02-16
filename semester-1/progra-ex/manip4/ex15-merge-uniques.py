def merge_uniques(lst_from: list, lst_to: list) -> None:
    for tup in lst_from:
        if tup not in lst_to:
            lst_to.append(tup)
    print(lst_to)
    print(len(lst_to)-len(lst_from))

lst_from = [(1, 2, 3), (9, 9, 0), (5, 6, 8)]
lst_to = [(1, 2, 3), (3, 4), (9, 1, 2)]
merge_uniques(lst_from, lst_to)
