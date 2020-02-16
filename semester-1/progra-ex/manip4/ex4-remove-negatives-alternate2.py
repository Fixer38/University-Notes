def remove_negatives(lst: list) -> None:
    lst = [i for i in lst if i >= 0]
    print(lst)

lst = [-99, -101, 204, 52, -64]
remove_negatives(lst)
