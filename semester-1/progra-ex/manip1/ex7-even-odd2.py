import timeit


code_to_test = """
nb = int(input("Enter a number: "))
if nb % 2 == 0:
    print(True)
"""

print(timeit.timeit(code_to_test, number=5)/100)
