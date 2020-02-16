commande = input("Entrez une commande (O, X, F, P)")


def ouvrir():
    nom_fichier = input("Entrez le nom du fichier à ouvrir: ")
    print(f"Ouverture du fichier {nom_fichier}")

def sortir():
    confirm = input("Etes vous sur de vouloir quitter? [y/n]: ")
    if confirm == "y":
        print("Sortie du programme")

def fermer():
    confirm = input("Etes vous sur de vouloir fermer le fichier? [y/n]: ")
    if confirm == "y":
        print("Fermeture du fichier")

def imprimer():
    nb_impression = int(input("Entrez le nombre d'impressions à effectuer: "))
    print(f"Les {nb_impression} impressions sont en cours")

if commande == "O":
    ouvrir()

elif commande == "X":
    sortir()

elif commande == "F":
    fermer()

elif commande == "P":
    imprimer()

else:
    print("commande non valide")
