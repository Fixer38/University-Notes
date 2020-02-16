def print_tails(lst: list) -> None:
    length = len(lst)
    for x in range(length):
        for y in range(x, length):
            print(lst[y])

lst = [3, 7, 9]
print_tails(lst)
