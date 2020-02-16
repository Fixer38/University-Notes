from random import randint
nb1 = randint(0, 100)

nb_input = int(input("Entrez un nombre: "))
tries = 0

while nb_input != nb1 and tries < 5:
    if nb_input < nb1:
        print("trop petit")

    else:
        print("trop grand")

    tries += 1
    nb_input = int(input("Entrez un nombre: "))

if tries >= 5:
    print("Vous avez perdu")

else:
    print(f"Vous avez trouvé le nombre caché était donc bien: {nb1}")
