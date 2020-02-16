nb1 = int(input("Entrez un nombre: "))

summ = 1
i = 1

while i <= nb1:
    print(i, i+1)
    summ = summ * i
    print(summ)
    i += 1

print(f"La factorielle de ce nombre est égal à: {summ}")
