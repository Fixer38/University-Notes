nb = int(input("Entrez un nombre: "))
summ = 0

while nb >= 0:
    summ += nb
    nb = int(input("Entrez un nombre: "))

print(f"La somme de tous ces nombres est de: {summ}")
