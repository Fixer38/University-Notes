import timeit

code_to_test = """
nb = int(input("Nombre: "))
print(nb % 2 == 0)
"""
print(timeit.timeit(code_to_test, number=5)/100)
