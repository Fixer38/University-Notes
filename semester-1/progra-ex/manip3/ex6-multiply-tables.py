def print_multiply_tables(nb, start=1, end=10):
    i = start
    while i <= end:
        print(f"{nb} * {i} = {nb * i}")
        i += 1

print_multiply_tables(2, 5, 12)
