global nb
nb = int(input("Entrez un nombre: "))

def check_carre():
    racine = nb ** 0.5

    if racine.is_integer():
        print("le nombre est carré")

    else:
        print("le nombre n'est pas carré")


check_carre()
