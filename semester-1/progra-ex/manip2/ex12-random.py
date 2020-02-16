from random import randint
nb1 = randint(0, 100)

nb_input = int(input("Entrez un nombre: "))

while nb_input != nb1:
    if nb_input < nb1:
        print("trop petit")

    else:
        print("trop grand")

    nb_input = int(input("Entrez un nombre: "))

print(f"Vous avez trouvé le nombre caché était donc bien: {nb1}")
