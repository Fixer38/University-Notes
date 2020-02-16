decimal = int(input("Veuillez entrer un nombre de 0 à 15 en décimal : "))
i = 0
binary = ""

while i < 4:
    binary += str(decimal % 2)
    decimal //= 2
    i += 1
print(binary)

